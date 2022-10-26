from typing import Union
from fastapi import FastAPI

from services.PrimeNumberService import checkPrimeNumber
from services.ImageService import InvertPictureColors

app = FastAPI()
# W folderze z mainem w cmd 'uvicorn main:app --reload'
#swagger - http://127.0.0.1:8000/docs

#zad1
#http://127.0.0.1:8000/primeverif/20
@app.get("/primeverif/{number}")
def prime(number: str):
    response = {
        "Number": number,
        "Prime": checkPrimeNumber(number)
    }
    return response
#zad2
# InvertPictureColors('kot.jpg')
