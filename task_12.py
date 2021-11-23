""" Упражнение 12 
Создайте класс JellyBean, расширяющий класс Dessert (из Упражнения 11) новым
геттером и сеттером для атрибута flavor (все параметры являются не
обязательными). Измените метод is_delicious таким образом, чтобы он возвращал
false только в тех случаях, когда flavor равняется «black licorice». """

from task_11 import Dessert

class JellyBean (Dessert):
    def __init__(self, name = None, calories = None, flavor = None):
        Dessert.__init__(self, name, calories)
        self.flavor = flavor

    def setFlavor(self, flavor):
        self.flavor = flavor
    
    def getFlavor(self):
        return self.flavor

    def is_delicious(self):
        if self.flavor == "black licorice":
            return False
        else:
            return True