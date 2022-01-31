"===================================================================================="""
"МАССИВЫ"

"""array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range("от какого элемента", "до какого элемента", "с каким щагом"):
    print(i, 'элемент =', array[i])
del array[:]        # полная очистка массива"""




"""array2 = []
"Заполнение массива"
n = int(input())    # количество элементов в массиве
for i in range(n):
    tmp = input()
    array2.append(tmp)
print(array2)"""


""""Вложенный циклы"
"как вывести все числа составленные из цифр?"
test = ['3', '2', '1']
for i in range(len(test)):
    for j in range(int(len(test))):
        print(test[i] + test[j])"""

"Нахождение всех делителей числа"

for i in range(850000, 850100):
    min = 1000 * 1200002103
    max = -1
    for j in range(2, i // 2):
        if i % j == 0 and j < min:
            min = j
            break

    for j in range(i-1, i // 2, -1):
        if i % j == 0 and j > max:
            max = j
            break

    if min == 1200002103000: f = 0
    print(i, min, max)

'===================================================================================='


str   = '123456789'
dicrionary = {'username': 'password', 'email': 'superPuperPass'}

print(dicrionary['username'])

for i in range(1):
    pass