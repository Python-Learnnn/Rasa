import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the RGB image
image = cv2.imread('image1.jpg')

if image is None:
    print("Error loading the image.")
else:
    # Save the original image for comparison
    cv2.imwrite('original_image.jpg', image)

    # Apply JPEG compression with a compression factor (quality) of 90
    compression_params = [cv2.IMWRITE_JPEG_QUALITY, 10]
    cv2.imwrite('compressed_image.jpg', image, compression_params)

    # Decompress the compressed image
    decompressed_image = cv2.imread('compressed_image.jpg')

    # Calculate PSNR between original and decompressed images
    mse = np.mean((image - decompressed_image) ** 2)
    if mse == 0:
        psnr = 100  # PSNR is infinite if images are identical
    else:
        max_pixel_value = 255.0
        psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))

    # Display the original image, decompressed image, and PSNR value
    plt.figure(figsize=(12, 6))

    # Original RGB Image
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original RGB Image')
    plt.axis('off')

    # Decompressed RGB Image
    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(decompressed_image, cv2.COLOR_BGR2RGB))
    plt.title('Decompressed RGB Image')
    plt.axis('off')

    # Display PSNR value
    plt.subplot(1, 3, 3)
    plt.text(0.5, 0.5, f'PSNR: {psnr:.2f} dB', fontsize=12, ha='center')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
