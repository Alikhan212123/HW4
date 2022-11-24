# Инкапсуляция
# Полеморфизм

class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Person:
    def __init__(self, name, age, address):
        self.__address = address


class Animal:
    __a = 31

    def __init__(self, name, age, address):
        self.__name = name
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise AttributeError("Неверный тип аттрибута!")
        if isinstance(address, Address):
            self.__address = address
        else:
            raise AttributeError("Неверный тип аттрибута!")
        self.__is_born()

    def get_name(self):
        return self.__name

    def set_name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise AttributeError("Неверный тип аттрибута!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0:
            self.__age = value
        else:
            raise AttributeError("Неверный тип аттрибута!")

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if isinstance(value, Address):
            self.__address = value
        else:
            raise AttributeError("Неверный тип аттрибута!")

    def calculate_year(self):
        print(2022 - self.__age)

    def __is_born(self):
        print(f"Родилось животное {self.__name}")

    def info(self):
        return f"{self.__name} {self.__age} {self.__address.city} " \
               f"{self.__address.street} {self.__address.number}"

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, address, brad):
        super(Dog, self).__init__(name, age, address)
        self.__brad = brad

    @property
    def brad(self):
        return self.__brad

    @brad.setter
    def brad(self, value):
        self.__brad = value

    def speak(self):
        print(f"{self.get_name()} говорит ГАВ ГАВ")

    def info(self):
        return super().info() + f" {self.__brad}"


class Cat(Animal):
    def __init__(self, name, age, address, brad):
        super(Cat, self).__init__(name, age, address)
        self.__brad = brad

    @property
    def brad(self):
        return self.__brad

    @brad.setter
    def brad(self, value):
        self.__brad = value

    def speak(self):
        print(f"{self.get_name()} говорит Мяу Мяу")

    def info(self):
        return super().info() + f" {self.__brad}"


class Fish(Animal):
    def __init__(self, name, age, address):
        super(Fish, self).__init__(name, age, address)


class Cow:
    def __init__(self):
        pass


address1 = Address("Bishkek", "Ibraimova", 103)

ak_tosh = Dog("AK-Tosh", 2, address1, "Alabai")
alaman = Dog("Alaman", 2, address1, "OVCHARKA")
zholbors = Dog("zholbors", 2, address1, "Kandek")

murya = Cat("Murya", 1, address1, "Siam")
snezhok = Cat("snezhok", 1, address1, "Egypt")
simka = Cat("simka", 1, address1, "Megacom")

dorri = Fish("Dorri", 1, address1)

pets = [ak_tosh, murya, alaman, snezhok, zholbors, simka, dorri]

for pet in pets:
    pet.speak()
    print(pet.info())

# animal = Animal(name="Jyvotnoe", age=3, address=address1)
#
# print(animal.info())

# print(animal.get_name())
# print(animal.age)
# animal.set_name("AK_TOSH")
# animal.age = 5

# print(animal.get_name())
# print(animal.age)

# print(f"{animal}, {animal.age}")

# animal.age = "Tree"
# print(f"{animal.name}, {animal.age}")

# animal.calculate_year()
