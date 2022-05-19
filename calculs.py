import math

#source : https://janakiev.com/blog/gps-points-distance-python/ 

#calcul de la distance entre deux points GPS
def haversine(coord1, coord2):
    R = 6372800  # Rayon de la Terre (en mètre)
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))

#exemples avec des villes 
london_coord = 51.5073219,  -0.1276474
cities = {
    'berlin': (52.5170365,  13.3888599),
    'vienna': (48.2083537,  16.3725042),
    'sydney': (-33.8548157, 151.2164539),
    'madrid': (40.4167047,  -3.7035825) 
}

for city, coord in cities.items():
    distance = haversine(london_coord, coord)
    print(city, distance)