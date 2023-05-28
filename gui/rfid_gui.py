from PySide2.QtWidgets import QApplication, QMainWindow
import sys

import mainwindow_ui


class MainApplicationWindow(QMainWindow):
    def __init__(self):
        super(MainApplicationWindow, self).__init__()
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    gui_app = QApplication(sys.argv)
    mainAppWindow = MainApplicationWindow()
    mainAppWindow.show()
    sys.exit(gui_app.exec_())
