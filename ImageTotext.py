import re
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
text = pytesseract.image_to_string(Image.open('test4.png'))
#text=re.sub(r'\s+', '', text)
print(text)
