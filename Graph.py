# ---------------------------------------- #
#           Algorithmic Project            #
#  Algorithmic - 8INF870 - Imène Benkalai  #
#        Claire SABA - SABC14529902        #
# ---------------------------------------- #

"""The following functions were taken from my precedent work for the course
'Méthodes de Résolutions de Problèmes' that I followed at the
'Institut Supérieure d'Informatique, de Modélisation et de leurs Applications'
(ISIMA) in France for my second year of bachelor's degree (2018-2019). This
course was provided by ISIMA's teacher Christian Laforest."""

import random

def extract_graph_from_file(file):
    """Takes a file name as input and extracts the graph inside it.
    The file is composed of n lines, where n is the total number of vertices.
    Each line is of the form u:v1:v2:...:vk where u is a vertex and the
    vi's are its neighbors. If u has no neighbor, the corresponding line is u:
    This function returns a dictionary representing the graph:
    Its keys are vertices and its values are the sets of neighbors
    of each vertex."""
    graph = {}
    with open(file, "r", encoding="utf8") as f:
        for line in f:
            l = line.strip().split(":")
            key = l[0]
            if len(l) == 1:
                graph[key] = set()
            else:
                graph[key] = set(l[1:])
    return graph


def write_graph_in_file(graph, file):
    """Takes a graph and a file name as inputs and write the graph in the file."""
    with open(f"{file}", "w", encoding='utf8') as f:
        for u in set_of_vertices(graph):
            s = str(u) + ":"
            for v in graph[u]:
                s += str(v) + ":"
            f.write(s[:-1] + '\n')


def set_of_vertices(graph):
    """Returns the set of vertices of the graph."""
    return set(graph.keys())


def set_of_neighbors(graph, u):
    """Returns the set of neighbors of vertex u in the graph."""
    return graph[u]


def degree_of(graph, u):
    """Returns the numbers of neighbors of vertex u in the graph."""
    return len(set_of_neighbors(graph, u))


def are_neighbors(graph, u, v):
    """Boolean function returning True if u and v are neighbors in the graph.
     Returns False otherwise."""
    return u in set_of_neighbors(graph, v) and v in set_of_neighbors(graph, u)


def number_of_vertices(graph):
    """Returns the number of vertices of the graph."""
    return len(graph)


def number_of_edges(graph):
    """Returns the number of edges of the graph.
    We suppose that it is NON directed."""
    nb_of_edges = 0
    set_of_vertices_treated = set()
    for u in set_of_vertices(graph):
        for v in set_of_neighbors(graph, u):
            if v not in set_of_vertices_treated and are_neighbors(graph, u, v):
                nb_of_edges += 1
        set_of_vertices_treated.add(u)
    return nb_of_edges


def complete_graph(n):
    """Constructs a complete graph of n vertices and write it in file 'complete_n'."""
    with open(f"complete_{n}", "w", encoding='utf8') as f:
        for u in range(1, n + 1):
            s = str(u) + ":"
            for v in range(1, n + 1):
                if u != v:
                    s += str(v) + ":"
            f.write(s[:-1] + '\n')


def nul_graph(n):
    """Constructs a nul graph of n vertices and write it in file 'nul_n'."""
    with open(f"nul_{n}", "w", encoding='utf8') as f:
        for u in range(1, n + 1):
            s = str(u) + ":"
            f.write(s[:-1] + '\n')


def random_graph(n):
    """Constructs a random non oriented graph of n vertices and write it in file 'graph_n'."""
    graph = {}
    for u in range(1, n + 1):
        graph[u] = set()

    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            random_number = random.random()
            if random_number < 0.5:
                graph[u].add(v)
                graph[v].add(u)

    write_graph_in_file(graph, f"graph_{n}")

    return graph

