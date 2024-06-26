import numpy as np
import cv2

color = [0, 0, 255] # 빨간색
pixel = np.uint8([[color]]) # 한픽셀로 구성된 이미지로 변환

hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV) 
# cvtColor 함수를 이용하여 hsv 색공간으로 변환

hsv = hsv[0][0] # 픽셀값을 가져옴

print("bgr: ", color)
print("hsv: ", hsv) # +_ 10
