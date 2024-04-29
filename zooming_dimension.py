import cv2


def resize_image(input_image, scale_percent):
    # Get the original dimensions
    width = int(input_image.shape[1] * scale_percent / 100)
    height = int(input_image.shape[0] * scale_percent / 100)

    # Resize the image using cubic interpolation
    resized_image = cv2.resize(input_image, (width, height), interpolation=cv2.INTER_CUBIC)

    return resized_image


if __name__ == "__main__":
    # Input image path
    input_image_path = input("Enter the path to the image: ")

    # Read the input image
    original_image = cv2.imread(input_image_path)

    if original_image is None:
        print("Error: Unable to read the image.")
    else:
        # Get the zoom factor and shrink factor
        zoom_factor = float(input("Enter the zoom factor : "))
        shrink_factor = float(input("Enter the shrink factor : "))

        # Zoom the image
        zoomed_image = cv2.resize(original_image, None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_LINEAR)

        # Shrink the image
        shrunken_image = resize_image(original_image, shrink_factor * 100)

        # Display the original, zoomed, and shrunken images
        cv2.imshow("Original Image", original_image)
        cv2.imshow("Zoomed Image", zoomed_image)
        cv2.imshow("Shrunken Image", shrunken_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
