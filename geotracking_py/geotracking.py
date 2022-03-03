import time
import networkx

import nodemap
import msgparse

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def cgrab(i):
    nc = msgparse.get_coords()
    if nc != ():
        coords.append(nc)
        pax.cla()
        pax.plot(coords(0), coords(1), color='red')


if __name__ == '__main__':
    # load the node map
    begin = time.perf_counter()
    campus_map = networkx.Graph()
    nodemap.load_nodes(campus_map, "mapdata/nodes.csv")
    nodemap.load_edges(campus_map, "mapdata/edges.csv")
    nodeload = time.perf_counter()
    print(f'loaded map in {nodeload-begin} seconds')

    # get coords
    coords = ([], [])

    # prep the figure
    matplotlib.use('qtagg')
    fig, ax = plt.subplots()
    img = plt.imread("mapdata/gmap.png")
    ax.imshow(img, extent=[-121.3184, -121.3064, 37.9744, 37.9855])
    for n in list(campus_map.nodes):
        plt.scatter(float(campus_map.nodes[n]['lng']), float(campus_map.nodes[n]['lat']), color='blue')

    # draw lines
    for e in list(campus_map.edges):
        x = [float(campus_map.nodes[e[0]]['lng']), float(campus_map.nodes[e[1]]['lng'])]
        y = [float(campus_map.nodes[e[0]]['lat']), float(campus_map.nodes[e[1]]['lat'])]
        plt.plot(x, y, color='blue')
    pax = fig.add_axes(ax.get_position(), frameon=False)
    ani = FuncAnimation(fig, cgrab, interval=1)
    plt.show()


    # coords = msgparse.get_route()
    # coords = (-121.313960, 37.981323)
    # chambers_alt, library, classroom_olson
    '''coords = ([
        -121.311247,
        -121.309482,
        -121.311729
        ],[
        37.979507,
        37.980006,
        37.976124
        ])
    '''


