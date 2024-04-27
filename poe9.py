import cv2
import matplotlib.pyplot as plt

# Load the RGB image
image = cv2.imread('image1.jpg')

if image is None:
    print("Error loading the image.")
else:
    # Define scaling factors
    scale_factor_2x = 2.0
    scale_factor_half = 0.5

    # Perform image scaling
    scaled_image_2x = cv2.resize(image, None, fx=scale_factor_2x, fy=scale_factor_2x, interpolation=cv2.INTER_LINEAR)
    scaled_image_half = cv2.resize(image, None, fx=scale_factor_half, fy=scale_factor_half, interpolation=cv2.INTER_LINEAR)

    # Display the original image and scaled images
    plt.figure(figsize=(18, 6))  # Increase the width to accommodate the scaled images

    # Original RGB Image
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original RGB Image')
    plt.axis('off')

    # Scaled RGB Image (Factor 2x)
    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(scaled_image_2x, cv2.COLOR_BGR2RGB))  # Corrected color conversion
    plt.title('Scaled by Factor 2x')
    plt.axis('off')

    # Scaled RGB Image (Factor 0.5x)
    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(scaled_image_half, cv2.COLOR_BGR2RGB))  # Corrected color conversion
    plt.title('Scaled by Factor 0.5x')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
