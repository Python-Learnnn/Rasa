import cv2
import matplotlib.pyplot as plt

# Load the RGB image
image = cv2.imread('image1.jpg')

# Split the image into RGB channels
b, g, r = cv2.split(image)

# Compute histograms for each channel
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Display histograms
plt.figure(figsize=(12, 6))

# Blue channel histogram
plt.subplot(1, 3, 1)
plt.plot(hist_b, color='blue')
plt.title('Blue Channel Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Green channel histogram
plt.subplot(1, 3, 2)
plt.plot(hist_g, color='green')
plt.title('Green Channel Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

# Red channel histogram
plt.subplot(1, 3, 3)
plt.plot(hist_r, color='red')
plt.title('Red Channel Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
