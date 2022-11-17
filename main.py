from typing import Union
from fastapi import FastAPI, File
from services.PrimeNumberService import checkPrimeNumber
from services.ImageService import InvertPictureColors
from services.AuthorizationService import GenerateToken
from services.TimeService import GetCurrentDateTime

app = FastAPI()
# W folderze z mainem w cmd 'uvicorn main:app --reload'
#swagger - http://127.0.0.1:8000/docs

#zad1
@app.get("/project/primeverif/{number}")
def prime(number: str):
    return checkPrimeNumber(number)

#zad2
@app.post("/project/invertpicture")
def invertpicture(file: bytes = File()):
    return InvertPictureColors(file)

#zad3
@app.get("/project/generatetoken")
def getToken():
    return GenerateToken()

@app.get("/project/getcurrenttime/{providetoken}")
def Authorize(providetoken: str):
    correct = GenerateToken()
    if(providetoken == correct):
        return GetCurrentDateTime()
    else:
        return "Provided token is not correct!"
