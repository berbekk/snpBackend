""" Упражнение 11
Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
принимающим на вход name и calories (не обязательные параметры), а также двумя
методами is_healthy (возвращает true при условии калорийности десерта менее
200) и is_delicious (возвращает true для всех десертов). """

class Dessert():
    def __init__(self, name = None , calories = None):
        self.name = name
        self.calories = calories
        
    # Setters
    def setCalories(self, calories):
        self.calories = calories

    def setName(self, name): 
        self.name = name
        

    # Getters
    def getName(self): 
        try:
            return self.name
        except AttributeError:
            raise Exception("Название не задано")

    def getCalories(self): 
        try:
            return self.calories
        except AttributeError:
            raise Exception("Калории не заданы")

    def is_healthy (self):
        if self.name is not None and isinstance (self.name, str):
            if self.calories is not None and isinstance (self.calories, int):
                if self.calories < 200:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def is_delicious (self): return True
