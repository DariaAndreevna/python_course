from human import Human


class Student(Human):

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        self.record_book = record_book
        super().__init__(gender, age, first_name, last_name)

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}\nAge: {self.age}\nGender: {self.gender}\nRecord book: {self.record_book}'

    def __eq__(self, other):
        return self.last_name == other.last_name

    def __hash__(self):
        return hash(str(self))
