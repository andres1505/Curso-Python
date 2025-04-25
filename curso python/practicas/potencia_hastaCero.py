n = int(input("introduce un numero entre 1 y 20: "))
if n in range (1,21):
    i = 0
    while i < n:
        print(i**2)
        i +=1 #le suma 1 a i cada vez que itere