import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the RGB image
image = cv2.imread('image1.jpg')

if image is None:
    print("Error loading the image.")
else:
    # Separate the color channels
    b, g, r = cv2.split(image)

    # Apply DCT transformation to each channel
    dct_b = cv2.dct(np.float32(b))
    dct_g = cv2.dct(np.float32(g))
    dct_r = cv2.dct(np.float32(r))

    # Apply inverse DCT (IDCT) transformation to each channel
    idct_b = cv2.idct(dct_b)
    idct_g = cv2.idct(dct_g)
    idct_r = cv2.idct(dct_r)

    # Merge the color channels back into an RGB image
    idct_image = cv2.merge((idct_b, idct_g, idct_r))

    # Calculate PSNR between original and IDCT images
    mse = np.mean((image - idct_image) ** 2)
    if mse == 0:
        psnr = 100  # PSNR is infinite if images are identical
    else:
        max_pixel_value = 255.0
        psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))

    # Display the original image, IDCT image, and PSNR value
    plt.figure(figsize=(12, 6))

    # Original RGB Image
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original RGB Image')
    plt.axis('off')

    # IDCT Image (Reconstructed) displayed as RGB
    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(idct_image, cv2.COLOR_BGR2RGB))
    plt.title('IDCT Image (RGB)')
    plt.axis('off')

    # Display PSNR value
    plt.subplot(1, 3, 3)
    plt.text(0.5, 0.5, f'PSNR: {psnr:.2f} dB', fontsize=12, ha='center')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
