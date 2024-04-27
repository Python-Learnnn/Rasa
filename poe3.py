from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open('image1.jpg')

image_rgb=image.convert('RGB')

image_array = np.array(image_rgb)

c = 1 - image_array[:,:,0] / 255.0
m = 1 - image_array[:,:,1] / 255.0
y = 1 - image_array[:,:,2] / 255.0

cmy_image = np.stack((c, m, y), axis=-1)
cmy_image_display = (cmy_image * 255).astype(np.uint8)
cmy_image_pil = Image.fromarray(cmy_image_display)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Original RGB Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cmy_image_pil)
plt.title('CMY Image')
plt.axis('off')

plt.tight_layout()
plt.show()