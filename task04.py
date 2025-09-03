start = int(input("son: "))
step = int(input("son "))
stop = 15

if start <= stop:
    for i in range(start, stop +1, +step):    
        print(i)

else:
    for i in range(start, stop -1, -step):
        print(i)