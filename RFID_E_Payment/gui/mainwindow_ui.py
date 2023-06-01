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
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.reconnSerialBtn = QPushButton(self.centralwidget)
        self.reconnSerialBtn.setObjectName(u"reconnSerialBtn")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.reconnSerialBtn.setFont(font)

        self.verticalLayout_6.addWidget(self.reconnSerialBtn)

        self.curModeLineEdit = QLineEdit(self.centralwidget)
        self.curModeLineEdit.setObjectName(u"curModeLineEdit")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.curModeLineEdit.setFont(font1)
        self.curModeLineEdit.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.curModeLineEdit)

        self.verticalLayout_6.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stdModeBtn = QPushButton(self.centralwidget)
        self.stdModeBtn.setObjectName(u"stdModeBtn")
        self.stdModeBtn.setFont(font)

        self.verticalLayout_5.addWidget(self.stdModeBtn)

        self.trnModeBtn = QPushButton(self.centralwidget)
        self.trnModeBtn.setObjectName(u"trnModeBtn")
        self.trnModeBtn.setFont(font)

        self.verticalLayout_5.addWidget(self.trnModeBtn)

        self.regModeBtn = QPushButton(self.centralwidget)
        self.regModeBtn.setObjectName(u"regModeBtn")
        self.regModeBtn.setFont(font)

        self.verticalLayout_5.addWidget(self.regModeBtn)

        self.cnlModeBtn = QPushButton(self.centralwidget)
        self.cnlModeBtn.setObjectName(u"cnlModeBtn")
        self.cnlModeBtn.setFont(font)

        self.verticalLayout_5.addWidget(self.cnlModeBtn)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(3, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 5)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.groupBox.setFont(font2)
        self.groupBox.setFlat(False)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.readRidLineEdit = QLineEdit(self.groupBox)
        self.readRidLineEdit.setObjectName(u"readRidLineEdit")
        self.readRidLineEdit.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.readRidLineEdit)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.readEnableLineEdit = QLineEdit(self.groupBox)
        self.readEnableLineEdit.setObjectName(u"readEnableLineEdit")
        self.readEnableLineEdit.setFont(font)
        self.readEnableLineEdit.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.readEnableLineEdit)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.readBalanceLineEdit = QLineEdit(self.groupBox)
        self.readBalanceLineEdit.setObjectName(u"readBalanceLineEdit")
        self.readBalanceLineEdit.setFont(font)
        self.readBalanceLineEdit.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.readBalanceLineEdit)


        self.verticalLayout_8.addLayout(self.formLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.clearReadRidBtn = QPushButton(self.groupBox)
        self.clearReadRidBtn.setObjectName(u"clearReadRidBtn")
        self.clearReadRidBtn.setFont(font)

        self.horizontalLayout_3.addWidget(self.clearReadRidBtn)

        self.queryCardInfoBtn = QPushButton(self.groupBox)
        self.queryCardInfoBtn.setObjectName(u"queryCardInfoBtn")
        self.queryCardInfoBtn.setFont(font)

        self.horizontalLayout_3.addWidget(self.queryCardInfoBtn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.funcTabWidget = QTabWidget(self.centralwidget)
        self.funcTabWidget.setObjectName(u"funcTabWidget")
        self.funcTabWidget.setTabPosition(QTabWidget.North)
        self.funcTabWidget.setTabShape(QTabWidget.Rounded)
        self.funcTabWidget.setDocumentMode(False)
        self.trnTab = QWidget()
        self.trnTab.setObjectName(u"trnTab")
        self.verticalLayout_10 = QVBoxLayout(self.trnTab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.trnTab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.trnFlowComboBox = QComboBox(self.trnTab)
        self.trnFlowComboBox.addItem("")
        self.trnFlowComboBox.addItem("")
        self.trnFlowComboBox.setObjectName(u"trnFlowComboBox")
        self.trnFlowComboBox.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.trnFlowComboBox)

        self.label_6 = QLabel(self.trnTab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.trnValLineEdit = QLineEdit(self.trnTab)
        self.trnValLineEdit.setObjectName(u"trnValLineEdit")
        self.trnValLineEdit.setFont(font)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.trnValLineEdit)


        self.verticalLayout_10.addLayout(self.formLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.clearTrnValBtn = QPushButton(self.trnTab)
        self.clearTrnValBtn.setObjectName(u"clearTrnValBtn")
        self.clearTrnValBtn.setFont(font)

        self.horizontalLayout_4.addWidget(self.clearTrnValBtn)

        self.execTrnBtn = QPushButton(self.trnTab)
        self.execTrnBtn.setObjectName(u"execTrnBtn")
        self.execTrnBtn.setFont(font)

        self.horizontalLayout_4.addWidget(self.execTrnBtn)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 1)
        self.funcTabWidget.addTab(self.trnTab, "")
        self.regTab = QWidget()
        self.regTab.setObjectName(u"regTab")
        self.verticalLayout_9 = QVBoxLayout(self.regTab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_7 = QLabel(self.regTab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.birthLineEdit = QLineEdit(self.regTab)
        self.birthLineEdit.setObjectName(u"birthLineEdit")
        self.birthLineEdit.setFont(font)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.birthLineEdit)

        self.label_8 = QLabel(self.regTab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.personIdLineEdit = QLineEdit(self.regTab)
        self.personIdLineEdit.setObjectName(u"personIdLineEdit")
        self.personIdLineEdit.setFont(font)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.personIdLineEdit)

        self.label_9 = QLabel(self.regTab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.phoneNumLineEdit = QLineEdit(self.regTab)
        self.phoneNumLineEdit.setObjectName(u"phoneNumLineEdit")
        self.phoneNumLineEdit.setFont(font)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.phoneNumLineEdit)

        self.label_10 = QLabel(self.regTab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.generatedRidLineEdit = QLineEdit(self.regTab)
        self.generatedRidLineEdit.setObjectName(u"generatedRidLineEdit")
        self.generatedRidLineEdit.setFont(font)
        self.generatedRidLineEdit.setReadOnly(True)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.generatedRidLineEdit)

        self.generateRidBtn = QPushButton(self.regTab)
        self.generateRidBtn.setObjectName(u"generateRidBtn")
        self.generateRidBtn.setFont(font)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.generateRidBtn)


        self.verticalLayout_9.addLayout(self.formLayout_3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.clearRegInfoBtn = QPushButton(self.regTab)
        self.clearRegInfoBtn.setObjectName(u"clearRegInfoBtn")
        self.clearRegInfoBtn.setFont(font)

        self.horizontalLayout_5.addWidget(self.clearRegInfoBtn)

        self.execRegBtn = QPushButton(self.regTab)
        self.execRegBtn.setObjectName(u"execRegBtn")
        self.execRegBtn.setFont(font)

        self.horizontalLayout_5.addWidget(self.execRegBtn)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.verticalLayout_11.setStretch(0, 1)

        self.verticalLayout_9.addLayout(self.verticalLayout_11)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 1)
        self.funcTabWidget.addTab(self.regTab, "")
        self.cnlTab = QWidget()
        self.cnlTab.setObjectName(u"cnlTab")
        self.verticalLayout_12 = QVBoxLayout(self.cnlTab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.setEnableFalseBtn = QPushButton(self.cnlTab)
        self.setEnableFalseBtn.setObjectName(u"setEnableFalseBtn")
        self.setEnableFalseBtn.setFont(font)

        self.horizontalLayout_6.addWidget(self.setEnableFalseBtn)

        self.setEnableTrueBtn = QPushButton(self.cnlTab)
        self.setEnableTrueBtn.setObjectName(u"setEnableTrueBtn")
        self.setEnableTrueBtn.setFont(font)

        self.horizontalLayout_6.addWidget(self.setEnableTrueBtn)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_13.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.execCnlBtn = QPushButton(self.cnlTab)
        self.execCnlBtn.setObjectName(u"execCnlBtn")
        self.execCnlBtn.setFont(font)

        self.horizontalLayout_7.addWidget(self.execCnlBtn)


        self.verticalLayout_13.addLayout(self.horizontalLayout_7)

        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 1)

        self.verticalLayout_12.addLayout(self.verticalLayout_13)

        self.funcTabWidget.addTab(self.cnlTab, "")

        self.verticalLayout_7.addWidget(self.funcTabWidget)


        self.verticalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.monitorTextEdit = QPlainTextEdit(self.centralwidget)
        self.monitorTextEdit.setObjectName(u"monitorTextEdit")
        self.monitorTextEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.monitorTextEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.funcTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RFID E-Payment", None))
        self.reconnSerialBtn.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u9023\u63a5 Serial", None))
        self.stdModeBtn.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u6a5f\u6a21\u5f0f", None))
        self.trnModeBtn.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613\u6a21\u5f0f", None))
        self.regModeBtn.setText(QCoreApplication.translate("MainWindow", u"\u8a3b\u518a\u6a21\u5f0f", None))
        self.cnlModeBtn.setText(QCoreApplication.translate("MainWindow", u"\u8a3b\u92b7\u6a21\u5f0f", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5361\u7247\u8cc7\u8a0a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5361\u7247\u8b58\u5225 ID :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5361\u7247\u72c0\u614b :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5361\u7247\u9918\u984d :", None))
        self.clearReadRidBtn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5361\u7247\u8b58\u5225 ID \u6b04\u4f4d", None))
        self.queryCardInfoBtn.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u67e5\u8a62\u5361\u7247\u8cc7\u6599", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613\u985e\u578b :", None))
        self.trnFlowComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5132\u503c", None))
        self.trnFlowComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6263\u6b3e", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613\u91d1\u984d :", None))
        self.trnValLineEdit.setText("")
        self.trnValLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1-9999", None))
        self.clearTrnValBtn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u4ea4\u6613\u91d1\u984d", None))
        self.execTrnBtn.setText(QCoreApplication.translate("MainWindow", u"\u57f7\u884c\u4ea4\u6613\u7a0b\u5e8f", None))
        self.funcTabWidget.setTabText(self.funcTabWidget.indexOf(self.trnTab), QCoreApplication.translate("MainWindow", u"\u4ea4\u6613", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u751f\u5e74\u6708\u65e5 (8\u4f4d) :", None))
        self.birthLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"YYYYMMDD", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8eab\u5206\u8b49\u5b57\u865f (10\u4f4d) :", None))
        self.personIdLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A123456789", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u624b\u6a5f\u865f\u78bc (10\u4f4d) :", None))
        self.phoneNumLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0912345678", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5361\u7247\u8b58\u5225 ID :", None))
        self.generatedRidLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9ede\u64ca\u4e0b\u65b9\u6309\u9215\u751f\u6210\u8b58\u5225 ID", None))
        self.generateRidBtn.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u5361\u7247\u8b58\u5225 ID", None))
        self.clearRegInfoBtn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u6240\u6709\u6b04\u4f4d", None))
        self.execRegBtn.setText(QCoreApplication.translate("MainWindow", u"\u57f7\u884c\u8a3b\u518a\u7a0b\u5e8f", None))
        self.funcTabWidget.setTabText(self.funcTabWidget.indexOf(self.regTab), QCoreApplication.translate("MainWindow", u"\u8a3b\u518a", None))
        self.setEnableFalseBtn.setText(QCoreApplication.translate("MainWindow", u"\u8a2d\u7f6e\u5361\u7247\u70ba\u7981\u7528", None))
        self.setEnableTrueBtn.setText(QCoreApplication.translate("MainWindow", u"\u8a2d\u7f6e\u5361\u7247\u70ba\u555f\u7528", None))
        self.execCnlBtn.setText(QCoreApplication.translate("MainWindow", u"\u57f7\u884c\u8a3b\u92b7\u7a0b\u5e8f", None))
        self.funcTabWidget.setTabText(self.funcTabWidget.indexOf(self.cnlTab), QCoreApplication.translate("MainWindow", u"\u8a3b\u92b7", None))
    # retranslateUi

