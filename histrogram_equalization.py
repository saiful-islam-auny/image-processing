import cv2
import matplotlib.pyplot as plt

def plot_histogram(image, title, subplot_position):
    # Calculate histogram
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Plot histogram
    plt.subplot(subplot_position)
    plt.plot(histogram, color='blue')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.title(title)

# Load the image
image_path = input("Enter the path to the image: ")
original_image = cv2.imread(image_path)  # Read the image

if original_image is None:
    print("Error: Unable to read the image.")
else:
    # Convert the image to RGB color space
    original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    # Convert the image to grayscale for histogram equalization
    original_image_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Perform histogram equalization
    equalized_image = cv2.equalizeHist(original_image_gray)

    # Plot histograms
    plt.figure(figsize=(12, 6))


    plot_histogram(equalized_image, 'Histogram Equalization', 231)

    # Display original color image in the middle
    plt.subplot(1, 3, 2)
    plt.imshow(original_image_rgb)
    plt.title('Original Image')
    plt.axis('off')  # Hide axis

    # Display equalized image on the right
    plt.subplot(1, 3, 3)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Equalized Image')
    plt.axis('off')  # Hide axis

    plt.show()
