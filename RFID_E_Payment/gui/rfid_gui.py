from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Qt
from PySide2.QtGui import QIntValidator

from enum import Enum
from datetime import datetime
import sys

import mainwindow_ui
from RFID_E_Payment.api.database import database
from RFID_E_Payment.definitions import DATETIME_FORMAT


class RFIDModes(Enum):
    """
    RFID modes => {STB: Standby, REG: Register_card, CNL: Cancel_card, RFL: Refill, DBT: Debit}
    """
    STB = 0
    REG = 1
    CNL = 2
    RFL = 3
    DBT = 4

    def mode_string(self) -> str:
        if self.value == 0:
            return "待機模式"
        if self.value == 1:
            return "註冊模式"
        if self.value == 2:
            return "註銷模式"
        if self.value == 3:
            return "儲值模式"
        if self.value == 4:
            return "扣款模式"
        return ""


class MainApplicationWindow(QMainWindow):
    def __init__(self):
        super(MainApplicationWindow, self).__init__()
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowState(Qt.WindowMaximized)

        # ==== Tools ====
        self.db = database.DatabaseInterface()

        # ==== Mode switcher buttons ====
        self.ui.standbyModeBtn.clicked.connect(lambda _: self.on_mode_switch(RFIDModes.STB))
        self.ui.regCardModeBtn.clicked.connect(lambda _: self.on_mode_switch(RFIDModes.REG))
        self.ui.cancelCardModeBtn.clicked.connect(lambda _: self.on_mode_switch(RFIDModes.CNL))
        self.ui.refillModeBtn.clicked.connect(lambda _: self.on_mode_switch(RFIDModes.RFL))
        self.ui.debitModeBtn.clicked.connect(lambda _: self.on_mode_switch(RFIDModes.DBT))

        # ==== Register card buttons ====
        self.ui.clearRegInfoBtn.clicked.connect(self.clear_reg_info)
        self.ui.regCardBtn.clicked.connect(self.register_card_with_person_info)

        # ==== Cancel card buttons ====
        self.ui.cancelCardBtn.clicked.connect(self.cancel_card)

        # ==== Transaction buttons ====
        self.ui.clearTransactionValueBtn.clicked.connect(self.clear_transaction_value)
        self.ui.transactionBtn.clicked.connect(self.handle_transaction)

        # ==== RFID system variables ====
        self.rfid_curMode = RFIDModes.STB
        self.rfid_curReadRid = ""
        self.rfid_curReadBalance = -1  # 讀到rid的時候會立刻同步更新balance
        self.rfid_curReadEnable = False  # 讀到rid的時候會立刻同步更新balance
        self.ui.curModeLineEdit.setText(self.rfid_curMode.mode_string())

        # ==== Set widget's initial setting ====
        self.set_widget_by_mode()
        self.display_read_card_info()
        self.ui.personIdLineEdit.setPlaceholderText("A123456789")
        self.ui.personBirthLineEdit.setPlaceholderText("YYYYMMDD")
        self.ui.setTransactionValueLineEdit.setPlaceholderText("0-9999")
        self.ui.setTransactionValueLineEdit.setValidator(QIntValidator(0, 9999))

    def on_mode_switch(self, mode: RFIDModes):
        if mode == RFIDModes.STB:
            self.rfid_curMode = RFIDModes.STB
        elif mode == RFIDModes.REG:
            self.rfid_curMode = RFIDModes.REG
        elif mode == RFIDModes.CNL:
            self.rfid_curMode = RFIDModes.CNL
        elif mode == RFIDModes.RFL:
            self.rfid_curMode = RFIDModes.RFL
        elif mode == RFIDModes.DBT:
            self.rfid_curMode = RFIDModes.DBT
        self.ui.curModeLineEdit.setText(self.rfid_curMode.mode_string())
        self.set_widget_by_mode()

    def set_widget_by_mode(self):
        self.ui.standbyModeBtn.setEnabled(True)
        self.ui.regCardModeBtn.setEnabled(True)
        self.ui.cancelCardModeBtn.setEnabled(True)
        self.ui.refillModeBtn.setEnabled(True)
        self.ui.debitModeBtn.setEnabled(True)

        self.ui.personIdLineEdit.setEnabled(False)
        self.ui.personBirthLineEdit.setEnabled(False)
        self.ui.clearRegInfoBtn.setEnabled(False)
        self.ui.regCardBtn.setEnabled(False)

        self.ui.readCardIdToCancelLineEdit.setEnabled(False)
        self.ui.cardEnableStateToCancelLineEdit.setEnabled(False)
        self.ui.cancelCardBtn.setEnabled(False)

        self.ui.transactionModeLineEdit.setEnabled(False)
        self.ui.readCardToTransactLineEdit.setEnabled(False)
        self.ui.cardBalanceLineEdit.setEnabled(False)
        self.ui.setTransactionValueLineEdit.setEnabled(False)
        self.ui.clearTransactionValueBtn.setEnabled(False)
        self.ui.transactionBtn.setEnabled(False)
        self.ui.cardEnableStateToTransacLineEdit.setEnabled(False)

        flag = False

        if self.rfid_curMode == RFIDModes.STB:
            self.ui.standbyModeBtn.setEnabled(False)
        elif self.rfid_curMode == RFIDModes.REG:
            self.ui.regCardModeBtn.setEnabled(False)
            self.ui.personIdLineEdit.setEnabled(True)
            self.ui.personBirthLineEdit.setEnabled(True)
            self.ui.clearRegInfoBtn.setEnabled(True)
            self.ui.regCardBtn.setEnabled(True)
        elif self.rfid_curMode == RFIDModes.CNL:
            self.ui.cancelCardModeBtn.setEnabled(False)
            self.ui.readCardIdToCancelLineEdit.setEnabled(True)
            self.ui.cardEnableStateToCancelLineEdit.setEnabled(True)
            self.ui.cancelCardBtn.setEnabled(True)
        elif self.rfid_curMode == RFIDModes.RFL:
            self.ui.refillModeBtn.setEnabled(False)
            flag = True
        elif self.rfid_curMode == RFIDModes.DBT:
            self.ui.debitModeBtn.setEnabled(False)
            flag = True

        if flag:
            self.ui.transactionModeLineEdit.setEnabled(True)
            self.ui.readCardToTransactLineEdit.setEnabled(True)
            self.ui.cardBalanceLineEdit.setEnabled(True)
            self.ui.setTransactionValueLineEdit.setEnabled(True)
            self.ui.clearTransactionValueBtn.setEnabled(True)
            self.ui.transactionBtn.setEnabled(True)
            self.ui.transactionModeLineEdit.setText(self.rfid_curMode.mode_string())
            self.ui.cardEnableStateToTransacLineEdit.setEnabled(True)

    def clear_reg_info(self):
        self.ui.personIdLineEdit.clear()
        self.ui.personBirthLineEdit.clear()

    def clear_transaction_value(self):
        self.ui.setTransactionValueLineEdit.clear()

    # def query_card_balance(self):
    #     if not self.rfid_curReadRid:
    #         self.ui.cardBalanceLineEdit.setText("Not Found")
    #         return
    #     balance = self.db.find_card_balance(self.rfid_curReadRid)
    #     if not balance:
    #         self.ui.cardBalanceLineEdit.setText("Not Found")
    #         return
    #     self.ui.cardBalanceLineEdit.setText(str(balance[0]))

    def rfid_monitor_add_log(self, log_cls: str, log_text: str):
        log_time = datetime.strftime(datetime.now(), DATETIME_FORMAT)
        log_msg = f"<{log_time}> [{log_cls}] {log_text}"
        self.ui.rfidMonitorTextEdit.appendPlainText(log_msg)

    def display_read_card_info(self):
        # 在每次有接收到card資訊並更新時呼叫此方法更新GUI View
        read_rid = "Not Found" if not self.rfid_curReadRid else self.rfid_curReadRid
        read_enable = "Disabled" if not self.rfid_curReadEnable else "Enabled"
        read_balance = "Not Found" if self.rfid_curReadBalance < 0 else str(self.rfid_curReadBalance)
        self.ui.readCardIdToCancelLineEdit.setText(read_rid)
        self.ui.readCardToTransactLineEdit.setText(read_rid)
        self.ui.cardEnableStateToCancelLineEdit.setText(read_enable)
        self.ui.cardEnableStateToTransacLineEdit.setText(read_enable)
        self.ui.cardBalanceLineEdit.setText(read_balance)

    def register_card_with_person_info(self):
        person_id = self.ui.personIdLineEdit.text().strip()
        person_birth = self.ui.personBirthLineEdit.text().strip()
        if not person_id or not person_birth:
            return
        info = person_birth + person_id
        new_hkey, new_rid = database.generate_blake2_hash(info)
        self.ui.personIdLineEdit.clear()
        self.ui.personBirthLineEdit.clear()
        self.rfid_monitor_add_log(
            "GUI", f"New card info generated (rid=\"{new_rid}\" with key=\"{new_hkey}\")"
        )
        # insert new card
        # self.db.add_card(new_rid, info, new_hkey, 0, True)
        # TODO: send rid to RFID

    def cancel_card(self):
        # 先只抹除資料庫，不管RFID裡面的rid
        if not self.rfid_curReadRid:
            return
        card = self.db.find_card(self.rfid_curReadRid)
        if len(card) == 1:
            card = card[0]
            self.db.delete_card(card["rid"])
            self.rfid_monitor_add_log("GUI", f"One card (rid={card['rid']}) has been canceled")

    def handle_transaction(self):
        if not self.rfid_curReadRid or not self.rfid_curReadEnable or self.rfid_curReadBalance < 0:
            return
        rid = self.rfid_curReadRid
        transaction_val = self.ui.setTransactionValueLineEdit.text().strip()
        if not transaction_val:
            return
        transaction_val = abs(int(transaction_val))
        if self.rfid_curMode == RFIDModes.DBT:
            transaction_val *= -1
        success = self.db.update_card_transact(rid, transaction_val)
        if success:
            self.rfid_monitor_add_log(
                "GUI", f"A transaction executed successfully on (rid=\"{rid}\", value=\"{transaction_val}\")"
            )
            return
        self.rfid_monitor_add_log("GUI", f"A transaction executed failed on (rid=\"{rid}\", value=\"{transaction_val}\")")



if __name__ == "__main__":
    gui_app = QApplication(sys.argv)
    mainAppWindow = MainApplicationWindow()
    mainAppWindow.show()
    sys.exit(gui_app.exec_())
