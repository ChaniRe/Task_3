import json
import os
from fastapi import FastAPI, Body
from typing import List, Dict

#create the server
app = FastAPI()
FILE_PATH = "data.json"

#read json file
def read_json_file() -> list:
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, EOFError):
        return []

#add data to file
@app.post("/append")
async def append_payload(payload: Dict = Body(...)):
    data = read_json_file()
    data.append(payload) #add the new data
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)  
    return {"message": "Data added to List"}

#get 10 item
@app.get("/recent")
async def get_recent():
    data = read_json_file()
    return data[-10:] #return 10 recent items