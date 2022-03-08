# from PIL import Image
# import pytesseract
#
# pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
#
# im=Image.open("ankit.jpg")
# text=pytesseract.image_to_string(im,lang='eng')
# print(text)
from PIL import Image
image=Image.open('E:\pics\\ankit1.jpg')
width,height=image.size
print(image)
img=image.resize((int(width/4),int(height/4)))
print(img)

img.save("E:\pics\\resize1.jpg")

img.show();