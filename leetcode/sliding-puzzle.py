import copy
from typing import List


class Solution:
    position_distances = {}

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board_flattened = [board[i][j] for i in range(len(board)) for j in range(len(board[0]))]
        start_board = [1, 2, 3, 4, 5, 0]
        board_serialized = str(board_flattened)
        if str(start_board) == board_serialized:
            return 0
        if not Solution.position_distances.__len__():
            num_rows = len(board)
            num_cols = len(board[0])
            row_of_zero_beginning, col_of_zero_beginning = self.get_position_of_zero(start_board, num_rows, num_cols)
            this_distance = [[start_board, 0, row_of_zero_beginning, col_of_zero_beginning]]
            next_distance = []
            Solution.position_distances[str(start_board)] = 0
            index = 0
            while index < len(this_distance):
                position = this_distance[index][0]
                distance = this_distance[index][1]
                row_of_zero = this_distance[index][2]
                col_of_zero = this_distance[index][3]

                possible_moves = []
                if row_of_zero > 0:
                    possible_moves.append([row_of_zero - 1, col_of_zero])
                if row_of_zero < num_rows - 1:
                    possible_moves.append([row_of_zero + 1, col_of_zero])
                if col_of_zero > 0:
                    possible_moves.append([row_of_zero, col_of_zero - 1])
                if col_of_zero < num_cols - 1:
                    possible_moves.append([row_of_zero, col_of_zero + 1])

                for i, j in possible_moves:
                    number_to_switch_with_zero = position[i * num_cols + j]
                    position[i * num_cols + j] = 0
                    position[row_of_zero * num_cols + col_of_zero] = number_to_switch_with_zero
                    if Solution.position_distances.get(str(position)) is None:
                        Solution.position_distances[str(position)] = distance + 1
                        next_distance.append([copy.deepcopy(position), distance + 1, i, j])
                    position[row_of_zero * num_cols + col_of_zero] = 0
                    position[i * num_cols + j] = number_to_switch_with_zero
                index += 1
                if index >= len(this_distance):
                    this_distance = next_distance
                    index = 0
                    next_distance = []
        distance_of_board = Solution.position_distances.get(board_serialized)
        if distance_of_board is not None:
            return distance_of_board
        else:
            return -1

    def get_position_of_zero(self, position: List[int], num_rows, num_cols):
        for i in range(num_rows):
            for j in range(num_cols):
                if position[i * num_cols + j] == 0:
                    return i, j


if __name__ == '__main__':
    solution = Solution()
    print(solution.slidingPuzzle([[4, 1, 2], [5, 0, 3]]), " 5")
    print(solution.slidingPuzzle([[1, 2, 3], [5, 4, 0]]), " -1")
    print(solution.slidingPuzzle([[1, 2, 3], [4, 0, 5]]), " 1")
    print(solution.slidingPuzzle([[1, 2, 3], [4, 5, 0]]), " 0")
    print(solution.slidingPuzzle([[3, 2, 4], [1, 5, 0]]), " 14")
    print(solution.slidingPuzzle([[0, 5, 4], [3, 2, 1]]))
    print(solution.slidingPuzzle([[4, 5, 0], [1, 2, 3]]))
    print(solution.slidingPuzzle([[4, 5, 0], [3, 2, 1]]))
