class Student:
    total_students = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Student.total_students += 1

    @classmethod
    def display_student(cls):
        print(f"Общее число ебланов с сухариками флинт {cls.total_students}")


student_1 = Student("Мишаня", "Гачи мастер")
student_2 = Student("Артур", "Cухарик")
student_3 = Student("Жека", "Уничтожитель")


Student.display_student()

