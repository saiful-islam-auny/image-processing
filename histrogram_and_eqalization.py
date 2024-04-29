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
image = cv2.imread(image_path)  # Read the image

if image is None:
    print("Error: Unable to read the image.")
else:
    # Convert the image to the LAB color space
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Split the LAB image into channels
    l_channel, a_channel, b_channel = cv2.split(lab_image)

    # Perform histogram equalization on the L (luminance) channel
    equalized_l_channel = cv2.equalizeHist(l_channel)

    # Plot histograms
    plt.figure(figsize=(12, 6))

    plt.subplots_adjust(wspace=0.5, hspace=0.5)  # Adjust the horizontal and vertical space between subplots

    plot_histogram(l_channel, 'Original Image Histogram', 231)
    plot_histogram(equalized_l_channel, 'Equalized Image Histogram', 234)

    # Merge the equalized L channel with the original A and B channels
    equalized_lab_image = cv2.merge((equalized_l_channel, a_channel, b_channel))

    # Convert the equalized LAB image back to the BGR color space
    equalized_image = cv2.cvtColor(equalized_lab_image, cv2.COLOR_LAB2BGR)

    # Display the original and equalized images
    plt.subplot(232), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(235), plt.imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB)), plt.title('Equalized Image')

    plt.show()
