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

polygons, points = get_geometries((-4.988986826203816, 51.38642429657206), (8.721950673796183, 41.95242730865379), 0.05)

##country_geom is a shapely polygon with country boundaries
country_geom = wkt.loads('POLYGON((2.51240525190894 51.130989395235694,1.5456083769089402 50.93754300773787,1.2819365019089402 50.042908736991606,-0.03642287309105985 49.67461594797885,-0.43193068559105985 49.38940180533386,-1.1350556855910598 49.53221690570206,-1.5305634980910598 49.78823584482863,-2.01396193559106 49.61770623680294,-1.7063447480910598 48.8429043480013,-2.76103224809106 48.69808780246383,-3.15654006059106 48.90071404054666,-3.90361037309106 48.756064542939185,-4.82646193559106 48.61099734185345,-4.69462599809106 47.87938656095683,-4.12333693559106 47.672658799314426,-3.46415724809106 47.61344273362006,-2.89286818559106 47.46510884415463,-2.23368849809106 47.01758789319609,-1.9700166230910598 46.44529766606488,-1.3987275605910598 46.080721039442146,-1.3987275605910598 45.40603145861401,-1.3547822480910598 44.691954093274994,-1.3547822480910598 44.00058229658804,-1.8381806855910598 43.49264611551036,-1.9260713105910598 43.14094062016068,-0.8713838105910598 42.948243478925455,0.27119431440894015 42.625736963434065,1.2379911894089402 42.43142680148212,3.43525681440894 42.26904006158878,3.25947556440894 42.88387660757947,3.96260056440894 43.36498874744341,5.19306931440894 43.14094062016068,6.29170212690894 42.88387660757947,6.86299118940894 43.26906905143226,7.82978806440894 43.778890578483036,7.87373337690894 44.47285671839308,7.12666306440894 44.47285671839308,6.86299118940894 45.09665845484468,7.17060837690894 45.529308817706955,7.12666306440894 45.928098450839,6.77510056440894 46.44529766606488,6.64326462690894 46.98761872360023,7.12666306440894 47.28655407647338,7.87373337690894 47.761357055517706,7.96162400190894 48.26113021299408,8.26924118940894 49.016133082267416,7.65400681440894 49.30351290133691,6.64326462690894 49.589226431028216,5.85224900190894 49.84494607445823,4.92939743940894 50.15566516304368,3.91865525190894 50.54822476234497,2.51240525190894 51.130989395235694))')

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

create_csv(point_grid,"france.csv")