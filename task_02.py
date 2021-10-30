""" Упражнение 2
Дан список list и числовой диапазон range. Разработайте метод coincidence(list,
range) для определения элементов из массива list, значения которого входят в
указанный диапазон range. Если не передан хотя бы один из параметров, то
должен вернуться пустой массив. """

def coincidence (user_list = None, range = None):
    result = []
    if user_list != None and range != None:
        my_list = [x for x in user_list if isinstance(x, (int,float))]
        range_list = list(range)

        start = range_list[0] 
        stop = range_list[len(range_list)-1]
        
        sorted_list = sorted(my_list)
        for number in sorted_list:
            if number >= start and number <= stop:
                result.append(number)
        return result
    return result  

print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))