import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image1.jpg')

# Convert the image to grayscale
gray_image=cv2.imread('image1.jpg',cv2.IMREAD_GRAYSCALE)

# Apply Sobel edge detection
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Normalize the combined Sobel image to 0-255
sobel_normalized = np.uint8(255 * sobel_combined / np.max(sobel_combined))

threshold_value = 50
edges = cv2.threshold(sobel_normalized, threshold_value, 255, cv2.THRESH_BINARY)[1]

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
plt.title('Segmented Edges (Sobel Operator)')
plt.axis('off')

plt.tight_layout()
plt.show()
