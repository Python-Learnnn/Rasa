import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("image1.jpeg")
imgArray = np.asarray(img)

plt.figure(figsize=(24, 24))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(imgArray[:, :, 0], cmap='Reds', vmin=0, vmax=255)
plt.title("Red Channel")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(imgArray[:, :, 1], cmap='Greens', vmin=0, vmax=255)
plt.title("Green Channel")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(imgArray[:, :, 2], cmap='Blues', vmin=0, vmax=255)
plt.title("Blue Channel")
plt.axis('off')

plt.show()