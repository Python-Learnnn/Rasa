import cv2
import matplotlib.pyplot as plt

# Load the noisy RGB image
noisy_image = cv2.imread('noisy_image.jpeg')

if noisy_image is None:
    print("Error loading the image.")
else:
    # Apply Gaussian blur for smoothening
    smooth_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)

    # Display the original noisy image and the smoothened image
    plt.figure(figsize=(12, 6))

    # Original Noisy RGB Image
    plt.subplot(1, 2, 1)
    plt.imshow(noisy_image)
    plt.title('Original Noisy RGB Image')
    plt.axis('off')

    # Smoothened RGB Image
    plt.subplot(1, 2, 2)
    plt.imshow(smooth_image)
    plt.title('Smoothened RGB Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()