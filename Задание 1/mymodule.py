from numpy import random as rn





def calc136k(arr):
    """
    Заполнение массива случайными числами или вручную
    
    Параметры:
    arr -- массив

    """
    res = 0.0
    for i in range(len(arr)):
        res += arr[i]
    return (res ** 2) * 2


def init_array(arr):
    """
    Заполнение массива случайными числами или вручную
    
    Параметры:
    arr -- массив

    """
    
    print("\nЗаполнить массив случайными числами? Введите \"1\", если да или \"0\", если нет!")
    flag = int(input("flag = "))

    if flag == 1:
        arr = rn.randint(1, 10, len(arr), )
        #arr = rn.random(len(arr),)
        print("\na =", arr)
        return arr
        
    elif flag == 0:
        print()
        for i in range(len(arr)):
            arr[i] = float(input("a[{}] = ".format(i+1)))
        return arr
            
    else:
        print("Вы ввели неккоректное значение, было решено заполнить массив случайными числами")
        arr = rn.randint(1, 10, len(arr), )
        #arr = rn.random(len(arr),)
        print("\na =", arr)
        return arr
