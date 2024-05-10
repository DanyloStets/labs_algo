from red_black_priority_queue import RedBlackTree

def read_input(filename):
    with open(filename, 'r') as file:
        vertexes, edges = map(int, file.readline().split())
        clients = list(map(int, file.readline().split()))
        connections = []
        for _ in range(edges):
            start, end, latency = map(int, file.readline().split())
            connections.append((start, end, latency))
    return vertexes, edges, clients, connections

def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))

def contains_key(tree, key):
    return tree.search(key) != tree.NIL 

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    rb_tree = RedBlackTree()  
    rb_tree.insert(0, [start]) 
    visited = set()
    while rb_tree.root != rb_tree.NIL:
        min_distance = rb_tree.root.key
        vertices = rb_tree.root.value
        current_vertex = vertices.pop(0)

        if not vertices:
            rb_tree.delete(min_distance)
        visited.add(current_vertex) 

        for neighbor, weight in graph[current_vertex]:
            if neighbor in visited:
                continue

            alternative_distance = distances[current_vertex] + weight
            if alternative_distance < distances[neighbor]:
                distances[neighbor] = alternative_distance

                if not contains_key(rb_tree, alternative_distance):
                    rb_tree.insert(alternative_distance, [neighbor])
                else:
                    rb_tree.search(alternative_distance).value.append(neighbor)
    return distances

def server_create(graph, clients, visited_server=[]):
    server = {}
    for from_vertx, index in graph.items():
        if from_vertx in clients:
            continue
        else:
            server[from_vertx] = []
            server[from_vertx].append((index))
    
    return server, visited_server

def server_set(visited_server=None, server=None):
    sub_server = {}
    if not server:
        return
    for key, value in server.items():
        if key in visited_server:
            continue
        else:
            visited_server.append(key)
            sub_server[key] = []
            sub_server[key].append(value)
            break
    return sub_server, server, visited_server

def routers_to_dict(conects):
    graph = {}
    for conection in conects:
        from_vertex, to_vertex, ping = conection
        if from_vertex not in graph:
            graph[from_vertex] = []
        if to_vertex not in graph:
            graph[to_vertex] = []
        graph[from_vertex].append((to_vertex, ping))
        graph[to_vertex].append((from_vertex, ping))
    return graph 

def find_shortest_ping(input_file, out_file):
    ver, ed, client, cont = read_input(input_file)
    graph = routers_to_dict(cont)
    set_serv, visited_server = server_create(graph, client)
    sub_server, server, visited_server = server_set(visited_server, set_serv)
    summary_list = []
    for key, value in sub_server.items():
        sub_server[key] = value[0]
        distanse = dijkstra(graph, key)
        summary = 0
        i = 0
        for values in distanse.values():
            summary += values
        summary_list.append(summary)
        sub_server, server, visited_server = server_set(visited_server, server)
    write_output(out_file, min(summary_list))


