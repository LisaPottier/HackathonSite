#src : https://gis.stackexchange.com/questions/388952/getting-coordinate-grid-per-country

from shapely.geometry import MultiPolygon, Polygon, box, MultiPoint, Point
from shapely import wkt

def get_geometries(top_left, bottom_right, spacing=0.08):
    polygons = []
    points = []
    xmin = top_left[0]
    xmax = bottom_right[0]
    ymax = top_left[1]
    y = bottom_right[1]
    i = -1
    while True:
        if y > ymax:
            break
        x = xmin

        while True:
            if x > xmax:
                break
            
            #components for polygon grid
            polygon = box(x, y, x+spacing, y+spacing)
            polygons.append(polygon)

            #components for point grid
            point = Point(x, y)
            points.append(point)
            i = i + 1
            x = x + spacing

        y = y + spacing
    return polygons, points

polygons, points = get_geometries((-54.70398012112683, 5.837025464717242), (-51.47399965237683, 2.023485461146527), 0.5)

##country_geom is a shapely polygon with country boundaries
country_geom = wkt.loads('POLYGON((-53.93145206607949 5.7605147023226495,-53.42608097232949 5.552791060057871,-53.12945011295449 5.5090503435776865,-52.76690128482949 5.334055521388942,-52.27251651920449 4.863514113478214,-51.99785831607949 4.67739360408995,-51.78911808170449 4.6116920984983985,-51.63530948795449 4.173530887078694,-51.87700870670449 3.778975898208526,-52.23955753482949 3.230689015885577,-52.58013370670449 2.51748056877505,-52.95366886295449 2.1003399591609324,-53.25029972232949 2.232081655116072,-53.33819034732949 2.3418574130041816,-53.60186222232949 2.265015261624751,-53.78862980045449 2.3418574130041816,-54.15117862857949 2.133276451904325,-54.54668644107949 2.2979481194109233,-54.25005558170449 2.70405420446885,-54.17315128482949 3.142934314745993,-54.00835636295449 3.515838341318354,-54.17315128482949 3.877632205726407,-54.34893253482949 4.162573616058116,-54.42583683170449 4.567887712926,-54.48076847232949 4.983917747785059,-54.18413761295449 5.334055521388942,-53.93145206607949 5.7605147023226495))')

intersecting_polygons = []
intersecting_points = []
for polygon in polygons:
    if polygon.intersects(country_geom):
        intersecting_polygons.append(polygon)

for point in points:
    if country_geom.contains(point):
        intersecting_points.append(point)

polygon_grid = MultiPolygon(intersecting_polygons)
point_grid = MultiPoint(intersecting_points)

#grids are shapely geometries. You can output them as WKT format
print(point_grid.wkt)
print(polygon_grid.wkt)