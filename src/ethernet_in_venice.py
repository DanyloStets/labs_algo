from red_black_priority_queue import RedBlackTree
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

def pop_min(rb_tree):
    min_node = rb_tree.minimum(rb_tree.root)
    key = min_node.key
    value = min_node.value
    rb_tree.delete(key)
    return value

def prim(main_matrix, start_vertex):
    len_main_matrix = len(main_matrix)
    minimal_spaning_tree = []
    visited_vertex = set()
    prior_queue = RedBlackTree()

    visited_vertex.add(start_vertex)
    for v in range(len_main_matrix):
        if main_matrix[start_vertex][v] > 0:
            prior_queue.insert(main_matrix[start_vertex][v], (start_vertex, v))

    while prior_queue.root != prior_queue.NIL:
        (u, v) = pop_min(prior_queue)
        if v not in visited_vertex:
            minimal_spaning_tree.append((u, v, main_matrix[u][v]))
            visited_vertex.add(v)

            for neighbor in range(len_main_matrix):
                if (main_matrix[v][neighbor] > 0) and (neighbor not in visited_vertex):
                    prior_queue.insert(main_matrix[v][neighbor], (v, neighbor))
    return minimal_spaning_tree

def count_length_ethernet(graph):
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
    out_file(file_out, count_length_ethernet(minimal_lengh_conection))

file = 'island.csv'
out = 'island.out'
matrix = read_file(file)
print(matrix)
print(prim(matrix))
out_file(out, count_length_ethernet(prim(matrix)))
