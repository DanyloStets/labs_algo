def read_input_matrix(path):
    """
    Reads the input matrix from a file

    """
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read().strip().split("\n")
        cols, rows = map(int, data[0].split())
        sneaky_way = [list(data[i]) for i in range(1, len(data))]
    return rows, cols, sneaky_way

def read_output(path):
    """
      Reads the output from a file

    """
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
    return int(data)

def initialize_first_column(len_matrix, len_matrix_row):
    matrix_length = [[0] * len_matrix_row for _ in range(len_matrix)]

    for i in range(len_matrix):
        matrix_length[i][0] = 1

    return matrix_length

def count_ways(len_matrix, len_matrix_row, main_matrix):
    matrix_col = initialize_first_column(len_matrix, len_matrix_row)

    for j in range(1, len_matrix_row):
        # Temporary array to store the sum of ways to reach any letter
        sum_prev_col = {}
        new_letters = set()

        for i in range(len_matrix):
            letter = main_matrix[i][j - 1]
            if letter not in new_letters:
                sum_prev_col[letter] = matrix_col[i][j - 1]
                new_letters.add(letter)

        for i in range(len_matrix):
            matrix_col[i][j] = matrix_col[i][j - 1]
            letter = main_matrix[i][j]
            if letter in sum_prev_col:
                matrix_col[i][j] += sum_prev_col[letter]

    return matrix_col[0][len_matrix_row - 1] + matrix_col[len_matrix - 1][len_matrix_row - 1]

# main_matrix = [['a', 'a', 'b'],
#         ['c', 'a', 'a'],
#         ['d', 'e', 'a']]
# print(count_ways(3, 3, main_matrix))