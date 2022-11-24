import random


class GameEnity:
    def __init__(self,name,health,damage):
        self.name = name
        self.health = health
        self.damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f"{self.__name} health: {self.__health} damage: {self.__damage}"
class Boss(GameEnity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health = hero.health - self.damage

    def __str__(self):
        return "BOSS " + super().__str__() + f" defence: {self.__defence}"

class Heroes(GameEnity):
    def __init__(self, name, health, damage,super_abilityes):
        super(Heroes,self).__init__(name, health, damage,super_abilityes)
        self.super_abilityes = super_abilityes

class Berserk(Heroes):
    @property
    def super_ability(self):
        return self.__super_ability

    def hit(self, boss):
        if boss.health > 0 and self.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes,range):
        range = random.randint(1,5)
        boss.health -= self.damage * range
        print("Berserk range"f"{self.damage}")

class Thor(Heroes):
    def __init__(self, name, health, damage):
        super(Thor, self).__init__(name, health, damage, "LIGHTNING")
        
    def apply_super_power(self, boss, heroes):
            for hero in heroes:
                sun = random.randint(5, 11)
                if hero != self and hero.health > 0 and sun ==7:
                    hero.health += 50
                    print(" YOU'LL DIE ")
