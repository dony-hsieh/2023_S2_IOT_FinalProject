# include <SPI.h>
# include <MFRC522.h>

# define SS_PIN  10
# define RST_PIN 9
# define BAUD    9600

# define RID_SIZE         16
# define DATA_BUFFER_SIZE 17

# define RFID_SECTOR            1
# define RFID_BLOCK_ADDR        4
# define RFID_TRAILERBLOCK_ADDR 7

# define WM_STD     0x00  // Work mode (Standby)
# define WM_REG     0x01  // Work mode (Register)
# define WM_CNL     0x02  // Work mode (Cancelation)
# define WM_TRN     0x03  // Work mode (Transaction)
# define RID_CARRY  0x0F  // RID data carried

/**
 * Communication data format (including command block and data block):
 *   [===CMD===][=========DATA=========]
 *    --1Byte--  -------16Bytes--------
 * 
 * Commands:
 *   0x00 ---- Standby mode
 *   0x01 ---- Register mode
 *   0x02 ---- Cancelation mode
 *   0x03 ---- Transaction mode
 *   0x0F ---- RID data carried
 */
 

/* ========================================================================================================= */
/* Variables */

MFRC522 mfrc522(SS_PIN, RST_PIN);
MFRC522::MIFARE_Key mifare_key;

byte SERIAL_RID_FLAG = 0x00;
byte RFID_RID_FLAG_MASK = 0x00;
byte WORK_MODE = WM_TRN;  // Default is standby mode

byte data_buffer[DATA_BUFFER_SIZE];
byte rid_from_serial[RID_SIZE] = {
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
};
byte rid_from_rfid[RID_SIZE + 2] = {
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00
};


/* ========================================================================================================= */
/* Functions */

void dump_byte_array(byte *buffer, byte bufferSize) {
    for (byte i = 0; i < bufferSize; i++) {
        Serial.print(buffer[i] < 0x10 ? " 0" : " ");
        Serial.print(buffer[i], HEX);
    }
    Serial.println();
}


/* ========================================================================================================= */
/* Arduino main */

void setup() {
  // init
    Serial.begin(BAUD);
    SPI.begin();
    mfrc522.PCD_Init();
  
    // Prepare key for authentication of RFID
    for (byte i = 0; i < 6; i++) {
        mifare_key.keyByte[i] = 0xFF;
    }
    
    delay(4);
}


void loop() {
  // clear all flags
    SERIAL_RID_FLAG = 0x00;
    RFID_RID_FLAG_MASK = 0x00;
  
    // Read serial
    if (Serial.available()) {
        Serial.readBytes(data_buffer, DATA_BUFFER_SIZE);
    
        // Parse command
        if (data_buffer[0] == WM_STD || data_buffer[0] == WM_REG || data_buffer[0] == WM_CNL || data_buffer[0] == WM_TRN) {
            // Switch WORK_MODE
            WORK_MODE = data_buffer[0];
        } else if (data_buffer[0] == 0x0F) {
            // Store rid
            for (size_t i = 1; i < 1 + RID_SIZE; i++) {
                rid_from_serial[i-1] = data_buffer[i];
            }

            // Set flag
            SERIAL_RID_FLAG = 0x01;
        }
    }
  
    // RFID read tag
    if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
        // Authenticate using key A
        MFRC522::StatusCode status;
        status = (MFRC522::StatusCode) mfrc522.PCD_Authenticate(
            MFRC522::PICC_CMD_MF_AUTH_KEY_A, RFID_TRAILERBLOCK_ADDR, &mifare_key, &(mfrc522.uid)
        );
        if (status == MFRC522::STATUS_OK) {
            // Authenticate success
            byte buf_size = sizeof(rid_from_rfid);
            status = (MFRC522::StatusCode) mfrc522.MIFARE_Read(RFID_BLOCK_ADDR, rid_from_rfid, &buf_size);
            if (status == MFRC522::STATUS_OK) {
                // Set flasg
                RFID_RID_FLAG_MASK = 0x01;
            }
        }
    }

    // Works of WORK_MODE
    switch (WORK_MODE) {
        case WM_REG:
            if (SERIAL_RID_FLAG == 0x01) {
                // Write rid_from_serial to RFID
                // TODO???
            }
            break;
            
        case WM_CNL:
        case WM_TRN:
            if (RFID_RID_FLAG_MASK == 0x01) {
                // Send rid_from_rfid to serial
                Serial.write(RID_CARRY);
                Serial.write(rid_from_rfid, RID_SIZE);
                Serial.write('\n'); 
                //Serial.print(RID_CARRY);
                //dump_byte_array(rid_from_rfid, RID_SIZE);
            }
            break;
            
        default:
            if (WORK_MODE != WM_STD) {
                WORK_MODE = WM_STD;
            }
            break;
    }

    // Halt PICC
    mfrc522.PICC_HaltA();
    // Stop encryption on PCD
    mfrc522.PCD_StopCrypto1();
    //delay(1000);
}
