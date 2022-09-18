from fastapi import FastAPI
from promptoDB import *
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Cat(BaseModel):
    category: str
    id: int
    phrase: str

class Model(BaseModel):
    id: int
    userPrompt: str
    phrase: str


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/db")
async def db():
    table = Table()
    table.createTable("hate", "phrase", "STRING NOT NULL")
    
    return {"message": "Success"}

@app.post("/setValue/{cat.category}")
async def setValue(cat: Cat):
    table = Table()
    table.setValue(cat.category, ["ID", "phrase"], cat.id, [cat.phrase])

    return {"message": "Success"}

@app.get("/getValue/{cat.category}")
async def getValue(cat: Cat):
    table = Table()
    table.getValue(cat.category)

    return {"message": "Success"}