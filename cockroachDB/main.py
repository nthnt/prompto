from fastapi import FastAPI
from promptoDB import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/db")
async def db():
    table = Table()
    table.createTable("models", "userPrompt", "STRING NOT NULL")
    table.addColumn("models","phrase", "STRING NOT NULL")
    
    return {"message": "Success"}