import time
import networkx

import nodemap
import msgparse

if __name__ == '__main__':
    # load the node map
    begin = time.perf_counter()
    campus_map = networkx.Graph()
    nodemap.load_nodes(campus_map, "mapdata/nodes.csv")
    nodemap.load_edges(campus_map, "mapdata/edges.csv")
    nodeload = time.perf_counter()
    print(f'loaded map in {nodeload-begin} seconds')

    # get coords
    # coords = msgparse.get_coords()
    coords = (-121.313960, 37.981323)

    # draw the map
    drawstart = time.perf_counter()
    nodemap.draw_graph(campus_map, coords)
    drawend = time.perf_counter()
    print(f'drew graph in {drawend-drawstart} seconds')