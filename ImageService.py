from PIL import Image
import PIL.ImageOps  

def InvertPictureColors(path):
    image = Image.open(path)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.show()
    print("Image colors inverted succesfully")