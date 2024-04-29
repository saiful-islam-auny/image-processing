import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the input image
image_path = input("Enter the path: ")
original_image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Define the gamma value for the power-law transformation (adjust as needed)
gamma = 10

# Apply power-law transformation
power_law_image = np.power(gray_image / 255.0, gamma)

# Normalize the values to 0-255
power_law_image = (255 * power_law_image).astype(np.uint8)

# Display the original, grayscale, and power-law transformed images
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')

plt.subplot(1, 3, 3)
plt.imshow(power_law_image, cmap='gray')
plt.title('Power Law Transformation Image')

plt.show()
