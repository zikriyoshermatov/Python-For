price = float(input("1-narx: "))
mx = price
mn = price

for i in range(2, 5 +1):
    price = float(input(f"{i}-narx: "))
    if price > mx:
        mx = price
    if price < mn:
        mn = price

avg = (mn + mx) / 2
print(avg)