import cv2
from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

im=Image.open('C:\\Users\\Aymane\\Desktop\\stage data\\programme\\data\\card5.png')
ex=pytesseract.image_to_string(im)
        
 
