import networkx as nx
import matplotlib.pyplot as plt


edges = [
    (0, 1, {'weight': 60}),
    (0, 3, {'weight': 1}),
    (0, 4, {'weight': 1}),
    (0, 6, {'weight': 60}),
    (1, 2, {'weight': 2}),
    (1, 7, {'weight': 5}),
    (2, 3, {'weight': 2}),
    (2, 8, {'weight': 5}),
    (3, 9, {'weight': 5}),
    (4, 5, {'weight': 2}),
    (4, 10, {'weight': 5}),
    (5, 6, {'weight': 2}),
    (5, 11, {'weight': 5}),
    (6, 12, {'weight': 5})
]


def build_graph():
    g = nx.Graph()
    g.add_nodes_from(range(12))
    g.add_edges_from(edges)
    return g


def draw_graph(g):
    #subax1 = plt.subplot(121)
    nx.draw(g, with_labels=True, font_weight='bold')
    #subax2 = plt.subplot(122)
    nx.draw_shell(g, with_labels=True, font_weight='bold')
    plt.show()


if __name__ == '__main__':
    campus_map = build_graph()
    # draw_graph(campus_map)
    print(nx.shortest_path(campus_map, 7, 12, 'weight'))
    print(nx.shortest_path(campus_map, 0, 10, 'weight'))
    print(nx.shortest_path(campus_map, 2, 11, 'weight'))
    print(nx.shortest_path(campus_map, 0, 6, 'weight'))
    print(nx.shortest_path(campus_map, 1, 9, 'weight'))
    print(nx.shortest_path(campus_map, 12, 11, 'weight'))


