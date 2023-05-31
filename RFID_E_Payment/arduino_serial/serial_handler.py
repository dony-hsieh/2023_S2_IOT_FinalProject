from PySide2.QtCore import QThread
from typing import Callable
import serial
import threading
import time

from RFID_E_Payment.definitions import SERIAL_PORT, SERIAL_BAUD, SERIAL_COMMUNICATION_DATA_SIZE

# TODO


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
        self.serial = serial.Serial()
        self.serial.port = SERIAL_PORT
        self.serial.baudrate = SERIAL_BAUD

        self.reading_thread_run = True
        self.writing_thread_run = True

        self.reading_task = threading.Thread(target=self.reading_from_serial, daemon=True)

        self.open_serial()
        self.reading_task.start()

    def open_serial(self):
        try:
            self.serial.open()
        except serial.SerialException as e:
            print(e)

    def stop_all_threads(self):
        self.reading_thread_run = False
        self.writing_thread_run = False

    def start_all_threads(self):
        self.reading_task.start()

    def reading_from_serial(self):
        while self.reading_thread_run:
            if self.serial.in_waiting:
                read_data = self.serial.read(SERIAL_COMMUNICATION_DATA_SIZE)
                print(len(read_data), read_data.hex())

    def writing_to_serial(self):
        while self.writing_thread_run:
            pass


if __name__ == "__main__":
    serialHandler = SerialHandler()
    time.sleep(5)
    serialHandler.stop_all_threads()
