import MySQLdb
from datetime import datetime
from hashlib import blake2b
from random import choice

from definitions import MIN_BALANCE, MAX_BALANCE, DATETIME_FORMAT, HASH_COMPONENTS


def generate_blake2_hash(plain_text: str, hkey_length: int = 32, hashed_bytesize: int = 16) -> tuple:
    """
    Return hash_key and hashed_text
    """
    hkey = "".join([choice(HASH_COMPONENTS) for _ in range(hkey_length)])
    hasher = blake2b(key=hkey.encode("utf-8"), digest_size=hashed_bytesize)
    hasher.update(plain_text.encode("utf-8"))
    return hkey, hasher.hexdigest()


class BasicDatabase:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host="127.0.0.1",
            port=3306,
            user="iotuser",
            passwd="iotuser",
            db="rfid_db"
        )

    def __del__(self):
        if self.conn is not None:
            self.conn.close()

    def execute_R(self, statement: str, args: tuple = (), fetch_counts: int = 0) -> tuple:
        try:
            cursor = self.conn.cursor()
            cursor.execute(statement, args)
            if fetch_counts == 0:
                return cursor.fetchall()
            if fetch_counts > 0:
                return cursor.fetchmany(fetch_counts)
        except MySQLdb.Error as e:
            print(e.args)
        return tuple()

    def execute_CUD(self, statement: str, args: tuple = ()):
        try:
            cursor = self.conn.cursor()
            cursor.execute(statement, args)
            self.conn.commit()
        except MySQLdb.Error as e:
            print(e.args)


class DatabaseInterface:
    def __init__(self):
        self.db = BasicDatabase()

    def find_all_cards(self) -> list[dict]:
        statement = "SELECT `rid`, `user_info`, `hash_key`, `balance`, `enable` FROM `Card`;"
        ret = [
            {"rid": row[0], "user_info": row[1], "hash_key": row[2], "balance": row[3], "enable": row[4]}
            for row in self.db.execute_R(statement)
        ]
        return ret

    def find_card(self, rid: str) -> list[dict]:
        statement = "SELECT `rid`, `user_info`, `hash_key`, `balance`, `enable` FROM `Card` WHERE `rid`=%s;"
        ret = [
            {"rid": row[0], "user_info": row[1], "hash_key": row[2], "balance": row[3], "enable": row[4]}
            for row in self.db.execute_R(statement, (rid,))
        ]
        return ret

    def find_card_balance(self, rid: str) -> list[int]:
        statement = "SELECT `balance` FROM `Card` WHERE `rid`=%s;"
        ret = [row[0] for row in self.db.execute_R(statement, (rid,))]
        return ret

    def add_card(self, rid: str, user_info: str, hash_key: str, balance: int, enable: bool):
        statement = """
            INSERT INTO `Card` (`rid`, `user_info`, `hash_key`, `balance`, `enable`)
            VALUES (%s, %s, %s, %s, %s);
        """.strip()
        int_enable = 1 if enable else 0
        args = (rid, user_info, hash_key, balance, int_enable)
        self.db.execute_CUD(statement, args)

    def delete_card(self, rid: str):
        statement = "DELETE FROM `Card` WHERE `rid`=%s;"
        self.db.execute_CUD(statement, (rid,))

    def find_all_transaction_records(self, rid: str) -> list[dict]:
        statement = """
            SELECT `TransactionRecord`.`rid`, `transaction_date`, `value`, `flow`, `balance_after_transaction`
            FROM `TransactionRecord`, `Card`
            WHERE `TransactionRecord`.`rid`=`Card`.`rid` AND `TransactionRecord`.`rid`=%s
            ORDER BY `transaction_date` DESC;
        """.strip()
        ret = [
            {
                "rid": row[0],
                "transaction_date": datetime.strftime(row[1], DATETIME_FORMAT),  # datetime object to str
                "value": row[2],
                "flow": row[3],
                "balance_after_transaction": row[4]
            }
            for row in self.db.execute_R(statement, (rid,))
        ]
        return ret

    def update_card_set_enable(self, rid: str, enable: bool):
        oper_card = self.find_card(rid)
        if not oper_card:
            return False
        oper_card = oper_card[0]
        new_enable_val = 1 if enable else 0
        if oper_card["enable"] == new_enable_val:
            return
        set_enable_stat = "UPDATE `Card` SET `enable`=%s WHERE `rid`=%s;"
        self.db.execute_CUD(set_enable_stat, (new_enable_val, rid))

    def update_card_transact(self, rid: str, value: int) -> bool:
        """
        Return True: transacted successfully.
        Return False: transacted failed.
        """
        # find and verify card in database
        oper_card = self.find_card(rid)
        if not oper_card:
            return False
        oper_card = oper_card[0]
        if not oper_card["enable"]:
            return False

        # calculate and check balance and value
        # value >= 0: refill, value < 0: debit
        transact_flow = "+" if value >= 0 else "-"
        transact_date = datetime.strftime(datetime.now(), DATETIME_FORMAT)
        temp_balance = oper_card["balance"] + value
        if temp_balance < MIN_BALANCE or temp_balance > MAX_BALANCE:
            return False

        # update balance of card
        update_card_stat = "UPDATE `Card` SET `balance`=%s WHERE `rid`=%s AND `enable`=1;"
        self.db.execute_CUD(update_card_stat, (temp_balance, rid))

        # insert new transaction record
        new_transaction_stat = """
            INSERT INTO `TransactionRecord` (`rid`, `transaction_date`, `value`, `flow`, `balance_after_transaction`)
            VALUES (%s, %s, %s, %s, %s);
        """
        self.db.execute_CUD(new_transaction_stat, (rid, transact_date, abs(value), transact_flow, temp_balance))
        return True


if __name__ == "__main__":
    db = DatabaseInterface()

    # info = "20020101" + "L123456789"
    # hkey, rid = generate_blake2_hash(info)
    # db.add_card(rid, info, hkey, 0, True)

    # ret = db.update_card_transact("10745c07b9d3d99f741077030768f927", 500)
    # print(ret)

    # records = db.find_all_transaction_records("10745c07b9d3d99f741077030768f927")
    # print(records[0])
