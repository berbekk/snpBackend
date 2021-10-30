""" Упражнение 4
Дан список целых чисел. Необходимо разработать метод sort_list(list),который
поменяет местами все минимальные и максимальные элементы массива, а также
добавит в конец массива одно минимальное значение из него. """

def sort_list(numbers):
    if numbers:
        sorted_num = sorted(numbers)
        min = sorted_num [0]
        max = sorted_num [len(sorted_num)-1]

        for index in range(len(numbers)):
            el = numbers[index]
            if el == max:
                numbers[index] = min
                continue
            if el == min:
                numbers[index] = max
        numbers.append(min)
        return numbers
    else:
        return []

print(sort_list([])) # => []
print (sort_list([2, 4, 6, 8])) # => [8, 4, 6, 2, 2]
print (sort_list([1])) # => [1, 1]
print (sort_list([1, 2, 1, 3])) # => [3, 2, 3, 1, 1])