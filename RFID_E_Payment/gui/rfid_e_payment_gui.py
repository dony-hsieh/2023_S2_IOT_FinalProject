from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2.QtGui import QIntValidator, QCloseEvent

from enum import Enum
from datetime import datetime
import sys

from RFID_E_Payment.definitions import (
    MIN_TRANSACTION_VALUE, MAX_TRANSACTION_VALUE, SERIAL_COMMUNICATION_CARRY_DATA_SIZE
)
from RFID_E_Payment.api.database import database
from RFID_E_Payment.arduino_serial.serial_handler import SerialThread
import mainwindow_ui


class WorkMode(Enum):
    STD = "00"
    REG = "01"
    CNL = "02"
    TRN = "03"

    def mode_str(self):
        if self.value == "00":
            return "待機模式"
        if self.value == "01":
            return "註冊模式"
        if self.value == "02":
            return "註銷模式"
        if self.value == "03":
            return "交易模式"
        return "待機模式"


class MainApplicationWindow(QMainWindow):
    def __init__(self):
        super(MainApplicationWindow, self).__init__()
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = database.DatabaseInterface()
        self.rfid_serial_thread = SerialThread()

        self.rfid_serial_thread.new_data_from_serial.connect(self.parse_serial_reading_pack)
        self.rfid_serial_thread.open_serial()
        self.rfid_serial_thread.start()

        self.ui.trnValLineEdit.setValidator(QIntValidator(MIN_TRANSACTION_VALUE, MAX_TRANSACTION_VALUE))

        self.ui.reconnSerialBtn.clicked.connect(self.reconnect_serial)
        self.ui.stdModeBtn.clicked.connect(lambda _: self.on_mode_switch(WorkMode.STD))
        self.ui.trnModeBtn.clicked.connect(lambda _: self.on_mode_switch(WorkMode.TRN))
        self.ui.regModeBtn.clicked.connect(lambda _: self.on_mode_switch(WorkMode.REG))
        self.ui.cnlModeBtn.clicked.connect(lambda _: self.on_mode_switch(WorkMode.CNL))
        self.ui.clearReadRidBtn.clicked.connect(self.ui.readRidLineEdit.clear)
        self.ui.queryCardInfoBtn.clicked.connect(lambda _: self.query_card_info(True))
        self.ui.clearTrnValBtn.clicked.connect(self.ui.trnValLineEdit.clear)
        self.ui.execTrnBtn.clicked.connect(self.execute_transaction)
        self.ui.generateRidBtn.clicked.connect(self.generate_new_rid)
        self.ui.clearRegInfoBtn.clicked.connect(self.clear_register_info)
        self.ui.execRegBtn.clicked.connect(self.execute_register)
        self.ui.setEnableTrueBtn.clicked.connect(lambda _: self.set_card_enable(True))
        self.ui.setEnableFalseBtn.clicked.connect(lambda _: self.set_card_enable(False))
        self.ui.execCnlBtn.clicked.connect(self.execute_cancellation)

        self.rfid_curWorkMode = WorkMode.STD
        self.set_widgets_mode()

        # init the mode of rfid
        com_pack = (
            bytes.fromhex(self.rfid_curWorkMode.value) +
            bytes.fromhex("00" * SERIAL_COMMUNICATION_CARRY_DATA_SIZE)
        )
        self.rfid_serial_thread.set_writing_data(com_pack)

    def closeEvent(self, event: QCloseEvent):
        self.rfid_serial_thread.stop()

    def on_mode_switch(self, mode: WorkMode):
        if self.rfid_curWorkMode != mode:
            self.rfid_curWorkMode = mode
            self.set_widgets_mode()

            # send controlling command to serial
            com_pack = (
                bytes.fromhex(self.rfid_curWorkMode.value) +
                bytes.fromhex("00" * SERIAL_COMMUNICATION_CARRY_DATA_SIZE)
            )
            self.rfid_serial_thread.set_writing_data(com_pack)

    def set_widgets_mode(self):
        # show mode string
        self.ui.curModeLineEdit.setText("當前模式: " + self.rfid_curWorkMode.mode_str())

        # enable all mode controlling buttons
        self.ui.stdModeBtn.setEnabled(True)
        self.ui.trnModeBtn.setEnabled(True)
        self.ui.regModeBtn.setEnabled(True)
        self.ui.cnlModeBtn.setEnabled(True)

        # disable all other widgets
        self.ui.readRidLineEdit.setEnabled(False)
        self.ui.readEnableLineEdit.setEnabled(False)
        self.ui.readBalanceLineEdit.setEnabled(False)
        self.ui.clearReadRidBtn.setEnabled(False)
        self.ui.queryCardInfoBtn.setEnabled(False)

        self.ui.clearTrnValBtn.setEnabled(False)
        self.ui.execTrnBtn.setEnabled(False)
        self.ui.trnFlowComboBox.setEnabled(False)
        self.ui.trnValLineEdit.setEnabled(False)

        self.ui.birthLineEdit.setEnabled(False)
        self.ui.personIdLineEdit.setEnabled(False)
        self.ui.phoneNumLineEdit.setEnabled(False)
        self.ui.generatedRidLineEdit.setEnabled(False)
        self.ui.generateRidBtn.setEnabled(False)
        self.ui.clearRegInfoBtn.setEnabled(False)
        self.ui.execRegBtn.setEnabled(False)

        self.ui.setEnableFalseBtn.setEnabled(False)
        self.ui.setEnableTrueBtn.setEnabled(False)
        self.ui.execCnlBtn.setEnabled(False)

        # standby mode
        if self.rfid_curWorkMode == WorkMode.STD:
            self.ui.stdModeBtn.setEnabled(False)
            return

        # non-standby mode (read card info)
        self.ui.readRidLineEdit.setEnabled(True)
        self.ui.readEnableLineEdit.setEnabled(True)
        self.ui.readBalanceLineEdit.setEnabled(True)
        self.ui.clearReadRidBtn.setEnabled(True)
        self.ui.queryCardInfoBtn.setEnabled(True)

        # transaction mode
        if self.rfid_curWorkMode == WorkMode.TRN:
            self.ui.trnModeBtn.setEnabled(False)
            self.ui.clearTrnValBtn.setEnabled(True)
            self.ui.execTrnBtn.setEnabled(True)
            self.ui.trnFlowComboBox.setEnabled(True)
            self.ui.trnValLineEdit.setEnabled(True)
            self.ui.funcTabWidget.setCurrentIndex(0)
            return

        # register mode
        if self.rfid_curWorkMode == WorkMode.REG:
            self.ui.regModeBtn.setEnabled(False)
            self.ui.birthLineEdit.setEnabled(True)
            self.ui.personIdLineEdit.setEnabled(True)
            self.ui.phoneNumLineEdit.setEnabled(True)
            self.ui.generatedRidLineEdit.setEnabled(True)
            self.ui.generateRidBtn.setEnabled(True)
            self.ui.clearRegInfoBtn.setEnabled(True)
            self.ui.execRegBtn.setEnabled(True)
            self.ui.funcTabWidget.setCurrentIndex(1)
            return

        # cancel mode
        if self.rfid_curWorkMode == WorkMode.CNL:
            self.ui.cnlModeBtn.setEnabled(False)
            self.ui.setEnableFalseBtn.setEnabled(True)
            self.ui.setEnableTrueBtn.setEnabled(True)
            self.ui.execCnlBtn.setEnabled(True)
            self.ui.funcTabWidget.setCurrentIndex(2)

    def query_card_info(self, triggered_by_click: bool = False):
        flag = False
        read_rid = self.ui.readRidLineEdit.text().strip()
        ret = self.db.find_card(read_rid)
        enable_text = ""
        balance_text = ""
        if ret:
            flag = True
            enable_text = "啟用" if ret[0]["enable"] else "禁用"
            balance_text = str(ret[0]["balance"])
        self.ui.readEnableLineEdit.setText(enable_text)
        self.ui.readBalanceLineEdit.setText(balance_text)
        if triggered_by_click and not flag:
            QMessageBox.warning(
                self, "查詢卡片", "查無此卡片", QMessageBox.Ok
            )

    def execute_transaction(self):
        # check rid
        read_rid = self.ui.readRidLineEdit.text().strip()
        ret = self.db.find_card(read_rid)
        if not ret:
            QMessageBox.critical(
                self, "交易程序", "查無可進行交易的卡片", QMessageBox.Ok
            )
            return

        # check transaction flow and transaction value
        trn_flow = 1 if self.ui.trnFlowComboBox.currentIndex() == 0 else -1
        trn_val = self.ui.trnValLineEdit.text().strip()
        if not trn_val:
            QMessageBox.critical(
                self, "交易程序", "未輸入交易金額", QMessageBox.Ok
            )
            return
        trn_val = int(trn_val)
        if not trn_val or trn_val < MIN_TRANSACTION_VALUE or trn_val > MAX_TRANSACTION_VALUE:
            QMessageBox.critical(
                self, "交易程序", "交易金額非許可範圍", QMessageBox.Ok
            )
            return

        # execute transaction
        success = self.db.update_card_transact(read_rid, trn_flow * trn_val)
        if success:
            self.query_card_info()
            self.ui.trnFlowComboBox.setCurrentIndex(0)
            self.ui.trnValLineEdit.clear()
            QMessageBox.information(
                self, "交易程序", "交易結果: 成功", QMessageBox.Ok
            )
            return
        QMessageBox.critical(
            self, "交易程序", "交易結果: 失敗", QMessageBox.Ok
        )

    def generate_new_rid(self):
        # check person info
        person_birth = self.ui.birthLineEdit.text().replace(" ", "")
        person_id = self.ui.personIdLineEdit.text().replace(" ", "")
        person_phone_number = self.ui.phoneNumLineEdit.text().replace(" ", "")
        if len(person_birth) != 8 or len(person_id) != 10 or len(person_phone_number) != 10:
            self.ui.generatedRidLineEdit.clear()
            QMessageBox.critical(
                self, "生成卡片辨識ID", "生成失敗，請檢查註冊資料欄位是否填寫正確", QMessageBox.Ok
            )
            return

        # generate hash key and rid
        hkey, rid = database.generate_blake2_hash(person_birth + person_id + person_phone_number)
        self.ui.generatedRidLineEdit.setText(f"{rid}:{hkey}")

    def clear_register_info(self):
        self.ui.birthLineEdit.clear()
        self.ui.personIdLineEdit.clear()
        self.ui.phoneNumLineEdit.clear()
        self.ui.generatedRidLineEdit.clear()

    def execute_register(self):
        # check person info
        person_birth = self.ui.birthLineEdit.text().replace(" ", "")
        person_id = self.ui.personIdLineEdit.text().replace(" ", "")
        person_phone_number = self.ui.phoneNumLineEdit.text().replace(" ", "")
        if len(person_birth) != 8 or len(person_id) != 10 or len(person_phone_number) != 10:
            self.ui.generatedRidLineEdit.clear()
            QMessageBox.critical(
                self, "註冊程序", "註冊資料不完整", QMessageBox.Ok
            )
            return

        # check generated rid
        gen_rid = self.ui.generatedRidLineEdit.text().split(":")
        if len(gen_rid) != 2:
            self.ui.generatedRidLineEdit.clear()
            QMessageBox.critical(
                self, "註冊程序", "生成卡片ID格式錯誤", QMessageBox.Ok
            )
            return
        rid, hkey = gen_rid
        user_info = person_birth + person_id + person_phone_number

        # check if register data existed
        existed = self.db.check_registered_card_existed(rid, user_info)
        if existed:
            QMessageBox.critical(
                self, "註冊程序", "註冊資料已被使用", QMessageBox.Ok
            )
            return

        # send to serial, then insert to db
        com_pack = (
            bytes.fromhex("0f") +
            bytes.fromhex(rid)
        )
        self.rfid_serial_thread.set_writing_data(com_pack)
        success = self.db.add_card(rid, user_info, hkey, 0, True, datetime.now())
        if success:
            QMessageBox.information(
                self, "註冊程序", "已建立註冊資訊，請感應卡片來寫入ID", QMessageBox.Ok
            )

    def set_card_enable(self, set_enable: bool):
        read_rid = self.ui.readRidLineEdit.text().strip()
        ret = self.db.find_card(read_rid)
        if not ret:
            QMessageBox.critical(
                self, "設置卡片", "查無可設置的卡片", QMessageBox.Ok
            )
            return
        original_enable = True if ret[0]["enable"] > 0 else False
        if original_enable != set_enable:
            success = self.db.update_card_set_enable(read_rid, set_enable)
            self.query_card_info()
            if success:
                QMessageBox.information(
                    self, "設置卡片", "設置結果: 成功", QMessageBox.Ok
                )
                return
            QMessageBox.critical(
                self, "設置卡片", "設置結果: 失敗", QMessageBox.Ok
            )

    def execute_cancellation(self):
        read_rid = self.ui.readRidLineEdit.text().strip()
        ret = self.db.find_card(read_rid)
        if not ret:
            QMessageBox.critical(
                self, "註銷程序", "查無可進行註銷的卡片", QMessageBox.Ok
            )
            return
        confirm_to_cancel = QMessageBox.warning(
            self, "註銷卡片", f"確定要註銷卡片\nID=\"{read_rid}\"", QMessageBox.No | QMessageBox.Yes, QMessageBox.No
        )
        if confirm_to_cancel == QMessageBox.Yes:
            self.db.delete_card(read_rid)
            self.ui.readRidLineEdit.clear()
            self.ui.readEnableLineEdit.clear()
            self.ui.readBalanceLineEdit.clear()

    def reconnect_serial(self):
        self.rfid_serial_thread.stop()
        success = self.rfid_serial_thread.open_serial()
        if success:
            self.rfid_serial_thread.start()

    def parse_serial_reading_pack(self):
        raw_data = self.rfid_serial_thread.get_reading_data().hex()
        cmd = raw_data[0:2]
        carried_data = raw_data[2:]
        if cmd == "0f":
            self.ui.readRidLineEdit.setText(carried_data)
            self.query_card_info()
        elif cmd == "10":
            print(carried_data)


if __name__ == "__main__":
    gui_app = QApplication(sys.argv)
    main_window = MainApplicationWindow()
    main_window.show()
    sys.exit(gui_app.exec_())
