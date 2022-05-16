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

polygons, points = get_geometries((-61.826840369996866, 16.512545933673646), (-61.164914100465616, 15.862358653505432), 0.1)

##country_geom is a shapely polygon with country boundaries
country_geom = wkt.loads('POLYGON((-61.471452024195784 16.506808285565533,-61.422013547633284 16.475205092458523,-61.400040891383284 16.44096248164485,-61.400040891383284 16.385634740448957,-61.383561399195784 16.346105301487647,-61.334122922633284 16.338198453100713,-61.259965207789534 16.30656786215828,-61.221513059352034 16.267022439672434,-61.17344787380516 16.244609829838804,-61.24211242458641 16.25383886111992,-61.306657102320784 16.243291361432846,-61.372575071070784 16.224831875889052,-61.449479367945784 16.20637065955028,-61.46527221462547 16.198787873264948,-61.49479797146141 16.201755085234467,-61.542863157008284 16.230106191304277,-61.575822141383284 16.2327432960156,-61.584061887477034 16.195820616654537,-61.581315305445784 16.153614805776485,-61.551102903102034 16.092928177921163,-61.562089231227034 16.048060918297846,-61.606034543727034 15.979420859005463,-61.658219602320784 15.958296097620249,-61.702164914820784 15.945091990458014,-61.729630735133284 15.98734206972124,-61.762589719508284 16.040142116513703,-61.781815793727034 16.12723159870832,-61.792802121852034 16.21428282123131,-61.806535032008284 16.28020513312189,-61.790055539820784 16.34346972090907,-61.751603391383284 16.356647268179,-61.72551086208641 16.355988411934387,-61.696671750758284 16.335562765881125,-61.652726438258284 16.321065851089696,-61.60466125271141 16.30557932381916,-61.589555051539534 16.27559129113501,-61.542863157008284 16.301295600033317,-61.529130246852034 16.34083410477839,-61.493424680445784 16.346105301487647,-61.501664426539534 16.390904726914258,-61.531876828883284 16.41461790105245,-61.531876828883284 16.467303488192695,-61.471452024195784 16.506808285565533))')

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