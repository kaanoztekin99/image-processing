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
threshold = 1  # x ekseni boyunca birleştirme eşiği
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        x1, y1 = corners[i].ravel()
        x2, y2 = corners[j].ravel()
        if abs(x2 - x1) < threshold:  # x ekseni boyunca yakın olan köşeleri birleştir
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Sonuçları göster
cv2.imshow("Connected Corners", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
