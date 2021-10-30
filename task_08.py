""" Упражнение 8
Написать метод multiply_numbers(inputs), который вернет произведение цифр,
входящих в inputs. """

import re
from functools import reduce

def multiply_numbers(numbers = None):
        sorted = re.findall('\d', str(numbers))
        if sorted:
            return reduce(lambda x, y: int(x) * int(y) , sorted)


print (multiply_numbers()) # => None
print (multiply_numbers('ss')) # => None
print (multiply_numbers('1234')) # => 24
print (multiply_numbers('sssdd34')) # => 12
print (multiply_numbers(2.3)) # => 6
print (multiply_numbers([5, 6, 4])) # => 120