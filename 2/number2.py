import json
import os
from typing import List
import typer # type: ignore

app = typer.Typer()
FILE_PATH = "data.json"

#read json file
def read_json_file() -> List:
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, EOFError):
        return []

@app.command()
def add(payload: str): #get json as string
    data = read_json_file()
    try:
        json_payload = json.loads(payload)
        data.append(json_payload) #add the new data
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4) 
        typer.echo("Data added successfully")
    except json.JSONDecodeError:
        typer.echo("Error: The provided argument is not a valid JSON string.")

@app.command()
def getRecent():
    data = read_json_file()
    recent = data[-10:]
    #if the file is empty
    if not recent:
        typer.echo("The file is empty")
    else:
        typer.echo(json.dumps(recent, indent=2))
    
if __name__ == "__main__":
    app()

