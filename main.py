from typing import Union
from fastapi import FastAPI

from services.PrimeNumberService import checkPrimeNumber
from services.ImageService import InvertPictureColors

app = FastAPI()
# W folderze z mainem w cmd 'uvicorn main:app --reload'

#zad1
@app.get("/primeverif/{number}")
def prime(number: str):
    response = {
        "Number": number,
        "Prime": checkPrimeNumber(number)
    }
    return response
#zad2
# InvertPictureColors('kot.jpg')
