# ---------------------------------------- #
#           Algorithmic Project            #
#  Algorithmic - 8INF870 - Imène Benkalai  #
#        Claire SABA - SABC14529902        #
# ---------------------------------------- #

import time
from Graph import *


def is_stable(graph, set_s):
    """Boolean function taking as input a graph and a set of vertices.
    It returns True if this set is a stable of the graph (there is no edge
    between vertices of this set in the graph).
    Returns False otherwise."""
    set_of_vertices_left = set_s.copy()
    for u in set_s:
        set_of_vertices_left.discard(u)
        for v in set_of_vertices_left:
            if are_neighbors(graph, u, v):
                return False
    return True


def can_form_stable(graph, set_s, u):
    """Boolean function taking as input a graph, a stable of the graph and a vertex.
    It returns True if the vertex can be added to the stable and the resulting set
    is still a stable of the graph.
    Returns False otherwise."""
    for v in set_s:
        if are_neighbors(graph, u, v):
            return False
    return True


def exact_method_sub_function(graph, set_s, vertices_left, result, begin_time):
    """Sub recursive function that find a stable in the graph from the set given and
    the vertices left."""
    for u in vertices_left:
        # If a bigger stable can not be found with the remaining vertices or if there
        # is only one vertex left, the loop is stopped.
        nb_vertices = len(vertices_left) + len(set_s)
        if nb_vertices <= 1 or nb_vertices <= len(result) or time.time() - begin_time > 3600:
            break

        # Check if the vertex can form a stable with the set and, if it can, add it
        # to the set.
        if can_form_stable(graph, set_s, u):
            set_s.add(u)

            # If the new set is bigger than the stocked result, stock it as the new
            # result.
            if len(set_s) > len(result):
                result = set_s.copy()

            # Repeat the function with the current set and the vertices left.
            copy_vertices_left = vertices_left.copy()
            copy_vertices_left.discard(u)
            result = exact_method_sub_function(graph, set_s, copy_vertices_left, result, begin_time)

            # Remove the vertex from the set.
            set_s.discard(u)

    return result


def exact_method(graph, begin_time):
    """Method to find a maximum stable in the graph.
    This method return an exact solution, meaning that there does not exist a bigger
    stable in the graph than the one found.
    Return the stable found."""
    nb_vertices = number_of_vertices(graph)
    nb_edges = number_of_edges(graph)
    vertices = set_of_vertices(graph).copy()
    first_vertex = next(iter(vertices))

    # If the graph does not have any edge, the maximum stable is all the vertices.
    if nb_edges == 0:
        return vertices
    # If the graph has the maximum number of edges (complete graph), a maximum
    # stable is a vertex.
    if nb_edges == nb_vertices*(nb_vertices-1)/2:
        return set(first_vertex)

    return exact_method_sub_function(graph, set(), vertices, set(), begin_time)


def approximate_method(graph, begin_time):
    """Method to find a maximum stable in the graph.
    This method return an approximate solution, meaning that a bigger stable than the
    one found might exist in the graph.
    Return the stable found."""
    nb_vertices = number_of_vertices(graph)
    nb_edges = number_of_edges(graph)
    vertices = set_of_vertices(graph).copy()
    first_vertex = next(iter(vertices))

    # If the graph does not have any edge, the maximum stable is all the vertices.
    if nb_edges == 0:
        return vertices
    # If the graph has the maximum number of edges (complete graph), a maximum
    # stable is a vertex.
    if nb_edges == nb_vertices * (nb_vertices - 1) / 2:
        return set(first_vertex)

    result = set()
    result_size = 0
    previous_pop = []
    next_pop = []

    # Create the first population with one set for each vertex.
    for u in vertices:
        tmp = set()
        tmp.add(u)
        previous_pop.append(tmp)

    # Number of iteration done.
    iteration = 1

    # The loop stops when the stable of the maximum size is found (the number of
    # vertices minus 1 when the stable is not nul) or when the maximum number of
    # iterations has been done.
    while result_size < nb_vertices and iteration <= 1000 and time.time() - begin_time <= 3600:
        sets_left = len(previous_pop)
        copy_previous_pop = previous_pop.copy()

        while sets_left > 0:
            # Select two sets in the previous population
            first_set = random.choice(previous_pop)
            previous_pop.remove(first_set)
            second_set = random.choice(copy_previous_pop)
            copy_previous_pop.remove(second_set)
            sets_left -= 1

            # Create a child of the two sets as the union of them.
            # If the child is a stable of the graph, add it to the next population.
            # If not, add its two parents to the next population.
            child_set = first_set.union(second_set)
            if is_stable(graph, child_set) and child_set not in next_pop:
                next_pop.append(child_set)

                # Stock the child as the new result if it is bigger than the previous
                # result.
                if len(child_set) > result_size:
                    result = child_set.copy()
                    result_size = len(result)
            else:
                if first_set not in next_pop:
                    next_pop.append(first_set)
                if second_set not in next_pop:
                    next_pop.append(second_set)

        # Stock the next population as the previous one and reset it for the next
        # iteration.
        previous_pop = next_pop.copy()
        next_pop = []
        iteration += 1

    return result

