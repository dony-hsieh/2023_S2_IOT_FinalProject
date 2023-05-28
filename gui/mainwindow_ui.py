# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 541)
        MainWindow.setMinimumSize(QSize(800, 450))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"\u7d30\u660e\u9ad4")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.curModeLineEdit = QLineEdit(self.groupBox)
        self.curModeLineEdit.setObjectName(u"curModeLineEdit")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.curModeLineEdit.setFont(font1)
        self.curModeLineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.curModeLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.standbyModeBtn = QPushButton(self.groupBox)
        self.standbyModeBtn.setObjectName(u"standbyModeBtn")
        font2 = QFont()
        font2.setPointSize(15)
        self.standbyModeBtn.setFont(font2)

        self.horizontalLayout_2.addWidget(self.standbyModeBtn)

        self.regCardModeBtn = QPushButton(self.groupBox)
        self.regCardModeBtn.setObjectName(u"regCardModeBtn")
        self.regCardModeBtn.setFont(font2)

        self.horizontalLayout_2.addWidget(self.regCardModeBtn)

        self.cancelCardModeBtn = QPushButton(self.groupBox)
        self.cancelCardModeBtn.setObjectName(u"cancelCardModeBtn")
        self.cancelCardModeBtn.setFont(font2)

        self.horizontalLayout_2.addWidget(self.cancelCardModeBtn)

        self.refillModeBtn = QPushButton(self.groupBox)
        self.refillModeBtn.setObjectName(u"refillModeBtn")
        self.refillModeBtn.setFont(font2)

        self.horizontalLayout_2.addWidget(self.refillModeBtn)

        self.debitModeBtn = QPushButton(self.groupBox)
        self.debitModeBtn.setObjectName(u"debitModeBtn")
        self.debitModeBtn.setFont(font2)

        self.horizontalLayout_2.addWidget(self.debitModeBtn)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.personIdLineEdit = QLineEdit(self.groupBox)
        self.personIdLineEdit.setObjectName(u"personIdLineEdit")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.personIdLineEdit.setFont(font4)

        self.horizontalLayout_5.addWidget(self.personIdLineEdit)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.personBirthLineEdit = QLineEdit(self.groupBox)
        self.personBirthLineEdit.setObjectName(u"personBirthLineEdit")
        self.personBirthLineEdit.setFont(font4)

        self.horizontalLayout_4.addWidget(self.personBirthLineEdit)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.clearRegInfoBtn = QPushButton(self.groupBox)
        self.clearRegInfoBtn.setObjectName(u"clearRegInfoBtn")
        font5 = QFont()
        font5.setPointSize(13)
        self.clearRegInfoBtn.setFont(font5)

        self.horizontalLayout_6.addWidget(self.clearRegInfoBtn)

        self.regCardBtn = QPushButton(self.groupBox)
        self.regCardBtn.setObjectName(u"regCardBtn")
        self.regCardBtn.setFont(font5)

        self.horizontalLayout_6.addWidget(self.regCardBtn)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(2, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.readCardIdToCancelLineEdit = QLineEdit(self.groupBox)
        self.readCardIdToCancelLineEdit.setObjectName(u"readCardIdToCancelLineEdit")
        self.readCardIdToCancelLineEdit.setFont(font3)
        self.readCardIdToCancelLineEdit.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.readCardIdToCancelLineEdit)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 3)

        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_9)

        self.cardEnableStateToCancelLineEdit = QLineEdit(self.groupBox)
        self.cardEnableStateToCancelLineEdit.setObjectName(u"cardEnableStateToCancelLineEdit")
        self.cardEnableStateToCancelLineEdit.setFont(font3)
        self.cardEnableStateToCancelLineEdit.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.cardEnableStateToCancelLineEdit)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 3)

        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cancelCardBtn = QPushButton(self.groupBox)
        self.cancelCardBtn.setObjectName(u"cancelCardBtn")
        self.cancelCardBtn.setFont(font5)

        self.horizontalLayout_8.addWidget(self.cancelCardBtn)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.verticalLayout_7.setStretch(0, 2)
        self.verticalLayout_7.setStretch(1, 2)
        self.verticalLayout_7.setStretch(2, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_5)

        self.transactionModeLineEdit = QLineEdit(self.groupBox)
        self.transactionModeLineEdit.setObjectName(u"transactionModeLineEdit")
        self.transactionModeLineEdit.setFont(font3)
        self.transactionModeLineEdit.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.transactionModeLineEdit)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 3)

        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_6)

        self.readCardToTransactLineEdit = QLineEdit(self.groupBox)
        self.readCardToTransactLineEdit.setObjectName(u"readCardToTransactLineEdit")
        self.readCardToTransactLineEdit.setFont(font3)
        self.readCardToTransactLineEdit.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.readCardToTransactLineEdit)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 3)

        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_10)

        self.cardEnableStateToTransacLineEdit = QLineEdit(self.groupBox)
        self.cardEnableStateToTransacLineEdit.setObjectName(u"cardEnableStateToTransacLineEdit")
        self.cardEnableStateToTransacLineEdit.setFont(font3)
        self.cardEnableStateToTransacLineEdit.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.cardEnableStateToTransacLineEdit)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 3)

        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_7)

        self.cardBalanceLineEdit = QLineEdit(self.groupBox)
        self.cardBalanceLineEdit.setObjectName(u"cardBalanceLineEdit")
        self.cardBalanceLineEdit.setFont(font3)
        self.cardBalanceLineEdit.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.cardBalanceLineEdit)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 3)

        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.setTransactionValueLineEdit = QLineEdit(self.groupBox)
        self.setTransactionValueLineEdit.setObjectName(u"setTransactionValueLineEdit")
        font6 = QFont()
        font6.setPointSize(10)
        self.setTransactionValueLineEdit.setFont(font6)

        self.horizontalLayout_9.addWidget(self.setTransactionValueLineEdit)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 3)

        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 1)
        self.verticalLayout_8.setStretch(2, 1)
        self.verticalLayout_8.setStretch(3, 1)
        self.verticalLayout_8.setStretch(4, 1)

        self.verticalLayout_5.addLayout(self.verticalLayout_8)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.clearTransactionValueBtn = QPushButton(self.groupBox)
        self.clearTransactionValueBtn.setObjectName(u"clearTransactionValueBtn")
        self.clearTransactionValueBtn.setFont(font5)

        self.horizontalLayout_14.addWidget(self.clearTransactionValueBtn)

        self.transactionBtn = QPushButton(self.groupBox)
        self.transactionBtn.setObjectName(u"transactionBtn")
        self.transactionBtn.setFont(font5)

        self.horizontalLayout_14.addWidget(self.transactionBtn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.verticalLayout_5.setStretch(0, 4)
        self.verticalLayout_5.setStretch(1, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(4, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 7)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.rfidMonitorTextEdit = QPlainTextEdit(self.groupBox_2)
        self.rfidMonitorTextEdit.setObjectName(u"rfidMonitorTextEdit")
        self.rfidMonitorTextEdit.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.rfidMonitorTextEdit)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 2)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RFID", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"RFID Controller", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7576\u524d\u6a21\u5f0f:", None))
        self.standbyModeBtn.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u6a5f", None))
        self.regCardModeBtn.setText(QCoreApplication.translate("MainWindow", u"\u8a3b\u518a\u5361\u7247", None))
        self.cancelCardModeBtn.setText(QCoreApplication.translate("MainWindow", u"\u8a3b\u92b7\u5361\u7247", None))
        self.refillModeBtn.setText(QCoreApplication.translate("MainWindow", u"\u5132\u503c", None))
        self.debitModeBtn.setText(QCoreApplication.translate("MainWindow", u"\u6263\u6b3e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8eab\u5206\u8b49\u5b57\u865f(10\u78bc):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u751f\u5e74\u6708\u65e5(8\u78bc):", None))
        self.clearRegInfoBtn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u6b04\u4f4d", None))
        self.regCardBtn.setText(QCoreApplication.translate("MainWindow", u"\u8a18\u540d\u8a3b\u518a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8b80\u53d6\u5361\u7247\u8cc7\u8a0a:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5361\u7247\u72c0\u614b:", None))
        self.cancelCardBtn.setText(QCoreApplication.translate("MainWindow", u"\u8a3b\u92b7", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613\u6a21\u5f0f:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8b80\u53d6\u5361\u7247\u8cc7\u8a0a:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5361\u7247\u72c0\u614b:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5361\u7247\u9918\u984d:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8a2d\u5b9a\u4ea4\u6613\u91d1\u984d:", None))
        self.clearTransactionValueBtn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u4ea4\u6613\u91d1\u984d", None))
        self.transactionBtn.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"RFID Monitor", None))
    # retranslateUi
