import re

import numpy as np

def apply_on_matrix(functions, matrix, part):
    for function in functions:
        words = re.split("[\s,]", function)
        if words[0] == "toggle":
            offset = 1
        else:
            offset = 2
        start_x, start_y = [int(words[offset]), int(words[offset + 1])]
        end_x, end_y = [int(words[offset + 3])+1, int(words[offset + 4])+1]
        if words[0] == "turn" and words[1] == "on":
            if part == "part_one":
                matrix[start_x:end_x, start_y:end_y] = True
            else:
                matrix[start_x:end_x, start_y:end_y] += 1
        elif words[0] == "turn" and words[1] == "off":
            if part == "part_one":
                matrix[start_x:end_x, start_y:end_y] = False
            else:
                slice = matrix[start_x:end_x, start_y:end_y]
                matrix[start_x:end_x, start_y:end_y] = np.where(slice == 0, slice, slice-1)
        else:
            if part == "part_one":
                matrix[start_x:end_x, start_y:end_y] = ~matrix[start_x:end_x, start_y:end_y]
            else:
                matrix[start_x:end_x, start_y:end_y] += 2
    return np.sum(matrix)


if __name__ == '__main__':
    with open('inputs/binary_matrix_ops.txt', 'r') as file:
        all_lines = file.readlines()
        matrix_sum_two = apply_on_matrix(all_lines, np.full((1000, 1000), 0), "part_two")
        matrix_sum_one = apply_on_matrix(all_lines, np.full((1000, 1000), False), "part_one")
        print(matrix_sum_one, " ", matrix_sum_two)
