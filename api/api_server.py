from fastapi import FastAPI, Body, Request, Response
import uvicorn

from database import database
from definitions import API_HOST, API_PORT

app = FastAPI()

db = database.DatabaseInterface()


@app.get("/rfid-ticket-api")
async def api_root():
    return {"api_response": "Welcome to RFID Ticket API", "version": "1.0"}


@app.get("/rfid-ticket-api/card")
async def get_all_cards():
    ret = db.find_all_cards()
    return {"api_response": ret}


@app.get("/rfid-ticket-api/card/{rid}")
async def get_card(rid: str):
    ret = db.find_card(rid)
    return {"api_response": ret}


@app.get("/rfid-ticket-api/transaction_record/{rid}")
async def get_all_transaction_records(rid: str):
    ret = db.find_all_transaction_records(rid)
    return {"api_response": ret}


if __name__ == "__main__":
    uvicorn.run("api_server:app", host=API_HOST, port=API_PORT, reload=True)
