import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the RGB image
image = cv2.imread('image1.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)

# Display the original image and the segmented edges
plt.figure(figsize=(12, 6))

# Display the original RGB image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original RGB Image')
plt.axis('off')

# Display the segmented edges
plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Segmented Edges (Canny Operator)')
plt.axis('off')

plt.tight_layout()
plt.show()
