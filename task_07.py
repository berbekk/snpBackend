""" Упражнение 7
Анаграмма — литературный приём, состоящий в перестановке букв или звуков
определённого слова (или словосочетания), что в результате даёт другое слово
или словосочетание.
Разработайте метод combine_anagrams(words_array), который принимает на вход
массив слов и разбивает их в группы по анаграммам, регистр букв не имеет
значения при определении анаграмм. """

def combine_anagrams (word_list):
    anagram_list = []
    tmp = []
    for word_1 in word_list: 
        tmp.append(word_1)
        for word_2 in word_list: 
            if word_1 != word_2 and (sorted(word_1)==sorted(word_2)):
                tmp.append(word_2)
                word_list.pop(word_list.index(word_2))
        anagram_list.append(tmp)
        tmp = []
    return anagram_list

print (combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
