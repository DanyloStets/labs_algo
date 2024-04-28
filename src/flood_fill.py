def read_file(cur_file):
        # opening file
        # current_file = open(file, 'r', encoding="utf-8")

        with open(cur_file, 'r', encoding='utf-8') as current_file:
            list_resourse = list(current_file.readline().split(','))
            tuple_resourse = list(current_file.readline().split(','))
            recolour = current_file.readline().strip()
            main_matrix = current_file.readlines()           
        # assign values

        current_file.close()
        return list_resourse, tuple_resourse, recolour, main_matrix

def flood_fill_recolor(cur_file, file_result):
    list_resourse, tuple_resourse, recolour, main_matrix = read_file(cur_file)
    main = [line.strip().split(',') for line in main_matrix]

    width = int(list_resourse[0])
    height = int(list_resourse[1])
    tuple_resourse[1], tuple_resourse[0] = int(tuple_resourse[1]), int(tuple_resourse[0])
    pos = tuple(tuple_resourse)
    color_change = str(recolour)

    graph = change_colour(pos, color_change, main, width, height)

    return out_file(graph, file_result)

def out_file(graph, file_result):
      with open(file_result, 'w', encoding="utf-8") as current_output:
            for i in graph:
                current_output.write(str(i))
                current_output.write(str('\n'))

def change_position(pos):
        pos_x = pos[0] - 1
        pos_y = pos[1] - 1
        pos = (pos_x, pos_y)
        return pos

def change_colour(pos, colour_to_change, master_matrix, width, height):
        pos = change_position(pos)
        current_colour = what_colour_in_pos(pos, master_matrix, colour_to_change)
        visited = set()
        queue = []
        queue.append(pos)
        while queue:
            visited.add(queue[0])
            queue.pop(0)            
            queue = queue + find_neiborous(master_matrix, pos, current_colour, width, height)
            queue = is_element_was_visited(queue, visited)
            if queue:
                pos = queue[0]
            else:
                break
        master_matrix = recolor_matrix(visited, colour_to_change, master_matrix)
        return master_matrix

def recolor_matrix(visited_pos, colour_to_change, matrix):
        # recolor final graph
        for i in visited_pos:
            matrix[i[0]][i[1]] = colour_to_change
        return matrix

def is_element_was_visited(queue, visited):
        for i in visited:
            if i in queue:
                queue.remove(i)
            else:
                continue
        return queue

def what_colour_in_pos(pos, master_matrix, color_to_change):
        current_colour = master_matrix[pos[0]][pos[1]]
        if color_to_change == current_colour:
             return out_file
        return current_colour

def find_neiborous(master_matrix, position, colour, width, height):
        vortexs = []
        # verify from up -> right -> down -> left
        if (position[0] - 1 >= 0) and (master_matrix[(position[0] - 1)][position[1]] == colour):
            vortexs.append((position[0] - 1, position[1]))

        if (position[1] + 1 < width) and (master_matrix[position[0]][(position[1] + 1)] == colour):
            vortexs.append((position[0], position[1] + 1))

        if (position[0] + 1 < height) and (master_matrix[(position[0] + 1)][position[1]] == colour):
            vortexs.append((position[0] + 1, position[1]))

        if (position[1] - 1 >= 0) and (master_matrix[position[0]][(position[1] - 1)] == colour):
            vortexs.append((position[0], position[1] - 1))
        return vortexs

# matrix = [['W', 'W', 'G', 'R'],
#           ['Y', 'Y', 'G', 'R'],
#           ['W', 'Y', 'B', 'R'],
#           ['W', 'B', 'B', 'R']]

# print(flood_fill_recolor('tests\\resources\\index_pos_is_cur_colour.txt', 'tests\\resources\\index.txt'))