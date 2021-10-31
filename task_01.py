""" Упражнение 1
Разработайте метод is_palindrome(string), который будет определять, является ли
параметр string палиндромом (строкой, которая читается одинаково как сначала
так и с конца), при условии игнорирования пробелов, знаков препинания и
регистра. """

import re
def is_palindrome(value):
    sorted = re.findall('\w', str(value))
    result = "".join(sorted).lower()

    for index in range(0,len(result)):
        first = result[index]
        last = result[(len(result)-1)-index]
        if first == last:
            palindrome = True
        else:
            palindrome = False
            break   
    return palindrome


print (is_palindrome ("A man, a plan, a canal -- Panama")) # => True
print (is_palindrome ("Madam, I'm Adam!")) # => True
print (is_palindrome (333)) # => True
print (is_palindrome (None)) # => False
print (is_palindrome ("Abracadabra")) # => False