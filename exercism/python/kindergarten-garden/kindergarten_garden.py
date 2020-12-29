plant_names = {
    "V": "Violets",
    "C": "Clover",
    "R": "Radishes",
    "G": "Grass"
}


def generator(diagram, students):
    row_one = diagram.split()[0]
    row_two = diagram.split()[1]
    index = 0
    while index < len(row_one):
        yield {"student": students[index // 2],
               "plants": [row_one[index], row_one[index + 1], row_two[index], row_two[index + 1]]}
        index += 2


class Garden:
    def __init__(self, diagram: str, students: tuple = ("Bob", "Charlie", "David",
                                                        "Eve", "Alice", "Ginny", "Harriet",
                                                        "Ileana", "Fred", "Joseph", "Kincaid", "Larry")):
        students = list(students)
        students.sort()
        self.plant_map = {}
        for student_plants in generator(diagram, students):
            self.plant_map[student_plants["student"]] = [plant_names[plant] for plant in student_plants["plants"]]

    def plants(self, name):
        return self.plant_map[name]
