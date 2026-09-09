import cv2

image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges
    edges = cv2.Canny(blur, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Create a copy for drawing results
    output = image.copy()
    count = 0

    # Detect objects using contours
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 500:
            count += 1

            x, y, w, h = cv2.boundingRect(contour)

            # Draw bounding box
            cv2.rectangle(
                output,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Add object label
            cv2.putText(
                output,
                f"Object {count}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Print number of detected objects
    print("Objects detected:", count)

    # Save final result
    cv2.imwrite("output.jpg", output)

    # Display results
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Edge Detection", edges)
    cv2.imshow("Detected Objects", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()