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

polygons, points = get_geometries((8.450904109851427, 43.05188570528878), (9.692359187976427, 41.293342313219405), 0.5)

##country_geom is a shapely polygon with country boundaries
country_geom = wkt.loads('POLYGON((9.340796687976427 43.00777800816221,9.467139461413927 43.01982763783897,9.516577937976427 42.68962046356614,9.494605281726427 42.61689968430008,9.560523250476427 42.44688725538585,9.571509578601427 42.17471934252152,9.505591609851427 42.02391341541526,9.423194148913927 41.84820201012155,9.409688597881205 41.70760058608043,9.209415468723483 41.34437549708576,9.032374607269622 41.46731360897063,8.894415699980192 41.50401683811126,8.756456792690761 41.55714338359376,8.819855538533039 41.65439489248359,8.677942709402151 41.690126870956774,8.679761582390375 41.81887038330417,8.584522375241823 41.887746534533925,8.62475685156972 42.000788003501626,8.672266819850512 42.08781726396734,8.514601209537096 42.212714419797635,8.616750457660265 42.28320702914808,8.524418094531603 42.359043797699364,8.680329540149279 42.5185411592347,8.80538485325963 42.61033042939886,9.000563838855333 42.68053501642669,9.14922259129674 42.76427264813555,9.292731502429552 42.70576908870277,9.316077449695177 42.82272101196535,9.340796687976427 43.00777800816221))')

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