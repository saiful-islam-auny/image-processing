import cv2

image_path = input("Enter the path to the image: ")
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to read the image.")
else:
    shrink_ratio = float(input("Enter the shrinking ratio (e.g., 0.5 for 0.5x shrink): "))

    height, width = image.shape[:2]

    new_height = int(height * shrink_ratio)
    new_width = int(width * shrink_ratio)

    shrunken_image = cv2.resize(image, (new_width, new_height))

    cv2.imshow("Shrunken Image", shrunken_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


