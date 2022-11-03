from typing import Union
from fastapi import FastAPI, File

from services.PrimeNumberService import checkPrimeNumber
from services.ImageService import InvertPictureColors, Upload
app = FastAPI()
# W folderze z mainem w cmd 'uvicorn main:app --reload'
#swagger - http://127.0.0.1:8000/docs

#zad1
@app.get("/project/primeverif/{number}")
def prime(number: str):
    return checkPrimeNumber(number)

#zad2
@app.post("/project/uploadimage")
def UploadImage(file: bytes = File(...)):
    return Upload(file)

@app.get("/project/invertimage")
def imageConvertedColors():
    return InvertPictureColors()
