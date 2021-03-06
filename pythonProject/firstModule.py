import random
import numpy as np


def randArr(a, n):
    """
    Заполнение массива случайными числами
    :param a:
    :param n:
    :return:
    """
    for i in range(n):
        a.append(random.randint(1, 19))
        print(a[i])


def printArr(a, n):
    """
    Печать массива на экране
    :param a:
    :param n:
    :return:
    """
    for i in range(n):
        print(a[i])


def randArray(a, n, low, high):
    """
    Создание массива
    :param a:
    :param n:
    :return:
    """
    for i in range(n):
        a.append(random.randint(low, high))
    return a

def lab5(a, n):
    """
    Вычисление суммы элементов массива в квадрате умноженное на два
    :param a:
    :param n:
    :return summ:
    """
    summ = 0
    for i in range(n):
        summ += a[i]
    return 2 * summ**2


def lab6(a):
    """
    Нахождение членов последовательности, к-ые
    явл-ся удвоенными нечётными числами
    :param a:
    :return b:
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


def lab8(a, n):
    """
    Получение матрицы элемент, к-ой равен сумме элементов данной матрицы
    расположенных в области, как на рисунке
    :param n:
    :return:
    """
    b = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            summ = a[n - i - 1:n][n - j - 1:n].sum()       # до n-1
            b[i][j] = summ

    # ПРОШЛЫЙ ВАРИАНТ
    for i in range(n):
        for j in range(n):
            summ = 0
            for k in range(n - i - 1, n):
                for l in range(n - j - 1, n):
                    summ += a[k][l]
            b[i][j] = summ
    return b
