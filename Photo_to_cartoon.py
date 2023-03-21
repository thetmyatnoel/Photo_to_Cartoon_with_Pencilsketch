import cv2
import numpy as np

# Load the image
img = cv2.imread("KakaoTalk_Photo_2023-03-09-19-48-37.jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply median blur to smooth the image
gray = cv2.medianBlur(gray, 5)

# Detect edges using adaptive thresholding
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Apply bilateral filter to preserve edges while reducing noise
color = cv2.bilateralFilter(img, 9, 250, 250)

# Add a solid color background
background_color = (255, 255, 255) # white
background = img.copy()
background[:, :] = background_color

# Create a mask for the edges
mask = cv2.bitwise_not(edges)

# Apply the mask to the background image
background_masked = cv2.bitwise_and(background, background, mask=edges)

# Apply the mask to the color image
color_masked = cv2.bitwise_and(color, color, mask=mask)

# Add a sketch effect
sketch_gray, sketch_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

# Combine the edge-detected image with the color image and sketch effect
cartoon = cv2.add(background_masked, color_masked)
cartoon = cv2.addWeighted(cartoon, 0.6, sketch_color, 0.4, 0)

# Increase contrast and brightness
alpha = 1.3
beta = 30
cartoon = cv2.convertScaleAbs(cartoon, alpha=alpha, beta=beta)

merge = np.hstack((img, cartoon))

# Display the original and cartoon images side by side
cv2.imshow("Original Image  |   Cartoon Image", merge)
cv2.waitKey(0)
cv2.destroyAllWindows()
