import mymodule as mm
import opentaskmodule as otm
otm.open_task("136k.jpg")


n = int(input("Введите n = "))
a = [0] * n
a = mm.init_array(a)

res = mm.calc136k(a)

print("\nRes = ", res)
