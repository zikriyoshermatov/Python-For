num = float(input("1-son: "))
mx = num
mn = num

for i in range(2, 8):
    num = float(input(f"{i}-son: "))
    if num > mx:
        mx = num
    if num < mn:
        mn = num

avg = (mn + mx) / 2
print(avg)