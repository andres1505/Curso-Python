numero = int(input("Introduce un número entero positivo: "))
while numero < 0:
    numero = int(input("Introduce un número entero positivo: "))
else: 
    suma = ((numero*(numero+1))/2)
    print("la suma de los numero es:", suma)