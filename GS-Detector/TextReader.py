import cv2
from gtts import gTTS
import os
from PIL import Image
from pytesseract import pytesseract
camera = cv2.VideoCapture(0)
while True:
    _,image = camera.read()
    cv2.imshow('Text Detection', image)
    if cv2.waitKey(1)& 0xFF==ord ('s'):
        cv2.imwrite('test1.jpg', image)
        break
camera.release()
cv2.destroyAllWindows()
def tesseract():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    Imagepath = 'test1.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(Imagepath))
    return text
print(tesseract())
myText = tesseract()
language = 'en'
output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3")
os.system("start output.mp3")

