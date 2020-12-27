class Matrix:

    def __init__(self, matrix_string: str):
        self.rows = []
        self.cols = []
        lines = matrix_string.splitlines()
        for index, line in enumerate(lines):
            line_as_int_array = list(map(int, line.split()))
            self.rows.append(line_as_int_array)
        for i in range(self.rows[0].__len__()):
            self.cols.append(list(map(lambda row: row[i], self.rows)))

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.cols[index - 1]
