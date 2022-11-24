class MusicPlaybleMixin:
    @staticmethod
    def play_music(song):
        print(f"Играет музыка {song}...")


class SmartPhone(MusicPlaybleMixin):
    def __init__(self, sim_card_list):
        self.sim_card_list = sim_card_list


smartphone1 = SmartPhone(sim_card_list=['Megacom', "Beeline"])
print(smartphone1.sim_card_list)


class Laptop(MusicPlaybleMixin):
    pass


class Car(MusicPlaybleMixin):
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def drive(self):
        print("Я еду!")

    def info(self):
        print(f"Model: {self.model} Year: {self.year}")

    def __str__(self):
        return f"Model: {self.model} Year: {self.year}"


class ElectricCar(Car):
    def __init__(self, model, year, battery):
        Car.__init__(self, model, year)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f"{self.model} едет используя Электричество!")

    def __str__(self):
        return super().__str__() + f" Battery: {self.battery}"


class FuelCar(Car):
    __total_fuel = 5000

    def __init__(self, model, year, fuel_bank):
        Car.__init__(self, model, year)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    @fuel_bank.setter
    def fuel_bank(self, value):
        self.__fuel_bank = value

    def drive(self):
        print(f"{self.model} едет используя Топливо!")

    @classmethod
    def get_total_fuel(cls):
        return cls.__total_fuel

    @staticmethod
    def fuel_type():
        print("AI - 95")

    def __str__(self):
        return super().__str__() + f" Fuel Bank: {self.fuel_bank}"

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank

    def __sub__(self, other):
        return self.__fuel_bank - other.__fuel_bank

    def __mul__(self, other):
        return self.__fuel_bank * other.__fuel_bank

    def __floordiv__(self, other):
        return self.__fuel_bank // other.__fuel_bank

    def __gt__(self, other):
        return self.year > other.year

    def __lt__(self, other):
        return self.year < other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __ge__(self, other):
        return self.__fuel_bank >= other.__fuel_bank

    def __le__(self, other):
        return self.__fuel_bank <= other.__fuel_bank


class HybridCar(ElectricCar, FuelCar):

    def __init__(self, model, year, battery, fuel_bank):
        FuelCar.__init__(self, model, year, fuel_bank)
        ElectricCar.__init__(self, model, year, battery)

    def drive(self):
        print(f"{self.model} едет используя Топливо и Электричество!")


tesla = ElectricCar("Tesla Model X", 2022, 80000)
bmw = FuelCar("BMW X5", 2021, 60)
mers = FuelCar("Mers E220", 2002, 50)
lexus = HybridCar("Lexus lx-600", 2021, 50000, 40)

smartphone = SmartPhone(['megacom', "O!"])
laptop = Laptop()
# tesla.drive()
# bmw.drive()
# lexus.drive()

# tesla.info()
# print(tesla.model, tesla.year)

print(tesla)
print(bmw)
print(lexus)

print(FuelCar.get_total_fuel())
lexus.fuel_type()

lexus.play_music("Another Love")
laptop.play_music("Kiss - I was made")
smartphone.play_music("365")

# MRO - Method Resolution Order
# print(HybridCar.__mro__)
# print(HybridCar.mro())
