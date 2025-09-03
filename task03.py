start = int(input("son: "))
stop = 15

if start <= stop:
    for i in range(start, stop +1):    
        print(i)

else:
    for i in range(start, stop -1, -1):
        print(i)