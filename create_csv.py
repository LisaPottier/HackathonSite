import csv

def create_csv(point_grid,name):
    # Main array
    L = [["point"]]

    # Lists all the files and directories
    # Get the size and convert to Ko
    for point in point_grid:
        L.append([point])
        print(point)
    # CSV commands
    with open (name, 'w', newline='') as F:
        F_writer = csv.writer(F, delimiter=',')
        F_writer.writerows(L)
        print("csv saved")