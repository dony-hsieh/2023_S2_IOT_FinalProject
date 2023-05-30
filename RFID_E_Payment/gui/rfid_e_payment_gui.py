from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Qt

import sys

import mainwindow_ui_v2


class MainApplicationWindow(QMainWindow):
    def __init__(self):
        super(MainApplicationWindow, self).__init__()
        self.ui = mainwindow_ui_v2.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowState(Qt.WindowMaximized)


if __name__ == "__main__":
    gui_app = QApplication(sys.argv)
    main_window = MainApplicationWindow()
    main_window.show()
    sys.exit(gui_app.exec_())
