import math

def haversine(lat1, lon1, lat2, lon2):
    # Umwandlung von Grad in Radianten
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine-Formel
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Radius der Erde in Kilometern. Verwenden Sie 3956 für Meilen
    r = 6371

    return c * r

if __name__ == '__main__':
    # Beispielaufruf der Funktion
    dist = haversine(48.8566, 2.3522, 40.7128, -74.0060)  # Distanz zwischen Paris und New York
    print(f"Distanz: {dist} km")