start = int(input("son: "))
step = 1
stop = int(input("stop: "))

if start <= stop:
    for i in range(start, stop +1, +step):    
        print(i)

else:
    for i in range(start, stop -1, -step):
        print(i)