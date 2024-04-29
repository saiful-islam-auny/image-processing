import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the input image
image_path = input("Enter the path: ")
original_image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Apply log transformation
log_transformed_image = np.log1p(gray_image)

# Normalize the values to 0-255
log_transformed_image = (255 * (log_transformed_image - np.min(log_transformed_image)) / 
                         (np.max(log_transformed_image) - np.min(log_transformed_image))).astype(np.uint8)

# Display the original, grayscale, and log-transformed images
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')

plt.subplot(1, 3, 3)
plt.imshow(log_transformed_image, cmap='gray')
plt.title('Log Transformation Image')

plt.show()
