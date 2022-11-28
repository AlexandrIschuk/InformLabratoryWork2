import random
print("-"*90)
print("Задание 1.")
print("Найти минимальный четный пложительный элемент заданного массива.")
print("Задание 2.")
print("Найти индекс последнего нечётного элемента некратного X.")
print("Задание 3.")
print("Отсортировать массив по возрастанию старших цифр элементов списка (сортировка Шелла).")
a = []
def first(a):
    n = int(input("Введите количество элементов списка: "))
    print("Введите диапазон элементов через пробел:")
    b,c = map(int, input().split())
    for i in range(n):
        a.append(random.randint(b,c))
    return a
def FindMin(a):
    m = 10**10
    for i in range(len(a)):
        if a[i]%2 == 0 and a[i]<m and a[i]>0:
            m = a[i]
    if m != 10**10:
        return m
def LastIndex(a):
    n = len(a)
    print("Введите x:")
    x = int(input())
    i = n - 1
    while i>=0 and (a[i]%2 == 0 or a[i]%x == 0):
        i = i - 1
    if i >= 0:
        return i
    else:
        return "Таких нет"
print("-"*90)
print("Выберите способ заполнения массива:")
print("Введите 1 для автоматического заполнения массива")
print("Введите 2 для заполнения массива вручную")
v = int(input())
if v == 1:
    print("Массив",first(a))
else:
    print("Заполните массив:")
    a = (list(map(int, input().split())))
def shellSort(a):
     t = 5
     h = [9,5,3,2,1]
     for j in range(t):
         k = h[j]
         for i in range(len(a) - k):
             if a[i]>a[i + k]:
                 v = a[i]
                 a[i] = a[i+k]
                 a[i+k] = v
     return a
print("-"*90)
print("Ответ на задание 1:")
print("Минимальный четный положительный элемент: ",FindMin(a))
print("Ответ на задание 2")
print("Индекс последнего нечётного элемента некратного X: ",LastIndex(a))
print("Ответ на задание 3")
print("Сортировка Шелла:",shellSort(a))
print("-"*90)




