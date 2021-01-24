class DayOne:
    # count parentheses: "("=+1, ")"=-1
    def part_one(self, instructions):
        return instructions.count("(") - instructions.count(")")

    # where is result first equals to -1?  "("=+1, ")"=-1
    def part_two(self, instructions):
        return len(list(self.convert_to_floor(instructions)))

    def convert_to_floor(self, instructions):
        total = 0
        for char in list(instructions):
            if total == -1:
                break
            instruction = 1 if char == "(" else -1
            total += instruction
            yield


if __name__ == '__main__':
    with open('inputs/one.txt', 'r') as file:
        all_lines = file.readlines()
        line_zero = all_lines[0]
        day_one = DayOne()
        print(day_one.part_one(line_zero))
        print(day_one.part_two(line_zero))
