import cv2
import numpy as np

# Load image
image = cv2.imread("flower (1).jpg")

if image is None:
    print("Image not found!")
    exit()

current_image = image.copy()

while True:

    print("\n========== IMAGE PROCESSING LAB ==========")
    print("1. Display Image")
    print("2. Display Image Properties")
    print("3. Convert to Grayscale")
    print("4. Increase Brightness")
    print("5. Increase Contrast")
    print("6. Resize Image")
    print("7. Rotate Image")
    print("8. Flip Image")
    print("9. Crop Image")
    print("10. Negative Image")
    print("11. Save Image")
    print("0. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # 1. Display Image
    if choice == 1:
        cv2.imshow("Current Image", current_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 2. Display Image Properties
    elif choice == 2:
        print("\n========== IMAGE PROPERTIES ==========")
        print("Height :", current_image.shape[0])
        print("Width  :", current_image.shape[1])

        if len(current_image.shape) == 3:
            print("Channels :", current_image.shape[2])
        else:
            print("Channels : 1")

        print("Size :", current_image.size)
        print("Data Type :", current_image.dtype)

    # 3. Convert to Grayscale
    elif choice == 3:
        if len(current_image.shape) == 3:
            current_image = cv2.cvtColor(
                current_image,
                cv2.COLOR_BGR2GRAY
            )
            print("Image converted to grayscale.")
        else:
            print("Image is already grayscale.")

        cv2.imshow("Grayscale Image", current_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 4. Increase Brightness
    elif choice == 4:
        try:
            value = int(input("Enter Brightness Value (0-100): "))

            if 0 <= value <= 100:
                current_image = cv2.convertScaleAbs(
                    current_image,
                    alpha=1.0,
                    beta=value
                )

                cv2.imshow("Brightness Increased", current_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print("Enter value between 0 and 100.")

        except ValueError:
            print("Invalid brightness value.")

    # 5. Increase Contrast
    elif choice == 5:
        try:
            alpha = float(input("Enter Contrast Value (1.0 - 3.0): "))

            if 1.0 <= alpha <= 3.0:
                current_image = cv2.convertScaleAbs(
                    current_image,
                    alpha=alpha,
                    beta=0
                )

                cv2.imshow("Contrast Increased", current_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print("Enter value between 1.0 and 3.0.")

        except ValueError:
            print("Invalid contrast value.")

    # 6. Resize Image
    elif choice == 6:
        try:
            width = int(input("Enter New Width: "))
            height = int(input("Enter New Height: "))

            if width > 0 and height > 0:
                current_image = cv2.resize(
                    current_image,
                    (width, height)
                )

                cv2.imshow("Resized Image", current_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print("Width and height must be greater than 0.")

        except ValueError:
            print("Invalid dimensions.")

    # 7. Rotate Image
    elif choice == 7:
        try:
            angle = float(input("Enter Rotation Angle: "))

            h, w = current_image.shape[:2]
            center = (w // 2, h // 2)

            matrix = cv2.getRotationMatrix2D(
                center,
                angle,
                1.0
            )

            current_image = cv2.warpAffine(
                current_image,
                matrix,
                (w, h)
            )

            cv2.imshow("Rotated Image", current_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        except ValueError:
            print("Invalid rotation angle.")

    # 8. Flip Image
    elif choice == 8:
        print("\n1. Horizontal Flip")
        print("2. Vertical Flip")
        print("3. Both")

        try:
            flip_choice = int(input("Enter Choice: "))

            if flip_choice == 1:
                current_image = cv2.flip(current_image, 1)

            elif flip_choice == 2:
                current_image = cv2.flip(current_image, 0)

            elif flip_choice == 3:
                current_image = cv2.flip(current_image, -1)

            else:
                print("Invalid flip choice.")
                continue

            cv2.imshow("Flipped Image", current_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        except ValueError:
            print("Invalid choice.")

    # 9. Crop Image
    elif choice == 9:
        try:
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            width = int(input("Enter width: "))
            height = int(input("Enter height: "))

            img_h, img_w = current_image.shape[:2]

            if (
                x >= 0 and
                y >= 0 and
                width > 0 and
                height > 0 and
                x + width <= img_w and
                y + height <= img_h
            ):
                current_image = current_image[
                    y:y + height,
                    x:x + width
                ]

                cv2.imshow("Cropped Image", current_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            else:
                print("Invalid crop coordinates.")

        except ValueError:
            print("Invalid crop values.")

    # 10. Negative Image
    elif choice == 10:
        current_image = 255 - current_image

        cv2.imshow("Negative Image", current_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 11. Save Image
    elif choice == 11:
        filename = input(
            "Enter File Name (Example: output.jpg): "
        )

        if cv2.imwrite(filename, current_image):
            print("Image Saved Successfully.")
        else:
            print("Error: Could not save image.")

    # 0. Exit
    elif choice == 0:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")