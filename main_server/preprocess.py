import cv2
import numpy as np
from wavelet import w2d

def pre(img):
    scalled_raw_img = cv2.resize(img, (32,32))
    img_har = w2d(img, 'db1', 5)
    scalled_img_har = cv2.resize(img_har, (32,32))
    combined_img = np.vstack((scalled_raw_img.reshape(32*32*3,1),scalled_img_har.reshape(32*32,1)))
    len = 32*32*3 + 32*32
    final = combined_img.reshape(1,len).astype(float)
    return final

if __name__ == '__main__':
    original_image = cv2.imread('fire_0003.jpg')
    print(len(pre(original_image)))