class GameEnity:
    def __init__(self,name,health,damage):
        self.name = name
        self.health = health
        self.damage = damage
    @property
    def name(self):
        return self.name
    @name.setter
    def name(self,value):
        self.name = value
    @property
    def health(self):
        return self.health
    @health.setter
    def health(self,value):
        self.health = value
    @property
    def damage(self):
        return self.damage
    @damage.setter
    def damage(self,value):
        self.damage = value

class Boss(GameEnity):
    def __init__(self, name, health, damage):
        super(Boss).__init__(name, health, damage)