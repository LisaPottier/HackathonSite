from calculDistanceMin import distance_min
import csv, os

# Main array
L = [["latitude","longitude", "distance"]]

os.remove("csvDistance.csv")

path = "csv/"
dirs = os.listdir(path)

# CSV commands
with open ('csvDistance.csv', 'w', newline='') as writtenCsv:
    for file in dirs:
        with open ('csv/'+file, newline='') as readCsv:
            print(file)
            pointsTerritoire = csv.DictReader(readCsv)
            for point in pointsTerritoire:
                    current_lon = float(point['lon'])
                    current_lat = float(point['lat'])
                    distance=distance_min(current_lon, current_lat)
                    print([current_lon, current_lat, distance])
                    L.append([current_lon, current_lat, distance]) 
                    print("happen ok")         
        F_writer = csv.writer(writtenCsv, delimiter=',')
        F_writer.writerows(L)
        print("csv saved")
writtenCsv.close()