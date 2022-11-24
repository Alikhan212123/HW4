# ООП - Объектно Ориентированое Програмирование
# DRY - Don't Repeat Yourself


class Transport:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color


class Car(Transport):  # Чертеж
    wheels = 4  # Атрибут класса

    # self.model - Аттрибуты / Поля \ Свойство  объекта
    # __init__ - Конструктор
    def __init__(self, model, year, color, penalties=0):
        Transport.__init__(self, model, year, color)
        super().__init__(model, year, color)
        self.penalties = penalties

    def drive(self, city):  # Метод
        print(f"Машина {self.model} едет в {city}...")

    def change_color(self, new_color):
        self.color = new_color


class Rocket(Transport):
    def __init__(self, model, year, color):
        Transport.__init__(self, model, year, color)

    def fly(self, planet):
        print(f'Ракета {self.model} полетела на планету {planet}')


class Truck(Transport):
    def __init__(self, model, year, color, load_capacity, penalties=0):
        Transport.__init__(self, model, year, color)
        self.load_capacity = load_capacity
        self.penalties = penalties

    def load_cargo(self, product, weight):
        if self.load_capacity > weight:
            print(f"{product} ({weight} kg) Загружен в {self.model}")
        else:
            print(f"Вы не можете загрузить этот груз (Максимальная грузоподъемность {self.load_capacity} kg)")


def sum_ab(a, b):
    return a + b


mers_car = Car("Mersedes-Benz A52", 2020, "Black", 2000)  # Объект
kia = Car(model="Kia RIO", year=2017, color="White")
# a = Car()
rocket = Rocket("Nasa K32", 2022, 'White')

print(rocket.model)
rocket.fly('Марс')

# print(type(mers_car))  # Ссылка на объект
# print(f"{mers_car.model} {mers_car.year} {mers_car.color} {mers_car.penalties}")
print(f"{kia.model} {kia.year} {kia.color} {kia.penalties}")

kia.color = 'Red'
kia.change_color('Green')

print(f"{kia.model} {kia.year} {kia.color} {kia.penalties}")
# print(kia.wheels)

mers_car.drive('Ош')
kia.drive('Бишкек')

man = Truck("Optimus Prime", 2012, "Red", 30000)

man.load_cargo("Яблоки", 31000)
