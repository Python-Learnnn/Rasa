import cv2
import matplotlib.pyplot as plt

image=cv2.imread('image1.jpg',cv2.IMREAD_GRAYSCALE)

negative_image=255-image
cv2.imwrite('negative.jpg',negative_image)
plt.figure(figsize=(12,8))

plt.subplot(1,2,1)
plt.title('Input image')
plt.imshow(image,cmap='gray')

plt.subplot(1,2,2)
plt.title('Negative image')
plt.imshow(negative_image,cmap='gray')



plt.show()