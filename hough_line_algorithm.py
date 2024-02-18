import cv2
import numpy as np

# Detects lines and rotates them using Canny edge detection followed by Hough transform to detect edges in a given image.

def detect_lines(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    # Canny Parameters: image, low threshold, high threshold, aperture size (sobel gradiant calculation), L2 Gradient norm (optional: True or False)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)
    # Hough Line parameters: image, rho, theta, threshold, minLineLength, maxLineGap
    return lines, edges

def find_longest_line(lines):
    max_length = 0
    longest_line = None
    for line in lines:
        x1, y1, x2, y2 = line[0]
        length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if length > max_length:
            max_length = length
            longest_line = line
    return longest_line

def count_windows_and_floors(image, lines):
    window_count = 0
    floor_count = 0
    longest_line = find_longest_line(lines)
    x1_longest, y1_longest, x2_longest, y2_longest = longest_line[0]
    max_y = max(y1_longest, y2_longest)
    min_y = min(y1_longest, y2_longest)

    # The height range of windows can often be different, so it may not be sufficient to compare the detected lines with the longest line.
    # A specific height range or other characteristics may also need to be taken into account to determine the lines considered as windows.

    for line in lines:
        x1, y1, x2, y2 = line[0]
        if np.array_equal(line, longest_line):
            continue
        if min_y < y1 < max_y or min_y < y2 < max_y:
            window_count += 1
        else:
            floor_count += 1

    return window_count, floor_count, longest_line

def draw_HoughLines(image, lines):
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

def main():
    original_image = cv2.imread("bina.png")
    image = cv2.imread("bina.png")
    lines, edges = detect_lines(image)
    if lines is not None:
        window_count, floor_count, longest_line = count_windows_and_floors(image, lines)
        hough_lined_image = np.copy(image)
        draw_HoughLines(hough_lined_image, lines)
        cv2.putText(hough_lined_image, "Window Count:" + str(window_count), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.imshow("Detected Lines: ", hough_lined_image)
        cv2.imshow("Image: ", original_image)
        cv2.imshow("Canny Edges: ", edges)
        x1, y1, x2, y2 = longest_line[0]
        cv2.line(edges, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cv2.putText(edges, "Longest Line", (int(((x1 + x2) / 2) - 20), int((y1 + y2) / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
        cv2.imshow("Longest Line", edges)
        print("Window Count:", window_count)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error")

if __name__ == '__main__':
    main()
