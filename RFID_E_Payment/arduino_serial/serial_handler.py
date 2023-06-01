from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QThread, Signal
import serial
import time

from RFID_E_Payment.definitions import SERIAL_PORT, SERIAL_BAUD, SERIAL_COMMUNICATION_PACK_SIZE


class SerialThread(QThread):
    new_data_from_serial = Signal()

    def __init__(self):
        super(SerialThread, self).__init__()

        self.serial = serial.Serial()
        self.serial.port = SERIAL_PORT
        self.serial.baudrate = SERIAL_BAUD
        self.serial.timeout = 2

        self.running = False
        self.writing_flag = False
        self.reading_buffer = b""
        self.writing_buffer = b""

    def open_serial(self) -> bool:
        try:
            self.serial.close()
            self.serial.open()
            return True
        except serial.SerialException as e:
            print(e)
            return False

    def run(self):
        if not self.serial.is_open:
            print("Serial is not open")
            return
        self.running = True
        self.serial.flushInput()
        self.serial.flushOutput()
        while self.running:
            try:
                if self.writing_flag:
                    self.writing_flag = False
                    self.serial.write(self.writing_buffer)
                if self.serial.in_waiting:
                    raw_data = self.serial.read(SERIAL_COMMUNICATION_PACK_SIZE)
                    self.reading_buffer = raw_data
                    self.new_data_from_serial.emit()
            except serial.SerialException as e:
                print(e)
                self.stop()

    def stop(self):
        self.writing_flag = False
        self.running = False

    def set_writing_data(self, data: bytes):
        self.writing_buffer = data
        self.writing_flag = True

    def get_reading_data(self):
        return self.reading_buffer
