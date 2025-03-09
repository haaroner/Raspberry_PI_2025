cv2.namedWindow("Sliders")

cv2.createTrackbar('H_low', "Sliders", 0, 255, nothing)
cv2.createTrackbar('H_high', "Sliders", 0, 255, nothing)

cv2.createTrackbar('S_low', "Sliders", 0, 255, nothing)
cv2.createTrackbar('S_high', "Sliders", 0, 255, nothing)

cv2.createTrackbar('V_low', "Sliders", 0, 255, nothing)
cv2.createTrackbar('V_high', "Sliders", 0, 255, nothing)