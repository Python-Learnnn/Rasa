import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the RGB image
image = cv2.imread('image1.jpg')

if image is None:
    print("Error loading the image.")
else:
    # Split the image into its color channels (BGR format)
    b, g, r = cv2.split(image)

    # Define an enhancement factor (adjust as needed)
    enhancement_factor = 1.5

    # Enhance the red channel by multiplying with the enhancement factor
    enhanced_r = np.clip(r * enhancement_factor, 0, 255).astype(np.uint8)

    # Merge the enhanced red channel with the original green and blue channels
    enhanced_image = cv2.merge((b, g, enhanced_r))

    # Display the original image and the enhanced image
    plt.figure(figsize=(12, 6))

    # Original RGB Image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original RGB Image')
    plt.axis('off')

    # Enhanced RGB Image
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB))
    plt.title('Enhanced RGB Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
