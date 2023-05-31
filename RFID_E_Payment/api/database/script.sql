USE `rfid_db`;

DROP TABLE `TransactionRecord`;
DROP TABLE `Card`;

CREATE TABLE `Card` (
    `rid`        VARCHAR(32)   NOT NULL,
    `user_info`  VARCHAR(28)   NOT NULL,
    `hash_key`   VARCHAR(32)   NOT NULL,
    `balance`    INTEGER       NOT NULL,
    `enable`     INTEGER       NOT NULL,
    `reg_date`   DATETIME      NOT NULL,
    PRIMARY KEY (`rid`),
    UNIQUE (`user_info`)
);

CREATE TABLE `TransactionRecord` (
    `rid`                        VARCHAR(32)  NOT NULL,
    `transaction_date`           DATETIME    NOT NULL,
    `value`                      INTEGER     NOT NULL,
    `flow`                       CHAR(1)     NOT NULL,
    `balance_after_transaction`  INTEGER     NOT NULL,
    PRIMARY KEY (`rid`, `transaction_date`),
    FOREIGN KEY (`rid`) REFERENCES `Card`(`rid`)
    ON DELETE CASCADE  ON UPDATE CASCADE
);