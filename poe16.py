import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the RGB image
image = cv2.imread('image1.jpg')

if image is None:
    print("Error loading the image.")
else:
    # Normalize the image by dividing by the maximum pixel value (255)
    normalized_image = cv2.normalize(image, None, 0, 1.0,cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    # Display the original image and the normalized image
    plt.figure(figsize=(12, 6))

    # Original RGB Image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original RGB Image')
    plt.axis('off')

    # Normalized RGB Image
    plt.subplot(1, 2, 2)
    plt.imshow(normalized_image)
    plt.title('Normalized RGB Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
