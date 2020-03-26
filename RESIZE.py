from PIL import Image
import os
import numpy as np
import cv2 as cv


GT_List = os.listdir(r'F:\retest\GT')

for i in GT_List:
    img_path = os.path.join(r'F:\retest\GT',i)
    print(img_path)
    img = cv.imread(img_path)
    img = cv.resize(img,(640,480))
    save_path = os.path.join(r'F:\retest\GT',i)
    cv.imwrite(save_path,img)
