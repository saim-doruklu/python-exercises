class Matrix:

    def __init__(self, matrix_string: str):
        self.rows = []
        for line in matrix_string.splitlines():
            self.rows.append([int(num) for num in line.split()])

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return [row[index-1] for row in self.rows]
