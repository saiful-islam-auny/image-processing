import cv2

image_path = input("Enter the path to the image: ")
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to read the image.")
else:
    desired_width = int(input("Enter the desired width: "))
    desired_height = int(input("Enter the desired height: "))

    shrink_ratio_width = desired_width / image.shape[1]
    shrink_ratio_height = desired_height / image.shape[0]

    shrink_ratio = max(shrink_ratio_width, shrink_ratio_height)

    new_width = int(image.shape[1] * shrink_ratio)
    new_height = int(image.shape[0] * shrink_ratio)

    shrunken_image = cv2.resize(image, (new_width, new_height))

    cv2.imshow("Shrunken Image", shrunken_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
