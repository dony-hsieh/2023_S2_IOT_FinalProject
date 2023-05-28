from PySide2.QtCore import QThread
from typing import Callable
import serial

from RFID_E_Payment.definitions import SERIAL_PORT, SERIAL_BAUD


class TaskThread(QThread):
    def __init__(self, task: Callable):
        super(TaskThread, self).__init__()
        self.task = task
        self.args = ()

    def run(self):
        self.task(*self.args)

    def startTask(self, args: tuple = ()):
        self.args = args if isinstance(args, tuple) else ()
        self.start()

    def connectSignal(self, started_slot: Callable = None, finished_slot: Callable = None):
        if isinstance(started_slot, Callable):
            self.started.connect(started_slot)
        if isinstance(finished_slot, Callable):
            self.finished.connect(finished_slot)


class SerialHandler:
    def __init__(self):
        self.serial = None
        self.open_serial()

    def open_serial(self) -> bool:
        try:
            self.serial = serial.Serial(port=SERIAL_PORT, baudrate=SERIAL_BAUD, timeout=5)
            return True
        except serial.SerialException as e:
            print(e.args)
            return False


if __name__ == "__main__":
    serialHandler = SerialHandler()
