""" Упражнение 12 
Создайте класс JellyBean, расширяющий класс Dessert (из Упражнения 11) новым
геттером и сеттером для атрибута flavor (все параметры являются не
обязательными). Измените метод is_delicious таким образом, чтобы он возвращал
false только в тех случаях, когда flavor равняется «black licorice». """

from task_11 import Dessert

class JellyBean (Dessert):
    def __init__(self, name = None, calories = None, flavour = None):
        Dessert.__init__(self, name, calories)
        self.flavour = flavour

    def setFlavour(self, flavour):
        self.flavour = flavour
    
    def getFlavour(self):
        return self.flavour

    def is_delicious(self):
        if self.flavour == "black licorice":
            return False
        else:
            return True