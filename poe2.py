import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

input=Image.open('image1.jpg')
negative=np.asarray(input)
negative_img=255-negative
output=Image.fromarray(negative_img)

plt.figure(figsize=(12,8))
plt.subplot(1,2,1)
plt.title('INput')
plt.imshow(input)

plt.subplot(1,2,2)
plt.title('INput')
plt.imshow(output)

plt.show()