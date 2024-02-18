import cv2
import numpy as np

def main():
    image = cv2.imread("bina.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
    # Shi-Tomasi Corner Detection Applied
    corners = cv2.goodFeaturesToTrack(gray, maxCorners = 100, qualityLevel=0.01, minDistance=10)
    corners = np.int0(corners)
    # Sort the corners into the Vertical Line
    corners_sorted = sorted(corners, key = lambda x: x[0][1])
    # Deviation Threshold
    deviation_threshold = 5
    longest_line = []
    current_line = []
    prev_y = corners_sorted[0][0][1]

    for corner in corners_sorted:
        y = corner[0][1]
        if abs(y - prev_y) < deviation_threshold: # Eğer iki nokta arasındaki y mesafesi belirli bir eşik değerinden küçükse aynı hizada kabul et
            current_line.append(corner)
        else:
            if len(current_line)> len(longest_line):
                longest_line = current_line
            current_line = [corner]
        prev_y = y
    # Döngü bittiğinde en uzun çizgi en son kısımdaysa kontrol et
    if len(current_line)> len(longest_line):
        longest_line = current_line
    # En uzun Çizgideki nokta sayısını hesapla
    point_count = len(longest_line)
    floor_count = len(corners_sorted)

    # Köşeleri resme çiz
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(image, (x, y), 3, 255, -1)

    print("********************************")
    print("Tahmini Kat Sayısı: ", point_count)
    print("Threshold Değeri: ", deviation_threshold)
    print("********************************")
    print("Total Corner Sayısı: ", floor_count)

    cv2.imshow("Original Image: ", image)
    cv2.imshow("Canny Edges: ", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

