from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

def normalize_image(image):
    image = np.array(image)

    image = image.astype(np.float32)
    
    image = (image - np.min(image)) / (np.max(image) - np.min(image))
    
    return image
    

input_image = Image.open('image1.jpg')
normalized_image = normalize_image(input_image)

# Plot the images
plt.figure(figsize=(12, 8))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(input_image)
plt.title('Original Image')
plt.axis('off')

# Normalised Image
plt.subplot(1, 2, 2)
plt.imshow(normalized_image)
plt.title('Normalised Image')
plt.axis('off')

plt.tight_layout()
plt.show()