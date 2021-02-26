from typing import Optional
from fastapi import FastAPI
from mongo import fetchData

app = FastAPI();

@app.get("/")
def read_root():
    return {"hello world"}

@app.get("/tickers/{ticker}")
def read_item(ticker:str):
    data = fetchData(ticker)
    return data['tweets']