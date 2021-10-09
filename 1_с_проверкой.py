try:
    n = int(input('Ввести количество элементов в массиве'))
    arr = []
except ValueError:
    print('Неверные данные')
    exit()
else:
    for i in range(n):
        arr.append(int(input('Ввести элементы массива')))
    print('Состав массива:', arr)
    print('Ввести значение дельты')
    delta = int(input())
    check = [min(arr) - delta, min(arr) + delta]
    ans = arr.count(check[0]) + arr.count(check[1])
    print("Вывод:", ans)