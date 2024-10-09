""" Сарибекян Милена 43ИС """
""" Реализовать методы добавления, удаления и отображения информации о животных"""
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name} the {self.species}, {self.age} years old"

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
animal1 = Animal("Archi", "Dog", 5)
animal2 = Animal("Simba", "Lion", 4)

zoo.add_animal(animal1)
zoo.add_animal(animal2)

zoo.display_animals() 