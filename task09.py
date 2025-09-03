num = float(input("1-son: "))
mn = num

for i in range(2, 8):
    num = float(input(f"{i}-son: "))
    if num < mn:
        mn = num


print(mn)