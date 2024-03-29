zig_arr = [[1,2,3,4,5],
           [6,7,8,9,10],
           [11,12,13,14,15],
           [16,17,18,19,20],
           [21,22,23,24,25]]

# def go_right(rows, cols, result, arr):
#         cols += 1
#         result.append(arr[rows][cols])
#         return rows, cols

# def go_down(row, col, result, arr):
#     result.append(arr[row + 1][col])
#     row += 1
#     return row, col

# def zig_zag_in_arr(arr):
#     row, col = 0, 0
#     result = []

#     if (len(arr) * len(arr[0])) == 0:
#         print('fail')
#         return False
#     result.append(arr[0][0])


#     while len(result) != (len(arr) * len(arr[0])):
#         if col != (len(arr[0]) - 1):
#             row, col = go_right(row, col, result, arr)
#             if row > 0:
#                 while row != 0 and col != (len(arr[0]) - 1):
#                     row -= 1
#                     col += 1
#                     result.append(arr[row][col])
#             else:
#                 while col != 0 and row != (len(arr) - 1):
#                     row += 1
#                     col -= 1
#                     result.append(arr[row][col])
#         if row != (len(arr) - 1):
#             row, col = go_down(row, col, result, arr)
#             if col > 0:
#                 while col != 0 and row != (len(arr) - 1):
#                     row += 1
#                     col -= 1
#                     result.append(arr[row][col])
#             else:
#                 while row != 0 and col != (len(arr[0]) - 1):
#                     row -= 1
#                     col += 1
#                     result.append(arr[row][col])
#     return result

def go_up(row, col):
    row -= 1
    return row, col

def go_left(row, col):
    col -= 1
    return row, col

def zig_zag_in_arr(arr):

    row = (len(arr) - 1)
    col = (len(arr[0]) - 1)
    result = []
    result.append(arr[row][col])
    while len(result) != (len(arr) * len(arr[0])):
        if row != 0:
            row, col = go_up(row, col)
            result.append(arr[row][col])
            if col < (len(arr[0]) - 1):
                while row != 0 and col != (len(arr[0]) - 1):
                    row -= 1
                    col += 1
                    result.append(arr[row][col])
            else:
                while row != (len(arr) - 1) and col != 0:
                    row += 1
                    col -= 1
                    result.append(arr[row][col])
        if col != 0:
            row, col = go_left(row, col)
            result.append(arr[row][col])
            if row < (len(arr) - 1):
                while row != (len(arr) - 1) and col != 0:
                    row += 1
                    col -= 1
                    result.append(arr[row][col])
            else:
                while row != 0 and col != (len(arr[0]) - 1):
                    row -= 1
                    col += 1
                    result.append(arr[row][col])
    return result


print(zig_zag_in_arr(zig_arr))
