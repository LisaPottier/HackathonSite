#src : https://gis.stackexchange.com/questions/388952/getting-coordinate-grid-per-country

from shapely.geometry import MultiPolygon, Polygon, box, MultiPoint, Point
from shapely import wkt
from create_csv import create_csv

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

polygons, points = get_geometries((55.20282193720966, -20.847806137214857), (55.85925504267841, -21.413983021238945), 0.05)

##country_geom is a shapely polygon with country boundaries
country_geom = wkt.loads('POLYGON((55.44452115595966 -20.868338821349322,55.51043912470966 -20.888868700719556,55.56537076533466 -20.888868700719556,55.63128873408466 -20.904264268265702,55.69446012080341 -20.950441487730284,55.71093961299091 -21.02224439511291,55.76587125361591 -21.10682486864672,55.82904264033466 -21.147816253894607,55.82629605830341 -21.20416088691325,55.80157682002216 -21.265603250414667,55.80432340205341 -21.337253606610325,55.75213834345966 -21.365392394538183,55.66699430049091 -21.378180966227546,55.58185025752216 -21.378180966227546,55.52417203486591 -21.370507957254535,55.47198697627216 -21.34492835721305,55.40606900752216 -21.311668204787214,55.35388394892841 -21.283519114031876,55.32641812861591 -21.270722291163118,55.27972623408466 -21.21696349017349,55.27972623408466 -21.152939379987938,55.21930142939716 -21.076073897781765,55.21655484736591 -21.0350627083921,55.23578092158466 -20.994040226949597,55.27972623408466 -20.976089345076083,55.28521939814716 -20.94274627300852,55.35113736689716 -20.901698450030736,55.44452115595966 -20.868338821349322))')

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

create_csv(point_grid,"reunion.csv")