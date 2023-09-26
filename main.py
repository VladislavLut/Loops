try:
    print('Введіть початок та кінець діапазону')
    start = int(input("Початок:"))
    end = int(input('Кінець:'))
    print('Усі числа діапазону.')
    for i in range(start, end+1):
        print(i, end="")
    print()
    print('Усі числа діапазону за спаданням.')
    for i in range(end, start -1,-1):
        print(i, end="")
    print()
    print('Усі числа кратні 7:')
    for i in range(start, end +1):
        if i % 7 == 0:
            print(i, end=" ")
        print()
        print('Кількість чисел, кратних 5:')
        count = 0
        for i in range(start, end+ 1):
            if i % 5 == 0:
                count += 1
        print(count)

except Exception as e:
    print(e)



