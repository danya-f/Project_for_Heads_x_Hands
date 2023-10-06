from random import randint


def generator(n: int) -> list:
    '''Генератор массивов разной длинны + сортировка массиовов по порядковым номерам ( четные по возрастанию , нечетные по убыванию)'''
    x = []  # итоговый массив
    y = []  # промежуточный массив
    z = []  # замер массивов
    q = n + 1
    while n != 0:
        y = [randint(1, q * q) for i in range(randint(1, q))]  # генерируем рандомный массив
        if len(y) in z:  # если массив такой длины уже присутствует , генерируем массив еще раз
            continue
        else:
            z.append(len(y))
            x.append(y)
            y = []
        n -= 1
    for i in range(0, len(x), 2):
        x[i].sort()
    for i in range(1, len(x), 2):
        x[i].sort(key=lambda t: -t)
    return x
