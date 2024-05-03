def read_file(filename):
    with open(filename, 'r') as file:
        matrix = []
        for line in file:
            new_line = list(map(int, line.split()))
            matrix.append(new_line)
    return matrix

def out_file(filename, value):
    with open(filename, 'w') as file:
        file.write(str(value))

def prim(matrix):
    """
    Algo Prima
    Args:
    matrix -- adjacency matrix , where [i][j] is the weight of the rib

    Return:
    minimal_spanning_tree - list with tuple, where 1 element is neighbor
    2 element is where we can go
    3 element is value of edge
    """
    n = len(matrix)
    visited = {2} 
    minimal_spaning_tree = []

    while len(visited) < n:
        min_weight = float('inf')
        min_edge = None

        for vertex in visited:
            for neighbor in range(n):
                if (neighbor not in visited) and (matrix[vertex][neighbor] < min_weight):
                    min_weight = matrix[vertex][neighbor]
                    min_edge = (vertex, neighbor, min_weight)
        if min_edge:
            minimal_spaning_tree.append(min_edge)
            visited.add(min_edge[1])
    return minimal_spaning_tree


def count_lengh_ethernet(graph):
    """
    args:
    graph - accept minimal spaning tree

    return:
    min_lengh - counts value of edges is MST
    """
    min_lengh = 0
    value_in_graph = 2
    for value in graph:
        min_lengh += value[value_in_graph]

    return min_lengh

def find_shortest_lengh_ethernet(file_in, file_out):
    if len(file_in) > 100 and len(file_in) < 0:
        return 'island must to be from 1 to 100'
    matrix = read_file(file_in)
    minimal_lengh_conection = prim(matrix)
    out_file(file_out, count_lengh_ethernet(minimal_lengh_conection))

file = 'island.csv'
out = 'island.out'
matrix = read_file(file)
print(matrix)
print(prim(matrix))
out_file(out, count_lengh_ethernet(prim(matrix)))
