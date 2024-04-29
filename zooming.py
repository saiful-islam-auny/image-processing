import cv2

image_path = input("Enter the path to the image: ")
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to read the image.")
else:
    zoom_ratio = float(input("Enter the zoom ratio (e.g., 1.5 for 1.5x zoom): "))

    height, width = image.shape[:2]

    new_height = int(height * zoom_ratio)
    new_width = int(width * zoom_ratio)

    zoomed_image = cv2.resize(image, (new_width, new_height))

    cv2.imshow("Zoomed Image", zoomed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
