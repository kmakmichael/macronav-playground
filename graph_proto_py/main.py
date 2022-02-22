import csv
import sys
import networkx as nx
import matplotlib.pyplot as plt


def load_nodes(g, csv_file):
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            g.add_nodes_from([(row['name'], {"lat": row['lat'], "lng": row['lng']})])


def load_edges(g, csv_file):
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            g.add_edge(row['a'], row['b'])


def draw_graph(g):
    # draw nodes
    fig = plt.figure()
    for n in list(g.nodes):
        plt.scatter(float(g.nodes[n]['lng']), float(g.nodes[n]['lat']), color='blue')

    # draw lines
    for e in list(g.edges):
        x = [float(g.nodes[e[0]]['lng']), float(g.nodes[e[1]]['lng'])]
        y = [float(g.nodes[e[0]]['lat']), float(g.nodes[e[1]]['lat'])]
        plt.plot(x, y, color='blue')

    plt.show()


if __name__ == '__main__':
    campus_map = nx.Graph()
    load_nodes(campus_map, "nodes.csv")
    load_edges(campus_map, "edges.csv")
    # draw_graph(campus_map)
    print(nx.shortest_path(campus_map, sys.argv[1], sys.argv[2]))


