import cv2
import numpy as np
import matplotlib.pyplot as plt

def normalize_image(image):
   
    img_normalized = cv2.normalize(image, None, 0, 1.0,
    cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    # ret,thresh = cv2.threshold(image,140,255,cv2.THRESH_BINARY)
    # print("Image data after Thresholding:\n", thresh)


    # img_normalized = cv2.normalize(thresh, None, 0, 1.0,
    # cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    return img_normalized

def rgb_to_cmy(rgb_image):
    # Normalize the RGB image
    normalized_rgb = normalize_image(rgb_image)

    # Calculate CMY values
    c = 1.0 - normalized_rgb[:, :, 0]  # Cyan
    m = 1.0 - normalized_rgb[:, :, 1]  # Magenta
    y = 1.0 - normalized_rgb[:, :, 2]  # Yellow

    # Stack CMY channels into a single image
    cmy_image = np.stack((c, m, y), axis=-1)

    return cmy_image

# Read the input RGB image
rgb_image = cv2.imread('image1.jpg')

# Normalize the RGB image
normalized_image = normalize_image(rgb_image)

# Convert RGB image to CMY
cmy_image = rgb_to_cmy(rgb_image)

# Plot the original image, normalized image, and CMY image side by side
plt.figure(figsize=(12, 4))

# Original RGB image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB))
plt.title('Original RGB Image')
plt.axis('off')

# Normalized image
plt.subplot(1, 3, 2)
plt.imshow(normalized_image)
plt.title('Normalized Image')
plt.axis('off')

# CMY image
plt.subplot(1, 3, 3)
plt.imshow(cmy_image)
plt.title('CMY Image')
plt.axis('off')

plt.show()