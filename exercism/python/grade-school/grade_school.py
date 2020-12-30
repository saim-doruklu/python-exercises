class School:
    def __init__(self):
        self.grade_roster = {}

    def add_student(self, name, grade):
        self.grade_roster.setdefault(grade, [])
        self.grade_roster[grade].append(name)

    def roster(self):
        return [student for grade_students in sorted(self.grade_roster.items()) for student in sorted(grade_students[1])]

    def grade(self, grade_number):
        return sorted(self.grade_roster.get(grade_number, []))
