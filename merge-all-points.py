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

# Köşeleri y ekseninde gruplayarak çizgiler oluştur
corners_sorted = sorted(corners, key=lambda x: x[0][1])  # Y koordinatına göre sırala
for i in range(len(corners_sorted) - 1):
    x1, y1 = corners_sorted[i].ravel()
    x2, y2 = corners_sorted[i + 1].ravel()
    if abs(y2 - y1) < 10:  # Y ekseninde yakın olan köşeleri birleştir
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Sonuçları göster
cv2.imshow("Connected Corners", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
