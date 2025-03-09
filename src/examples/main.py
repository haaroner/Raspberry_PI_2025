from picamera2 import Picamera2 as picam2
from picamera2 import Preview
import numpy as np
import cv2

from gpiozero import CPUTemperature

import time

def nothing(x):
    pass

camera = picam2()
print_timer = 0
view_timer = 0
print(camera.sensor_modes)
print('            ')
print(camera.create_video_configuration())
camera_config = camera.create_video_configuration(use_case = {'buffer_count' : 4},
                                                  controls = {'FrameDurationLimits' : (10000, 22000)},
                                                  sensor={"output_size":(600, 600)},
                                                  raw = {'format': 'SGBRG10', 'fps':'60'})
#camera.preview_configuration.main
camera.configure(camera_config)

#camera.start_preview(Preview.QTGL)
cv2.startWindowThread()
cv2.namedWindow("Sliders")
cv2.namedWindow("Camera")
cv2.resizeWindow('Camera', 600, 600)

cv2.createTrackbar('H_low', "Sliders", 0, 255, nothing)
cv2.createTrackbar('H_high', "Sliders", 0, 255, nothing)

cv2.createTrackbar('S_low', "Sliders", 0, 255, nothing)
cv2.createTrackbar('S_high', "Sliders", 0, 255, nothing)

cv2.createTrackbar('V_low', "Sliders", 0, 255, nothing)
cv2.createTrackbar('V_high', "Sliders", 0, 255, nothing)

camera.start()
blue_low = np.array([94, 80, 2], np.uint8)
blue_high = np.array([124, 255, 255], np.uint8)

yellow_low = np.array([94, 80, 2], np.uint8)
yellow_high = np.array([124, 255, 255], np.uint8)

counter = 0
while True:
    timer = time.time() * 1000
    counter+=1
    
    image = camera.capture_array()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    
    blue_low[0] = cv2.getTrackbarPos('H_low', 'Sliders')
    blue_high[0] = cv2.getTrackbarPos('H_high', 'Sliders')
    
    blue_low[1] = cv2.getTrackbarPos('S_low', 'Sliders')
    blue_high[1] = cv2.getTrackbarPos('S_high', 'Sliders')
    
    blue_low[2] = cv2.getTrackbarPos('V_low', 'Sliders')
    blue_high[2] = cv2.getTrackbarPos('V_high', 'Sliders')
    mask = cv2.inRange(hsv_image, blue_low, blue_high)
    
    if(timer - print_timer > 1000):
        print("CPU temp =",CPUTemperature().temperature)
        #print('time =', time.time())
        print("fps =", counter)
        counter = 0
        print_timer = timer
    cv2.imshow("Camera", image)
    key = cv2.waitKey(1) & 0xFF
        
    if key == 27:
        break

