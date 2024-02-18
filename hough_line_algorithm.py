import cv2
import numpy as np

def detect_lines(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold = 100, minLineLength = 100, maxLineGap=10)
    return lines, edges

def count_windows_and_floors(image, lines):
    window_count = 0
    floor_count = 0

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1,y1), (x2,y2), (0, 255, 0), 2)
        if np.sqrt(( x2 - x1 )**2 + ( y2 - y1 )**2 ) < 200:
            window_count +=1
            cv2.putText(image, "Window", (int(((x1 + x2)/2)-20), int((y1+y2)/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        else:
            floor_count+=1
            cv2.putText(image, "Floor", (int(((x1 + x2) / 2) - 20), int((y1 + y2) / 2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return window_count, floor_count

def draw_HoughLines(image, lines):
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1,y1), (x2,y2), (0, 0, 255), 2)

def main():
    original_image = cv2.imread("bina.png")
    image = cv2.imread("bina.png")
    lines, edges = detect_lines(image)
    if lines is not None:
        window_count, floor_count = count_windows_and_floors(image, lines)
        hough_lined_image = np.zeros_like(image)
        draw_HoughLines(hough_lined_image, lines)
        cv2.putText(image, "Window Count:" + str(window_count), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)
        cv2.putText(image, "Floor Count:" + str(floor_count), (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
        cv2.imshow("Detected Lines: ", image)
        cv2.imshow("Image: ", original_image)
        cv2.imshow("Canny Edges: ", edges)
        cv2.imshow("Hough Lines ", hough_lined_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error")

if __name__ == '__main__':
    main()