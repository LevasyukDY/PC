import opentaskmodule as otm
otm.open_task("38.jpg")


x = float(input("Введите x: "))
y = float(input("Введите y: "))

if x > y:
    z = x - y
else:
    z = y - x + 1
    
print(f"\nz = {z:.6}")