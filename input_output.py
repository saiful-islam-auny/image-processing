import cv2
from matplotlib import pyplot as plt

image_path = input("Enter the path: ")
original_image = cv2.imread(image_path)

gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 2, 2), plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image'), plt.xticks([]), plt.yticks([])

plt.show()
