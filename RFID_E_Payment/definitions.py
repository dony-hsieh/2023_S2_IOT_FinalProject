# Balance
MIN_BALANCE = 0
MAX_BALANCE = 10000
MIN_TRANSACTION_VALUE = 1
MAX_TRANSACTION_VALUE = 9999

# Datetime format (Python to MySQL)
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Hash
HASH_COMPONENTS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# API Server
API_HOST = "127.0.0.1"
API_PORT = 8000
ROOT_URL = f"{API_HOST}:{API_PORT}/rfid-ticket-api"

# Serial
SERIAL_PORT = "COM4"
SERIAL_BAUD = 9600
SERIAL_COMMUNICATION_CMD_SIZE = 1
SERIAL_COMMUNICATION_CARRY_DATA_SIZE = 16
SERIAL_COMMUNICATION_PACK_SIZE = (   # 17 bytes
        SERIAL_COMMUNICATION_CMD_SIZE + SERIAL_COMMUNICATION_CARRY_DATA_SIZE
)
