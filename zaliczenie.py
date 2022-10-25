from PIL import Image
import PIL.ImageOps  

#liczba pierwsza - DONE

# def checkPrimeNumber(data):
#     if (data.isnumeric() != True or int(data) < 0):
#         print("Provided data is of the string type, or it is negative!")
#     else:
#         checkSum = 0
#         for i in range(1, int(data)+1):
#             if int(data) % i == 0:
#                 checkSum += 1
#                 if checkSum >= 3:
#                     print("Provided number is not a prime numebr.")
#                     break
#         if checkSum == 2:
#             print("Provided number is a prime number.")

# data = input("Provide any positive number: ")
# checkPrimeNumber(data)

#inwersja kolorów jpg - DONE

image = Image.open('kot.jpg')
inverted_image = PIL.ImageOps.invert(image)
inverted_image.show()
print("inverted")