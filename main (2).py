""" Сарибекян Милена 43ИС """
""" Создать класс автомобиль, с реализацией следующих методов:
метод, выводящий информацию о автомобиле.
метод, выводящий текущие показания одометра.
метод, обновляющий показания одометра. """
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def describe_car(self):
        return f"{self.year} {self.brand} {self.model}"

    def read_odometer(self):
        return f"Одометр: {self.odometer_reading} мили"

    def update_odometer(self, miles):
        if miles >= self.odometer_reading: """проверка, чтобы нельзя было уменьшать"""
            self.odometer_reading = miles
        else:
            print("Вы не можете откатить одометр!")

my_car = Car('BMW', 'M5', 2022)
print(my_car.describe_car())
my_car.update_odometer(15000)
print(my_car.read_odometer())
