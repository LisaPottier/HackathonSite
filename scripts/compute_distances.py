import csv, os
from compute_min_distance import distance_min

# Remove the previous results
os.remove("../results/distances_to_DGFiP_facilities.csv")

# Main array
distances = [["latitude","longitude", "distance"]]

path = "../[CSV]-Datasets/territories/"
dirs = os.listdir(path)

with open ('../results/distance_to_DGFiP_facilities.csv', 'w', newline='') as writtenCsv:
    for file in dirs:
        with open (path+file, newline='') as readCsv:
            print(file, " opened.")
            territory_grid = csv.DictReader(readCsv)
            for point in territory_grid:
                    latitude = float(point['lat'])
                    longitude = float(point['lon'])
                    distance = distance_min(latitude, longitude)
                    print(file, " : ", [latitude, longitude, distance])
                    distances.append([latitude, longitude, distance])
        F_writer = csv.writer(writtenCsv, delimiter=',')
        F_writer.writerows(distances)
        print(file, "computed and saved.")
writtenCsv.close()
