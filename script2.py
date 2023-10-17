import cv2
import sys
import numpy as np
file_name = sys.argv[1]
# Load the image
image = cv2.imread(file_name)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform shape detection
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    # Approximate the contour to a polygon
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    # Determine the shape based on the number of vertices
    num_vertices = len(approx)
    
    if num_vertices == 3:
        # Triangle detected
        side1 = np.linalg.norm(approx[0][0] - approx[1][0])
        side2 = np.linalg.norm(approx[1][0] - approx[2][0])
        side3 = np.linalg.norm(approx[2][0] - approx[0][0])
    
    elif num_vertices == 4:
        # Rectangle detected
        side1 = np.linalg.norm(approx[0][0] - approx[1][0])
        side2 = np.linalg.norm(approx[1][0] - approx[2][0])
        side3 = np.linalg.norm(approx[2][0] - approx[3][0])
        side4 = np.linalg.norm(approx[3][0] - approx[0][0])

print(f"Side 1: {side1}")
print(f"Side 2: {side2}")
print(f"Side 3: {side3}")
print(f"Side 4: {side4}")

# Display the image with shape and side length information
# cv2.imshow('Shape with Side Lengths', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()