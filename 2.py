# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
n = int (input ('Введите количество элементов списка -> '))
list_one = []
for i in range(n):
    list_one.append(random.randint(1,100))
    i+=1
print(list_one)
list_one = list(set(list_one))
list_one.sort()
print(list_one)
x = int (input ('Введите x -> '))

if x > (list_one[len(list_one)-1]):
    print(list_one[len(list_one)-1])
elif x < list_one[0]:
    print(list_one[0])
elif list_one.count(x) !=0:
    print(x)
elif list_one.count(x) ==0:
    list_one.append(x)
    list_one.sort()
    q = list_one [(list_one.index(x))-1]
    a = list_one [(list_one.index(x))+1]
    if (x-q) > (a-x):
        print(a)
    else:
        print(q)

