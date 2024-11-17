# Noktaların tanımlanması
points = [(2, 3), (4, 5), (1, 1), (7, 8), (2, 9)]

# Öklid Mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2) ** 0.5

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonuçların yazdırılması
print(f"Tüm mesafeler: {distances}")
print(f"Minimum mesafe: {min_distance}")
