class DayThree:
    # num different locations visited by a series of moves
    # "><" means:  1 right + 1 left : [0,0] -> [0,1] -> [0,0] : total visited 2
    # "><^" means:  1 right + 1 left + 1 up: [0,0] -> [0,1] -> [0,0] -> [1,0] : total visited 3
    def part_one(self, moves: str):
        position = [0, 0]
        visited_coordinates = {str(position)}
        for row_delta, col_delta in self.convert_to_move(moves):
            position[0] += row_delta
            position[1] += col_delta
            visited_coordinates.add(str(position))
        return len(visited_coordinates)

    def part_two(self, moves: str):
        players = [[0, 0], [0, 0]]
        visited_coordinates = {str(players[0])}
        num_player_this_turn = 0
        for row_delta, col_delta in self.convert_to_move(moves):
            player = players[num_player_this_turn]
            player[0] += row_delta
            player[1] += col_delta
            visited_coordinates.add(str(player))
            num_player_this_turn = 0 if num_player_this_turn == 1 else 1
        return len(visited_coordinates)

    def convert_to_move(self, moves):
        for move in list(moves):
            if move == "^":
                yield [-1, 0]
            elif move == ">":
                yield [0, 1]
            elif move == "v":
                yield [1, 0]
            elif move == "<":
                yield [0, -1]
        return


if __name__ == '__main__':
    day_three = DayThree()
    # print(day_three.part_one("^>v<"), 4)
    # print(day_three.part_one(">"), 2)
    # print(day_three.part_one("^v^v^v^v^v"), 2)
    # print(day_three.part_two("^>v<"), 3)
    # print(day_three.part_two("^v"), 3)
    # print(day_three.part_two("^v^v^v^v^v"), 11)
    with open('inputs/three.txt', 'r') as file:
        all_lines = file.readlines()
        print(day_three.part_one(all_lines[0]))
        print(day_three.part_two(all_lines[0]))
