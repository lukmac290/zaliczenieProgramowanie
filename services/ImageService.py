from fastapi import File
from PIL import Image
import PIL.ImageOps
import io
from fastapi.responses import StreamingResponse


def InvertPictureColors(file: bytes = File()):
    input = Image.open(io.BytesIO(file))
    inverted = PIL.ImageOps.invert(input)
    response = io.BytesIO()
    inverted.save(response, "JPEG")
    response.seek(0)
    return StreamingResponse(response, media_type="image/jpeg")