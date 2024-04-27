import cv2
import matplotlib.pyplot as plt

# Load the grayscale 8-bit image
gray_image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

if gray_image is None:
    print("Error loading the image.")
else:
    # Define the threshold value (adjust as needed)
    threshold_value = 128

    # Apply binary thresholding
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

    # Display the original grayscale image and the binary image
    plt.figure(figsize=(12, 6))

    # Original Grayscale Image
    plt.subplot(1, 2, 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    # Binary Image after Thresholding
    plt.subplot(1, 2, 2)
    plt.imshow(binary_image, cmap='gray')
    plt.title('Binary Image after Thresholding')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
