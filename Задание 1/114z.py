from math import factorial
import opentaskmodule as otm
otm.open_task("114z.jpg")

n = 10
res = 0.0

for i in range(2,n+1):
    res += (1 - (1 / factorial(i))) ** 2

print(res)