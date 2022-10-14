# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def packing(txt):
    count = 1
    res = ''
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt) - 2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def unpacking(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


file = input('Введите текст из буквенных символов: ')
print('Код после сжатия: ', packing(file))
print('Текст после восстановления данных: ', unpacking(packing(file)))