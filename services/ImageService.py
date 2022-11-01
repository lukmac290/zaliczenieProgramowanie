from PIL import Image
import PIL.ImageOps
from fastapi.responses import FileResponse
from os.path import exists

def InvertPictureColors():
    if(exists('image.jpg')):
        image = Image.open('image.jpg')
        inverted_image = PIL.ImageOps.invert(image).save('inverted_image.jpg')
        return FileResponse('inverted_image.jpg', media_type="image/jpeg")
    else:
        return "File does not exist"