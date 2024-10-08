""" Сарибекян Милена 43ИС """
""" Реализовать метод для вывода информации о погоде в городе """
class Weather:
    def __init__(self, temperature, condition):
        self.temperature = temperature  
        self.condition = condition  

    def __str__(self):
        return f"Температура: {self.temperature}°C, Состояние погоды: {self.condition}"


class City:
    def __init__(self, name, weather):
        self.name = name  
        self.weather = weather  
        
    def display_weather(self):
        print(f"Погода в городе {self.name}: {self.weather}")


if __name__ == "__main__":
    weather = Weather(16, "облачно")
    city = City("Москва", weather)
    city.display_weather()
