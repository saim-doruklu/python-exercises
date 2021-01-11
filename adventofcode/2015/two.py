import numpy as np


class DayTwo:
    def part_one(self, gifts):
        sum = 0
        for gift in gifts:
            dimensions = [int(dimension) for dimension in gift.split("x")]
            dimensions_1_3 = np.matrix(dimensions)
            dimensions_3_1 = np.transpose(dimensions_1_3)
            dimensions_x_dimensions = np.matmul(dimensions_3_1, dimensions_1_3)
            dimensions_x_dimensions = dimensions_x_dimensions.astype(np.float)
            np.fill_diagonal(dimensions_x_dimensions, np.nan)
            this_result = np.nansum(dimensions_x_dimensions) + np.nanmin(dimensions_x_dimensions)
            sum += int(this_result)
        return sum

    def part_two(self, gifts):
        sum = 0
        for gift in gifts:
            dimensions = [int(dimension) for dimension in gift.split("x")]
            dimensions_1_3 = np.matrix(dimensions)
            dimensions_3_1 = np.transpose(dimensions_1_3)
            dimensions_x_dimensions = self.custom_multiply(dimensions_3_1, dimensions_1_3)
            dimensions_x_dimensions = dimensions_x_dimensions.astype(np.float)
            np.fill_diagonal(dimensions_x_dimensions, np.nan)
            this_result = int(np.nanmin(dimensions_x_dimensions)) + np.prod(dimensions_1_3)
            sum += this_result
        return sum

    def custom_multiply(self,x, y):
        return np.array([2*(row + column) for row in x for column in y.T]).reshape(x.shape[0], y.shape[1])


if __name__ == '__main__':
    with open('two.txt', 'r') as file:
        all_lines = file.readlines()
        day_two = DayTwo()
        print(day_two.part_one(all_lines))
        print(day_two.part_two(all_lines))
