class Computer:
    def __init__(self,cpu,memory):
        self.cpu = cpu
        self.memory = memory
    @property
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self,value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory
    @memory.setter
    def memory(self,value):
        self.__memory = value
    def make_comututations(self,other):
        
    def __add__(self, other):
        return self.__cpu + other.__memory

    def __sub__(self, other):
        return self.__cpu - other.__memory

    def __mul__(self, other):
        return self.__cpu * other.__memory

    def __floordiv__(self, other):
        return self.__cpu // other.__memory

    def __ge__(self, other):
        return self.__cpu >= other.__memory

    def __le__(self, other):
        return self.__cpu <= other.__memory

class Phone:
    def __sim_cards_list(self,sim1,sim2):
        self.sim1 = sim1
        self.sim2 = sim2
    @property
    def sim1(self):
        return self.sim1
    @sim1.setter
    def sim1(self,value):
        self.sim1 = value
    @property
    def sim2(self):
        return self.sim2
    @sim2.setter
    def sim2(self,value):
        self.sim2 = value
call = Phone(sim)



