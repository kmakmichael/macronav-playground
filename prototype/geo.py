import time
import math
import networkx
import pynmea2
import nodemap

# constants
TOL = 8e-6


def reached(pt, coords):
    d_x = abs(float(pt['lng']) - coords[0])
    d_y = abs(float(pt['lat']) - coords[1])
    distance = math.sqrt(d_x*d_x + d_y*d_y)
    return distance(pt, coords) < TOL


def navigate_path(g, a, b):
    coords = (37.980, -121.312) # pull these from the gps chip
    reached(b, coords)


if __name__ == '__main__':
    # load the node map
    begin = time.perf_counter()
    campus_map = networkx.Graph()
    nodemap.load_nodes(campus_map, "mapdata/nodes.csv")
    nodemap.load_edges(campus_map, "mapdata/edges.csv")
    nodeload = time.perf_counter()
    print(f'loaded map in {nodeload-begin} seconds')