from fastapi import FastAPI, Body, Request, Response
import uvicorn
from datetime import datetime

from database import database
from RFID_E_Payment.definitions import API_HOST, API_PORT, DATETIME_FORMAT

app = FastAPI()

db = database.DatabaseInterface()


@app.get("/rfid-epayment-api/")
async def api_root():
    return {"api_response": "Welcome to RFID Ticket API", "version": "1.0"}


@app.get("/rfid-epayment-api/card/")
async def get_all_cards():
    ret = db.find_all_cards()
    return {"api_response": ret}


@app.get("/rfid-epayment-api/card/{rid}/")
async def get_card(rid: str):
    ret = db.find_card(rid)
    return {"api_response": ret}


@app.get("/rfid-epayment-api/transaction_record/{rid}/")
async def get_all_transaction_records(rid: str):
    ret = db.find_all_transaction_records(rid)
    return {"api_response": ret}


@app.post("/rfid-epayment-api/transact/")
async def update_card_transact(payload: dict = Body(...)):
    if "rid" not in payload or "value" not in payload:
        return {"api_response": False}
    success = db.update_card_transact(payload.get("rid", ""), payload.get("value", 0))
    return {"api_response": success}


@app.post("/rfid-epayment-api/card_existed/")
async def check_registered_user_existed(payload: dict = Body(...)):
    if "rid" not in payload or "user_info" not in payload:
        return {"api_response": -1}
    existed = db.check_registered_card_existed(payload.get("rid", ""), payload.get("user_info", ""))
    return {"api_response": existed}


@app.post("/rfid-epayment-api/add_card/")
async def add_new_card(payload: dict = Body(...)):
    columns = ("rid", "user_info", "hash_key", "balance", "enable", "reg_date")
    for col in columns:
        if col not in payload:
            return {"api_response": -1}
    success = db.add_card(
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
    success = db.update_card_set_enable(payload.get("rid", ""), payload.get("enable", ""))
    return {"api_response": success}


@app.get("/rfid-epayment-api/delete_card/{rid}/")
async def delete_card(rid: str):
    success = db.delete_card(rid)
    return {"api_response": success}


if __name__ == "__main__":
    uvicorn.run("api_server:app", host=API_HOST, port=API_PORT, reload=True)
