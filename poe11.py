import cv2
import matplotlib.pyplot as plt

# Load the RGB image
image = cv2.imread('image1.jpg')

if image is None:
    print("Error loading the image.")
else:
    # Rotate the image clockwise by 90 degrees
    rotated_image_clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Rotate the image anti-clockwise by 90 degrees
    rotated_image_anticlockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display the original image and rotated images
    plt.figure(figsize=(12, 6))

    # Original RGB Image
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original RGB Image')
    plt.axis('off')

    # Rotated RGB Image (Clockwise)
    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(rotated_image_clockwise, cv2.COLOR_BGR2RGB))
    plt.title('Rotated Clockwise by 90°')
    plt.axis('off')

    # Rotated RGB Image (Anti-clockwise)
    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(rotated_image_anticlockwise, cv2.COLOR_BGR2RGB))
    plt.title('Rotated Anti-clockwise by 90°')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
