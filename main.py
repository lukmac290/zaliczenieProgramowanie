from typing import Union
from fastapi import FastAPI, File, UploadFile

from services.PrimeNumberService import checkPrimeNumber
from services.ImageService import InvertPictureColors

app = FastAPI()
# W folderze z mainem w cmd 'uvicorn main:app --reload'
#swagger - http://127.0.0.1:8000/docs

#zad1
@app.get("/project/primeverif/{number}")
def prime(number: str):
    response = {
        "Number": number,
        "Prime": checkPrimeNumber(number)
    }
    return response

#zad2
@app.post("/project/upload")
def UploadImage(file: bytes = File(...)):
    with open('image.jpg','wb') as image:
        image.write(file)
        image.close()
        return "Image succesfully uploaded"

@app.get("/project/invertimage")
def imageConvertedColors():
    return InvertPictureColors()
