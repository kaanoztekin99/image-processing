import cv2
import numpy as np

# Resmi yükle
image_path = "bina.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Köşeleri bul
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

# Köşelere nokta çiz
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (x, y), 3, (255, 0, 0), -1)

# Köşeleri x ekseni boyunca gruplayarak çizgiler oluştur
threshold = 10  # x ekseni boyunca birleştirme eşiği (esneklik)
lines = []  # Çizgileri depolamak için bir liste
connected_points = []  # Birleştirilen noktaları depolamak için bir liste
for i in range(len(corners)):
    connected = []  # Her köşe için birleştirilen noktaları depolamak için bir liste
    for j in range(i + 1, len(corners)):
        x1, y1 = corners[i].ravel()
        x2, y2 = corners[j].ravel()
        if abs(x2 - x1) < threshold:  # x ekseni boyunca yakın olan köşeleri birleştir
            line_length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Çizginin uzunluğunu hesapla
            lines.append(((x1, y1), (x2, y2), line_length))  # Çizgiyi listeye ekle
            connected.append((x2, y2))  # Birleştirilen noktayı listeye ekle
    connected_points.append(connected)  # Her köşe için birleştirilen noktaları listeye ekle

# En uzun çizgiyi bul
longest_line = max(lines, key=lambda x: x[2])

# En uzun çizgideki doğru noktaları belirle
longest_line_points = [point for point_list in connected_points for point in point_list if tuple(point) == longest_line[0] or tuple(point) == longest_line[1]]

# En uzun çizgiyi yeşil renkte çiz
cv2.line(image, longest_line[0], longest_line[1], (0, 255, 0), 2)

# En uzun çizgideki birleştirilen nokta sayısını bul
num_points_connected = len(longest_line_points)
print(f"En uzun çizgide {num_points_connected} nokta birleştirildi.")

# Birleştirilen noktaları göster
connected_image = np.zeros_like(gray)
for connected in connected_points:
    for point in connected:
        cv2.circle(connected_image, tuple(point), 3, 255, -1)

# En uzun çizgiye ait olan doğru noktaları göstermek için yeni bir görüntü oluştur
correct_points_image = np.zeros_like(connected_image)
for point in longest_line_points:
    cv2.circle(correct_points_image, tuple(point), 3, 255, -1)

# Sonuçları göster
cv2.imshow("Connected Corners", image)
cv2.imshow("Connected Points", connected_image)
cv2.imshow("Correct Points", correct_points_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
