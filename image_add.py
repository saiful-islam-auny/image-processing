import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path1 = input("Enter 1st image path: ")
image1 = cv2.imread(image_path1)

image_path2 = input("Enter 2nd image path: ")
image2 = cv2.imread(image_path2)

if image1 is None or image2 is None:
    print("Error: One or both images could not be read.")
else:
    height, width = min(image1.shape[0], image2.shape[0]), min(
        image1.shape[1], image2.shape[1])
    image1_resized = cv2.resize(image1, (width, height))
    image2_resized = cv2.resize(image2, (width, height))

    combined_image = cv2.add(image1_resized, image2_resized)

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image1_resized, cv2.COLOR_BGR2RGB))
    plt.title('First')

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(image2_resized, cv2.COLOR_BGR2RGB))
    plt.title('Second')

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(combined_image, cv2.COLOR_BGR2RGB))
    plt.title('Marge Image')

    plt.show()
