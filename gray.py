import cv2

image_path = input("Enter the path to the input image: ")

# Read the input image
image = cv2.imread(image_path)

# Check if the image is successfully loaded
if image is None:
    print("Error: Unable to load the image.")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale values
print("Grayscale values:")
for row in gray_image:
    for pixel in row:
        print(pixel, end=' ')
    print()

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
