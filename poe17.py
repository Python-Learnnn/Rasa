import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

# Check if image is loaded successfully
if image is None:
    print("Error loading image.")
else:
    # Define the intensity range to highlight (e.g., intensities from 100 to 200)
    min_intensity = 100
    max_intensity = 200

    # Apply gray-level slicing preserving the background
    mask = np.where((image >= min_intensity) & (image <= max_intensity), 255, 0).astype(np.uint8)
    result_preserve_bg = cv2.bitwise_and(image, mask)

    # Apply gray-level slicing not preserving the background
    result_non_preserve_bg = np.where((image >= min_intensity) & (image <= max_intensity), 255, image)

    # Display the results using matplotlib
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(result_preserve_bg, cmap='gray')
    plt.title('Gray-level Slicing (Preserve BG)')

    plt.subplot(1, 3, 3)
    plt.imshow(result_non_preserve_bg, cmap='gray')
    plt.title('Gray-level Slicing (Non-Preserve BG)')

    plt.show()
