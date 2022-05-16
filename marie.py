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

polygons, points = get_geometries((-61.341120507127954, 16.007296224022934), (-61.190058495409204, 15.865010986636145), 0.05)

##country_geom is a shapely polygon with country boundaries
country_geom = wkt.loads('POLYGON((-61.27601578076161 16.005852357326585,-61.259192965820205 15.998261906192665,-61.239966891601455 15.988030841975247,-61.2313838227538 15.981099823619436,-61.228980563476455 15.969547592788997,-61.21559097607411 15.955684035931865,-61.205977938964736 15.9510626371329,-61.19808151562489 15.937527927852766,-61.196021579101455 15.92036064178974,-61.20460464794911 15.900880598062338,-61.21662094433583 15.895927743646386,-61.230697177245986 15.882053943081655,-61.24923660595692 15.87082624812623,-61.27807571728505 15.867523865834674,-61.304854892089736 15.873468114997614,-61.32270767529286 15.884035236047874,-61.33163406689442 15.897243357494352,-61.33644058544911 15.92959958905447,-61.33644058544911 15.940824002543046,-61.3192744477538 15.953368192040896,-61.31790115673817 15.973833341936093,-61.304854892089736 15.980434556993949,-61.304854892089736 15.987695642001647,-61.29867508251942 15.99627658437745,-61.28974869091786 16.005517187241967,-61.27601578076161 16.005852357326585))')

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