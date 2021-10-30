""" Упражнение 10
Разработайте функцию count_words(string), которая будет возвращать словарь со
статистикой частоты употребления входящих в неё слов. """

import re
def count_words(value):
    res = {}
    words = re.findall(r'\b\w+\b', value)
    words_lower = [char.lower() for char in words]
    for word in words_lower:
        count = words_lower.count(word)
        res[str(word)] = count
    return res   
print(count_words("A man, a plan, a canal -- Panama")) # => {"a": 3, "man": 1,"canal": 1, "panama": 1, "plan": 1}
print(count_words("Doo bee doo bee doo")) # => {"doo": 3, "bee": 2}