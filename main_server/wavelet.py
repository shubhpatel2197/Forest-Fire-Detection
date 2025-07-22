import numpy as np
import pywt
import cv2

def w2d(img, mode='haar', level=1):
    imArray = img
    imArray = cv2.cvtColor(imArray, cv2.COLOR_BGR2GRAY)
    imArray = np.float32(imArray)
    imArray /=255
    
    coeff = pywt.wavedec2(imArray, mode, level)
    
    coeff_H = list(coeff)
    coeff_H[0] *= 0
    imArray_H = pywt.waverec2(coeff_H, mode)
    imArray_H *= 255
    imArray_H = np.uint8(imArray_H)
    
    return imArray_H

if __name__ == "__main__":
    original_image = cv2.imread('fire_0003.jpg')
    im_har = w2d(original_image, 'db1', 5)