import cv2
import sys
import numpy as np

file_name = sys.argv[1]
image = cv2.imread(file_name)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_range = np.array([0, 0, 0])
upper_range = np.array([255, 255, 255])

mask = cv2.inRange(hsv_image, lower_range, upper_range)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

total_area = 0
total_circumference = 0

for contour in contours:
    area = cv2.contourArea(contour)
    circumference = cv2.arcLength(contour, True)
    total_area += area
    total_circumference += circumference

print(f"Total Circumference: {total_circumference}")
print(f"Total Area: {total_area}")

# cv2.write('Detected Color Area', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()