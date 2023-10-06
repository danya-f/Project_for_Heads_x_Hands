from random import randint


def generator(n: int , сountdown : int=1) -> list:
    '''Генератор массивов разной длинны + сортировка массиовов по порядковым номерам ( четные по возрастанию , нечетные по убыванию)'''
    # Так как задание поставлено не четко и не понятно с нуля начинается отсчет
    # массивов или нет , я добавил переменную сountdown
    # которая равна 1 , если отсчет нужен с 0 , необходимо указать 0
    x = []  # итоговый массив
    y = []  # коллекция размеров массивов
    q = n + 1
    count = 1
    print(f'Общее число массивов: {n}')
    print()
    while n != 0:
        massiv = []
        z = randint(1, q * q)
        if z not in y:
            y.append(z)
            massiv = [randint(0, q * q) for i in range(z)]
            x.append(massiv)
            n -= 1
            print(f'Размер {count} массива : {z}')
            print()
            print(f'{count} массив : {massiv}')
            print()
            count += 1
        else:
            continue
    print(f'Итоговый неотсортированный массив : {x}')
    print()

    for i in range(0+сountdown, len(x), 2):
        x[i].sort()
    print(f'Отсортированные массивы стоящие на четных индексах : {sorted(x[0+сountdown:len(x):2])}')
    print()
    for i in range(1-сountdown, len(x), 2):
        x[i].sort(key=lambda x: -x)
    print(f'Отсортированные массивы стоящие на нечетных индексах : {sorted(x[1-сountdown:len(x):2], reverse= True)}')
    print()
    print('Итоговый отсортированный массив : ')
    return x


print(generator(10))
