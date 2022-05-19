from calculDistanceMin import distance_min
import csv, os

# Main array
L = [["latitude","longitude", "distance"]]

os.remove("csvDistance.csv")

# CSV commands
with open ('csvDistance.csv', 'w', newline='') as writtenCsv:
    with open ('csvTerritoire/test.csv', newline='') as readCsv:
        pointsTerritoire = csv.DictReader(readCsv)
        for point in pointsTerritoire:
            if(point['geocodage']!= ''):
                current_coord = point['geocodage'].partition(',')
                current_lat = float(current_coord[0])
                current_lon = float(current_coord[2])
            #current_lon = float(point['longitude'])
            #current_lat = float(point['latitude'])
                distance=distance_min(current_lon, current_lat)
                print([current_lon, current_lat, distance])
                L.append([current_lon, current_lat, distance]) 
                print("happen ok")         
        F_writer = csv.writer(writtenCsv, delimiter=',')
        F_writer.writerows(L)
        print("csv saved")
writtenCsv.close()