try:
    start = int(input("Введіть перше число: "))
    end = int(input("Введіть друге число: "))

    for i in range(start,end + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('Fizz Buzz')
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

except Exception as e:
    print(e)
