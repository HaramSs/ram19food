from fastapi import FastAPI
from typing import Union
import pickle

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/food")
def food(name:str):
    # 시간을 구함
    # 음식 이름과 시간을 CSV 로 저장 -> code/data.food.csv
    return {"food": name, "time": "2024-09-14 11:12:13"}