import numpy as np
import cv2
import matplotlib.pyplot as plt

def histogram_equalization_color(image):
    # Split the image into its RGB channels
    r, g, b = cv2.split(image)
    
    # Perform histogram equalization on each channel
    r_eq = cv2.equalizeHist(r)
    g_eq = cv2.equalizeHist(g)
    b_eq = cv2.equalizeHist(b)
    
    # Merge the equalized channels back into a single color image
    equalized_image = cv2.merge((r_eq, g_eq, b_eq))
    
    return equalized_image

# Function to plot histogram
def plot_histogram(image, title):
    hist, bins = np.histogram(image.ravel(), 256, [0, 256])
    plt.plot(hist, color='black')
    plt.title(title)

# Load input image
input_image = cv2.imread("image1.jpg")

# Perform histogram equalization
equalized_image = histogram_equalization_color(input_image)

# Display original and equalized images
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))  # Display the original image
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB))  # Display the equalized image
plt.title('Equalized Image')
plt.axis('off')

plt.subplot(2, 2, 3)
plot_histogram(cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY), 'Original Histogram')
plt.title('Original Histogram')

plt.subplot(2, 2, 4)
plot_histogram(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2GRAY), 'Equalized Histogram')
plt.title('Equalized Histogram')

plt.tight_layout()
plt.show()
