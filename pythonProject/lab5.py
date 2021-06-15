import firstModule
# Задание 136 к

a = []
n = 10
low = -10
high = 10

a = firstModule.randArray(a, n, low, high)
res = firstModule.lab5(a, n)
firstModule.printArr(a, n)

print("Result = ", res)