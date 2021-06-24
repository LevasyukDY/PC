import random
import numpy as np

def randArr(a,n):
    """
    Заполнение массива случайными числами
    :param a:
    :param n:
    :return:
    """
    for i in range(n):
        a.append(random.randint(1, 19))
        print(a[i])

def printArr(a,n):
    """
    Печать массива на экране
    :param a:
    :param n:
    :return:
    """
    for i in range(n):
        print(a[i])

def lab5(a,n):
    """
    Вычисление суммы элементов массива в квадрате умноженное на два
    :param a:
    :param n:
    :return:
    """
    summ = 0
    for i in range(n):
        a.append(random.randint(-10, 10)) # TODO: создание и добавление отдельно
        summ += a[i]
    return summ

def lab6(a):
    """
    Нахождение членов последовательности, к-ые
    явл-ся удвоенными нечётными числами
    :param a:
    :return:
    """
    b = []
    print("_____________________________________")
    for i in range(len(a)):
        if (a[i] % 2 == 0) and ((a[i] // 2) % 2 != 0):
            b.append(a[i])
    return b

def lab7(n):
    """
    Вычисление суммы по формуле из задачи 335
    :param n:
    :return:
    """
    k = 0
    for i in range(1, n + 1):
        k += i ** i
    return k

def lab8(n):
    """
    Получение матрицы элемент, к-ой равен сумме элементов данной матрицы
    расположенных в области, как на рисунке
    :param n:
    :return:
    """
    a = np.ones((n, n))
    b = np.zeros((n, n))
    i = j = 0
    for i in range(n):
        for j in range(n):
            summ = 0
            summ = a[n - i - 1:n][n - j - 1:n].sum()
            b[i][j] = summ
    print(b)

#     for i in range(n):
#             for j in range(n):
#                 summ = 0
#                 for k in range(n - i - 1, n):
#                     for l in range(n - j - 1,n):
#                         summ += a[k][l]
#                 b[i][j] = summ
