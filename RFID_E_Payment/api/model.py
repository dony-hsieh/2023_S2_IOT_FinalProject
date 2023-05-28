from pydantic import BaseModel


class Card(BaseModel):
    rid: str
    user_info: str
    hash_key: str
    balance: int
    enable: bool

    def to_dict(self) -> dict:
        return {
            "rid": self.rid,
            "user_info": self.user_info,
            "hash_key": self.hash_key,
            "balance": self.balance,
            "enable": self.enable
        }


class TransactionRecord(BaseModel):
    rid: str
    transaction_date: str
    value: int
    flow: str
    balance_after_transaction: int

    def to_dict(self) -> dict:
        return {
            "rid": self.rid,
            "transaction_date": self.transaction_date,
            "value": self.value,
            "flow": self.flow,
            "balance_after_transaction": self.balance_after_transaction
        }
