import cv2
from PIL import Image
import pytesseract
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

nlp = en_core_web_sm.load()




pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

im=Image.open('C:\\Users\\Aymane\\Desktop\\stage data\\programme\\data\\card5.png')
ex=pytesseract.image_to_string(im)
doc = nlp(ex)
print([(X.text, X.label_) for X in doc.ents])





