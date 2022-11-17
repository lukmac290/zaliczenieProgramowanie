from fastapi import File
from PIL import Image
import PIL.ImageOps
import io
from fastapi.responses import StreamingResponse


def InvertPictureColors(file: bytes = File()):
    image = Image.open(io.BytesIO(file))
    inverted_image = PIL.ImageOps.invert(image)
    responseImage = io.BytesIO()
    inverted_image.save(responseImage, "JPEG")
    responseImage.seek(0)
    return StreamingResponse(responseImage, media_type="image/jpeg")