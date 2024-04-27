import pywt
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the RGB image
image = cv2.imread('image1.jpg')

if image is None:
    print("Error loading the image.")
else:
    # Convert the image to grayscale
    gray_image = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

    # Apply DWT transformation (Haar wavelet)
    coeffs = pywt.dwt2(gray_image, 'haar')
    cA, (cH, cV, cD) = coeffs
    
    # Apply inverse DWT (IDWT) transformation
    idwt_image = pywt.idwt2((cA, (cH, cV, cD)), 'haar')

    # Calculate PSNR between original and IDWT images
    mse = np.mean((gray_image - idwt_image) ** 2)
    if mse == 0:
        psnr = 100  # PSNR is infinite if images are identical
    else:
        max_pixel_value = 255.0
        psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))

    # Display the original image, IDWT image, and PSNR value
    plt.figure(figsize=(12, 6))

    # Original RGB Image
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original RGB Image')
    plt.axis('off')

    # IDWT Image (Reconstructed)
    plt.subplot(1, 3, 2)
    plt.imshow(idwt_image, cmap='gray')
    plt.title('IDWT Image')
    plt.axis('off')

    # Display PSNR value
    plt.subplot(1, 3, 3)
    plt.text(0.5, 0.5, f'PSNR: {psnr:.2f} dB', fontsize=12, ha='center')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
