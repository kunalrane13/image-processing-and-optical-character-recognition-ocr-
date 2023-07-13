#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytesseract
from PIL import Image
import cv2


# In[5]:


img = cv2.imread('Mission.png')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(img):
    text= pytesseract.image_to_string(img)
    return text
def get_grescale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# def remove_noise(image):
#     return cv2.medianBlur(image,5)
def thresholding(image):
    return cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# In[6]:


img = get_grescale(img)
# img = remove_noise(img)
img = thresholding(img)


# In[7]:


print(ocr_core(img))


# In[ ]:




