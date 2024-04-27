import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the RGB image
image = cv2.imread('image1.jpg')

if image is None:
    print("Error loading the image.")
else:
    # Define translation parameters
    shift_right = 20
    shift_down = 10

    # Construct the translation matrix
    translation_matrix1 = np.float32([[1, 0, shift_right], [0, 1, 1]])

    # Perform image translation
    translated_image1 = cv2.warpAffine(image, translation_matrix1, (image.shape[1], image.shape[0]))

    translation_matrix2 = np.float32([[1, 0,1], [0, 1, shift_down]])

    # Perform image translation
    translated_image2 = cv2.warpAffine(image, translation_matrix2, (image.shape[1], image.shape[0]))

    # Display the original image and translated images
    plt.figure(figsize=(12, 6))

    # Original RGB Image
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original RGB Image')
    plt.axis('off')

    # Translated RGB Image (Shifted Right)
    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(translated_image1, cv2.COLOR_BGR2RGB))
    plt.title('Shifted Right by 20 units')
    plt.axis('off')

    # Translated RGB Image (Shifted Down)
    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(translated_image2, cv2.COLOR_BGR2RGB))
    plt.title('Shifted Down by 10 units')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
