import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = input("Enter the path to the image: ")
image = cv2.imread(image_path)  # Read the image

if image is None:
    print("Error: Unable to read the image.")
else:
    # Plot histogram
    plt.figure(figsize=(10, 5))
    
    # Plot histogram on the left
    plt.subplot(1, 2, 1)
    plt.hist(image.ravel(), bins=256, range=[0, 256], color='blue', alpha=0.7)
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.title('Image Histogram')
    
    # Display original image on the right
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')  # Hide axis
    
    plt.show()
