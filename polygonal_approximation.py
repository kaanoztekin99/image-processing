import cv2
import numpy as np

def group_windows(image_path, show_image = True):
    # Upload the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect the edges
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Make contour detection on the edges, contour lines are obtained.
    contours, _ = cv2.findContours (edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Convert contours into the rectangles
    windows = []

    for contour in contours:
        area = cv2.contourArea(contour)
        # The area of each contour is calculated

        if area < 0:
            # Contours with a negative area are ignored.
            continue

        epsilon = 0.02 * cv2.arcLength(contour, True)
        # The epsilon value is used to control the level of smoothing in the process of converting the contour into an approximate polygon.
        # High epsilon values are generally preferred to obtain simpler shapes with fewer edges, while low epsilon values are used to obtain more detailed shapes with more edges.

        approx = cv2.approxPolyDP(contour, epsilon, True)
        # Quadrilateral contours are (approximately) detected (using cv2.approxPolyDP).
        # If a contour has 4 sides, it is considered a quadrilateral.
        if len(approx) == 4:
            windows.append(approx)

    windows.sort(key = lambda x: x[0][0][1])
    # Lambda is used to sort the quadrilaterals in the windows list according to the y coordinates of their top edges

    # Show the Canny edge-detected and grayscale image
    if show_image:
        image_copy = image.copy()
        for window in windows:
            cv2.drawContours(image, [window], -1, (0,255,0), 2)
        cv2.imshow("Windows detected", image)
        cv2.imshow("Canny Edges", edges)
        cv2.imshow("Grayscale Image", gray)
        cv2.imshow("Original Image", image_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return len(windows)

def main():
    image_path = "bina.png"
    floor_count = group_windows(image_path, True)
    print(f"Kat Sayısı: {floor_count}")

if __name__ == '__main__':
    main()
