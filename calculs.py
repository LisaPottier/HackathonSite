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