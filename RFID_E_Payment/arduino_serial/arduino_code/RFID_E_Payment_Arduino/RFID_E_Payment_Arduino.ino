# include <SPI.h>
# include <MFRC522.h>

# define SS_PIN  10
# define RST_PIN 9
# define BAUD    9600

# define LED_WM_PIN0           6
# define LED_WM_PIN1           7
# define LED_RID_WRITEABLE_PIN 8

# define RID_SIZE         16
# define DATA_BUFFER_SIZE 17

# define RFID_SECTOR            1
# define RFID_BLOCK_ADDR        4
# define RFID_TRAILERBLOCK_ADDR 7

# define WM_STD     0x00  // Work mode (Standby)
# define WM_REG     0x01  // Work mode (Register)
# define WM_CNL     0x02  // Work mode (Cancellation)
# define WM_TRN     0x03  // Work mode (Transaction)
# define RID_CARRY  0x0F  // RID data carried
# define DEBUG_MSG  0x10  // Likit debug message

/**
 * PIN map (left to right):
 *   [RC522]    [Linkit]
 *     SDA        P10
 *     SCK        P13
 *     MOSI       P11
 *     MISO       P12
 *     GND        GND
 *     3v3        3V3
 */

/**
 * Communication data format (including command block and data block):
 *   [===CMD===][=========DATA=========]
 *    --1Byte--  -------16Bytes--------
 * 
 * Commands:
 *   0x00 ---- Standby mode (no data carried)
 *   0x01 ---- Register mode (no data carried)
 *   0x02 ---- Cancelation mode (no data carried)
 *   0x03 ---- Transaction mode (no data carried)
 *   0x0F ---- RID data carried (data carried)
 *   0x10 ---- Likit debug message (data carried)
 * 
 * # Debug message carried data:
 *   {FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00} ---- RFID key authentication failed
 *   {FE 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00} ---- RFID read rid failed
 *   {FD 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00} ---- RFID write rid successfully
 *   {FC 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00} ---- RFID write rid failed
 */
 

/* ========================================================================================================= */
/* Variables */

MFRC522 mfrc522(SS_PIN, RST_PIN);
MFRC522::MIFARE_Key mifare_key;

// Flags
bool RFID_RID_READY_FLAG = false;
bool NEW_CARD_READY_FLAG = false;
bool NEW_WRITABLE_RID_FLAG = false;

// State
byte WORK_MODE = WM_STD;  // Default is standby mode
MFRC522::StatusCode mfrc522_status;

// Buffers
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

void set_LED_WM_PIN(byte wm) {
    digitalWrite(LED_WM_PIN0, LOW);
    digitalWrite(LED_WM_PIN1, LOW);
    if (wm == WM_REG) {
        digitalWrite(LED_WM_PIN0, HIGH);
    } else if (wm == WM_CNL) {
        digitalWrite(LED_WM_PIN1, HIGH);
    } else if (wm == WM_TRN) {
        digitalWrite(LED_WM_PIN0, HIGH);
        digitalWrite(LED_WM_PIN1, HIGH);
    }
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

    pinMode(LED_WM_PIN0, OUTPUT);
    pinMode(LED_WM_PIN1, OUTPUT);
    pinMode(LED_RID_WRITEABLE_PIN, OUTPUT);
    
    delay(2000);
}


void loop() {
  // clear all flags
    RFID_RID_READY_FLAG = false;
    NEW_CARD_READY_FLAG = false;
  
    // Read serial
    if (Serial.available()) {
        Serial.readBytes(data_buffer, DATA_BUFFER_SIZE);
    
        // Parse command
        if (data_buffer[0] == WM_STD || data_buffer[0] == WM_REG || data_buffer[0] == WM_CNL || data_buffer[0] == WM_TRN) {
            // Switch WORK_MODE
            WORK_MODE = data_buffer[0];
            NEW_WRITABLE_RID_FLAG = false;
            set_LED_WM_PIN(WORK_MODE);
        } else if (data_buffer[0] == RID_CARRY && WORK_MODE == WM_REG) {
            // Store rid
            for (size_t i = 1; i < 1 + RID_SIZE; i++) {
                rid_from_serial[i-1] = data_buffer[i];
            }
            NEW_WRITABLE_RID_FLAG = true;  // enable to write rid to card
        }
    }

    // Set led
    if (NEW_WRITABLE_RID_FLAG) {
        digitalWrite(LED_RID_WRITEABLE_PIN, HIGH);
    } else {
        digitalWrite(LED_RID_WRITEABLE_PIN, LOW);
    }
  
    // Test RFID ready
    if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
        NEW_CARD_READY_FLAG = true;
    }

    // Read rid of RFID
    if (NEW_CARD_READY_FLAG) {
        // Authenticate using key A
        mfrc522_status = (MFRC522::StatusCode) mfrc522.PCD_Authenticate(
            MFRC522::PICC_CMD_MF_AUTH_KEY_A, RFID_TRAILERBLOCK_ADDR, &mifare_key, &(mfrc522.uid)
        );
        if (mfrc522_status == MFRC522::STATUS_OK) {
            // Authenticate success
            byte buf_size = sizeof(rid_from_rfid);
            mfrc522_status = (MFRC522::StatusCode) mfrc522.MIFARE_Read(RFID_BLOCK_ADDR, rid_from_rfid, &buf_size);
            if (mfrc522_status == MFRC522::STATUS_OK) {
                // Read success
                RFID_RID_READY_FLAG = true;  // set flag
            } else {
                // Read failed
                byte msg[RID_SIZE] = {
                    0xFE, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
                };
                Serial.write(DEBUG_MSG);
                Serial.write(msg, RID_SIZE);
            }
        } else {
            // Authenticate failed
            byte msg[RID_SIZE] = {
                0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
            };
            Serial.write(DEBUG_MSG);
            Serial.write(msg, RID_SIZE);
        }
    }

    // Works of WORK_MODE
    switch (WORK_MODE) {
        case WM_REG:
            // Write rid_from_serial to RFID
            if (NEW_CARD_READY_FLAG && NEW_WRITABLE_RID_FLAG) {
                // Authenticate using key A
                mfrc522_status = (MFRC522::StatusCode) mfrc522.PCD_Authenticate(
                    MFRC522::PICC_CMD_MF_AUTH_KEY_A, RFID_TRAILERBLOCK_ADDR, &mifare_key, &(mfrc522.uid)
                );
                if (mfrc522_status == MFRC522::STATUS_OK) {
                    // Authenticate success
                    mfrc522_status = (MFRC522::StatusCode) mfrc522.MIFARE_Write(RFID_BLOCK_ADDR, rid_from_serial, RID_SIZE);
                    if (mfrc522_status == MFRC522::STATUS_OK) {
                        // Write success
                        byte msg[RID_SIZE] = {
                            0xFD, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
                        };
                        Serial.write(DEBUG_MSG);
                        Serial.write(msg, RID_SIZE);
                    } else {
                        // write failed
                        byte msg[RID_SIZE] = {
                            0xFC, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
                        };
                        Serial.write(DEBUG_MSG);
                        Serial.write(msg, RID_SIZE);
                    }
                } else {
                    // Authenticate failed
                    byte msg[RID_SIZE] = {
                        0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
                    };
                    Serial.write(DEBUG_MSG);
                    Serial.write(msg, RID_SIZE);
                }
            }
            break;
            
        case WM_CNL:
        case WM_TRN:
            if (RFID_RID_READY_FLAG) {
                // Send rid_from_rfid to serial
                Serial.write(RID_CARRY);
                Serial.write(rid_from_rfid, RID_SIZE);
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
}
