from student import Student


class Group:

    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student):
        self.group.add(student)

    def find_student(self, last_name: str) -> Student | None:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str):
        st_to_del = self.find_student(last_name)
        if st_to_del:
            self.group.remove(st_to_del)

    def __str__(self):
        all_students = "\n".join([str(s) for s in self.group])
        return f'Number:{self.number}\n{all_students}'
