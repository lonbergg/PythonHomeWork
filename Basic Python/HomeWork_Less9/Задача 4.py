class Student:
    def __init__(self, name, surname, features=None):
        self.name = name
        self.surname = surname
        self.features = features if features is not None else []

    def __len__(self):
        return len(self.features)


student_1 = Student("Oleg", "Colda", features=[2, 4, 5, 3])
student_2 = Student("Artur", "Kalinenko", features=[4, 5, 5, 5, 5])
print(student_2.__len__())

list_students = [
    Student("Jenya", "Gigach", features=[5, 5, 5, 5, 5, 5]),
    Student("Misha", "Syharik", features=[3, 4, 5, 5, 5, 5, 5]),
    Student("SerGey", "Krut", features=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, ])
]

student_sort = sorted(list_students, key=len)
for student in student_sort:
    print(f"Норм чел {student.name} {student.surname}, норм оценок {len(student.features)}")
