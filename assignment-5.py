from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def rgb_to_cmy(rgb_image):
    cmy_image = Image.new('RGB', rgb_image.size)
    width, height = rgb_image.size

    for x in range(width):
        for y in range(height):
            r, g, b = rgb_image.getpixel((x, y))
            c = 255.0 - r 
            m = 255.0 - g 
            y_ = 255.0 - b 
            cmy_image.putpixel((x, y), (int(c), int(m), int(y_ )))

    return cmy_image

# def normalize_cmy(cmy_image):
#     width, height = cmy_image.size
#     normalized_image = Image.new('RGB', cmy_image.size)

#     for x in range(width):
#         for y in range(height):
#             c, m, y_ = cmy_image.getpixel((x, y))
#             # Normalize CMY values to the range [0, 1]
#             normalized_c = c / 255.0
#             normalized_m = m / 255.0
#             normalized_y = y_ / 255.0
#             # Convert normalized CMY values back to 0-255 range
#             normalized_c *= 255
#             normalized_m *= 255
#             normalized_y *= 255
#             normalized_image.putpixel((x, y), (int(normalized_c), int(normalized_m), int(normalized_y)))

#     return normalized_image

def normalize_cmy(image):
    image = np.array(image)

    image = image.astype(np.float32)
    
    image = (image - np.min(image)) / (np.max(image) - np.min(image))
    
    return image

# Load RGB image
rgb_image = Image.open('image1.jpg')

# Convert RGB to CMY
cmy_image = rgb_to_cmy(rgb_image)

# Normalize CMY image
normalized_cmy_image = normalize_cmy(cmy_image)

# Plot the images
plt.figure(figsize=(12, 8))

# Original RGB image
plt.subplot(1, 3, 1)
plt.imshow(rgb_image)
plt.title('Original RGB Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cmy_image)
plt.title('CMY image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(normalized_cmy_image)
plt.title('Normalised CMY Image')
plt.axis('off')

plt.tight_layout()
plt.show()