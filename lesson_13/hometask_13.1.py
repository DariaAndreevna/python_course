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


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
