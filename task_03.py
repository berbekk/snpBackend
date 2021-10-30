""" Упражнение 3
Дан список элементов произвольной природы. Необходимо разработать метод
max_odd(array), который определит максимальный нечетный элемент (21.000 = 21 и
тоже считается нечетным элементом). Вернуть None, если таких элементов нет в
переданном массиве. """

def max_odd (array):
    
    sorted = []

    for item in array:
        if type(item) is list:
            for el in item:
                if isinstance (el, (int,float)):
                    sorted.append(el)
        if isinstance (item, (int,float)):
            sorted.append(item)

    sorted.reverse()
    list_unique = list(set(sorted))

    if list_unique:
        for item in reversed(list_unique):
            if item % 2 != 0:
                return int(item)
                break
    else:
        return None            

print (max_odd([1, 2, 3, 4, 4]))  # => 3
print (max_odd([21.0, 2, 3, 4, 4])) # => 21
print (max_odd(['ololo', 2, 3, 4, [1, 2], None])) # => 3
print (max_odd(['ololo', 'fufufu'])) # => None
print (max_odd([2, 2, 4])) # => None