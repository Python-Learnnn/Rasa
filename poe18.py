import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the two grayscale images
image1 = cv2.imread('w1.jpeg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('w2.jpeg', cv2.IMREAD_GRAYSCALE)

# Check if images are loaded successfully
if image1 is None or image2 is None:
    print("Error loading images.")
else:
    # Perform addition of the two images
    addition_result = cv2.add(image1, image2)

    # Perform subtraction of the two images
    subtraction_result = cv2.subtract(image1, image2)

    # Display the results using matplotlib
    plt.figure(figsize=(10, 5))

    plt.subplot(2, 2, 1)
    plt.imshow(image1, cmap='gray')
    plt.title('Image 1')

    plt.subplot(2, 2, 2)
    plt.imshow(image2, cmap='gray')
    plt.title('Image 2')

    plt.subplot(2, 2, 3)
    plt.imshow(addition_result, cmap='gray')
    plt.title('Addition Result')

    plt.subplot(2, 2, 4)
    plt.imshow(subtraction_result, cmap='gray')
    plt.title('Subtraction Result')

    plt.show()
