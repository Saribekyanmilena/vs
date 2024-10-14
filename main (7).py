""" Сарибекян Милена 43ИС """
""" Реализовать методы добавления, удаления и отображения информации о животных, с наследованием и перегрузкой методов"""
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name} the {self.species}, {self.age} years old"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "Dog", age)
        self.breed = breed

    def __str__(self):
        return f"{self.name} the {self.breed} dog, {self.age} years old"

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Lion", age)

    def __str__(self):
        return f"{self.name} the mighty lion, {self.age} years old"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def display_animals(self):
        for animal in self.animals:
            print(animal)

# Пример использования
zoo = Zoo()
animal1 = Dog("Archi", 5, "Beagle")
animal2 = Lion("Simba", 4)

zoo.add_animal(animal1)
zoo.add_animal(animal2)

zoo.display_animals()
