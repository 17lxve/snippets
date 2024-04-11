import numpy as np
import cv2
import os,argparse
import imutils
import sys
import pytesseract
from PIL import Image
for x in range(1,2):
    pytesseract.pytesseract.tesseract_cmd = r"C:/Users/othniel.kouadio/AppData/Local/Tesseract-OCR/tesseract.exe"
    os.chmod("max.py", 0o777)

    #5303JF01
    # read and resize image to the required size
    image = cv2.imread(r"test{}.jpg".format(str(x)))
    #get image dimensions
    height, width = image.shape[:-1]
    print(width, height)
    print("test{}.jpg".format(str(x)))
    x1,y1,x2,y2=(width//3)+80,120+height//2,2*(width//3)-60,height-50
    crop_image = image[y1:y2, x1:x2]
    cv2.imshow("Cropped", crop_image)
    cv2.waitKey(0)


    # convert to gray scale
    gray = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
    """cv2.imshow("Grayscale Conversion", gray)"""

    # blur to reduce noise
    gray = cv2.bilateralFilter(gray, 11, 30, 30)
    cv2.imshow("Bilateral Filter", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    text = pytesseract.image_to_string(gray,config='--psm 12')
    print(text)