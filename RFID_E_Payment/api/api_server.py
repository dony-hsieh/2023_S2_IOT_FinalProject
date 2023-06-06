from fastapi import FastAPI, Body
import uvicorn
from datetime import datetime

from database import database
from RFID_E_Payment.definitions import API_HOST, API_PORT, DATETIME_FORMAT

# URL Root: http://127.0.0.1:8000/rfid-epayment-api/

app = FastAPI()

server_db = database.DatabaseInterface()


@app.get("/rfid-epayment-api/")
async def api_root():
    return {"api_response": "Welcome to RFID Ticket API", "version": "1.0"}


@app.get("/rfid-epayment-api/card/")
async def get_all_cards():
    ret = server_db.find_all_cards()
    return {"api_response": ret}


@app.get("/rfid-epayment-api/card/{rid}/")
async def get_card(rid: str):
    ret = server_db.find_card(rid)
    return {"api_response": ret}


@app.get("/rfid-epayment-api/transaction_record/{rid}/")
async def get_all_transaction_records(rid: str):
    ret = server_db.find_all_transaction_records(rid)
    return {"api_response": ret}


@app.post("/rfid-epayment-api/transact/")
async def update_card_transact(payload: dict = Body(...)):
    if "rid" not in payload or "value" not in payload:
        return {"api_response": False}
    success = server_db.update_card_transact(payload.get("rid", ""), payload.get("value", 0))
    return {"api_response": success}


@app.post("/rfid-epayment-api/card_existed/")
async def check_registered_user_existed(payload: dict = Body(...)):
    if "rid" not in payload or "user_info" not in payload:
        return {"api_response": -1}
    existed = server_db.check_registered_card_existed(payload.get("rid", ""), payload.get("user_info", ""))
    return {"api_response": existed}


@app.post("/rfid-epayment-api/add_card/")
async def add_card(payload: dict = Body(...)):
    columns = ("rid", "user_info", "hash_key", "balance", "enable", "reg_date")
    for col in columns:
        if col not in payload:
            return {"api_response": -1}
    success = server_db.add_card(
        payload.get("rid", ""),
        payload.get("user_info"),
        payload.get("hash_key", ""),
        payload.get("balance", ""),
        payload.get("enable", ""),
        datetime.strptime(payload.get("reg_date", ""), DATETIME_FORMAT)
    )
    return {"api_response": success}


@app.post("/rfid-epayment-api/card_enable/")
async def update_card_set_enable(payload: dict = Body(...)):
    if "rid" not in payload or "enable" not in payload:
        return {"api_response": False}
    success = server_db.update_card_set_enable(payload.get("rid", ""), payload.get("enable", ""))
    return {"api_response": success}


@app.get("/rfid-epayment-api/delete_card/{rid}/")
async def delete_card(rid: str):
    success = server_db.delete_card(rid)
    return {"api_response": success}


@app.get("/rfid-epayment-api/scan_history/{rid}/")
async def get_scan_history(rid: str):
    ret = server_db.find_all_scan_histories(rid)
    return {"api_response": ret}


@app.post("/rfid-epayment-api/add_scan_history/")
async def add_scan_history(payload: dict = Body(...)):
    if any([col not in payload for col in ("rid", "scan_time")]):
        return {"api_response": False}
    success = server_db.add_scan_history(
        payload.get("rid", ""), datetime.strptime(payload.get("scan_time", ""), DATETIME_FORMAT)
    )
    return {"api_response": success}


@app.get("/rfid-epayment-api/newest_scan_history/{rid}/")
async def get_newest_scan_histories(rid: str):
    ret = server_db.find_newest_scan_history(rid)
    return {"api_response": ret}


@app.get("/rfid-epayment-api/newest_scan_history/")
async def get_any_newest_scan_histories():
    ret = server_db.find_any_newest_scan_history()
    return {"api_response": ret}


if __name__ == "__main__":
    uvicorn.run("api_server:app", host=API_HOST, port=API_PORT, reload=True)
