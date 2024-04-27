import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the RGB image
image = cv2.imread('image1.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Prewitt edge detection
prewitt_kernel_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
prewitt_kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)

prewitt_x = cv2.filter2D(gray_image, -1, prewitt_kernel_x)
prewitt_y = cv2.filter2D(gray_image, -1, prewitt_kernel_y)

# Ensure prewitt_x and prewitt_y have the same size and type
prewitt_x = cv2.convertScaleAbs(prewitt_x)
prewitt_y = cv2.convertScaleAbs(prewitt_y)

# Combine the x and y Prewitt gradients
prewitt_combined = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)

# Normalize the combined Prewitt image to 0-255
prewitt_normalized = cv2.normalize(prewitt_combined, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Threshold the Prewitt image to obtain edges
threshold_value = 50
edges = cv2.threshold(prewitt_normalized, threshold_value, 255, cv2.THRESH_BINARY)[1]

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
plt.title('Segmented Edges (Prewitt Operator)')
plt.axis('off')

plt.tight_layout()
plt.show()
