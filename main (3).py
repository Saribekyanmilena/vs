""" Сарибекян Милена 43ИС """
""" Создать класс студент, c реализацией метода подсчета среднего балла студента. """
class Student:
    def __init__(self, name, age):
        self.name = name    
        self.age = age      
        self.grades = []    

    def add_grade(self, grade):
        """Добавляет оценку в список оценок."""
        self.grades.append(grade)

    def get_average_grade(self):
        """Возвращает среднюю оценку студента."""
        if len(self.grades) == 0:
            return 0  # Если нет оценок, возвращаем 0
        return sum(self.grades) / len(self.grades)


student1 = Student("Милена", 17)
student1.add_grade(4)
student1.add_grade(5)
student1.add_grade(3)

print(f"Средняя оценка студента {student1.name}: {student1.get_average_grade():.2f}")
