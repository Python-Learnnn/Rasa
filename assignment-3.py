import numpy as np
import matplotlib.pyplot as plt
from PIL import Image 

image = Image.open('image2.jpeg')
imgArray = np.asarray(image)


inverted_image = 255-imgArray
inverted_image = Image.fromarray(inverted_image)
rotated_image = inverted_image.rotate(180)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(rotated_image)
plt.title("Inverted Image")

plt.show()