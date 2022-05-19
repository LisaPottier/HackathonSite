from calculs import haversine 
import os, sys, csv
import string


def distance_min(struct_lat, struct_lon):
    distance_min=10000

    with open('coordonnees-structures.csv', newline='') as csvfile:
        pointsTerritoire = csv.DictReader(csvfile)
        for point in pointsTerritoire:
            if(point['geocodage']!= ''):
                current_coord = point['geocodage'].partition(',')
                current_lat = float(current_coord[0])
                current_lon = float(current_coord[2])
                distance= haversine(current_lat, current_lon, struct_lat, struct_lon)
                if(distance < distance_min):
                    distance_min=distance
    return distance_min

print(distance_min(48.579933,7.756877))
#'coordonnees-des-structures-dgfip.csv'