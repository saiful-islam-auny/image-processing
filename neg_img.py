import cv2
import matplotlib.pyplot as plt

# Read the input image
image_path = input("Enter the path: ")
original_image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Find the negative image
negative_image = 255 - gray_image

# Display the original, grayscale, and negative images
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')

plt.subplot(1, 3, 3)
plt.imshow(negative_image, cmap='gray')
plt.title('Negative Image')

plt.show()