# ejercicio mejorado par o impar
# el programa debe pedir un número al usuario y decir si es par o impar, pero si el número es mayor que 100, el programa debe pedir otro número hasta que sea menor que 100.
n = int(input("Introduce un número: "))   
while n < 0 and n < 100:
    #tiene que ser un numero mayor que 1 y menor que 100
    n = int(input("Introduce un número mayor menor que 100 y mayor que 1: "))
    
#si el numero es par y esta en el rango de 2 a 5 is NOT weird
if n % 2 == 0 and n in range(2, 5):
    print("Not weird")
    
#si el numero es par y esta en el rango de 6 a 20 is weird
elif n % 2 == 0 and n in range(6, 20):
    print("Weird")

#si el numero es par y es mayor que 20 is NOT weird
elif n % 2 == 0 and n > 20:
    print("Not weird")
    
#si el numero es impar is Weird
elif n % 2 != 0:
    print("Weird")
        



