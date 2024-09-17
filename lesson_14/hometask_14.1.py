class Human:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}\nAge: {self.age}\nGender: {self.gender}'


class Student(Human):

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        self.record_book = record_book
        super().__init__(gender, age, first_name, last_name)

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}\nAge: {self.age}\nGender: {self.gender}\nRecord book: {self.record_book}'


class StudentLimitError(Exception):
    pass


class Group:

    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student):
        if len(self.group) == 10:
            raise StudentLimitError("Only ten students per group is allowed")
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


gr = Group('PD1')
for _ in range(10):
    student = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    gr.add_student(student)

student = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
try:
    gr.add_student(student)
except StudentLimitError as sle:
    print(f'Student limit reached: {sle}')
