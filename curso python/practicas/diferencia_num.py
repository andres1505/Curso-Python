
#el strip elimina los espacios en blanco al principio y al final de la cadena
#Se usa STDIN  que es la abreviatura de standard input (entrada estandar)
a = int(input("Introduce un numero:").strip())
b = int(input("Introduce otro numero:").strip())

if a and b in range (1, 10**10):
    print(a+b)
    print(a-b)
    print(a*b)
    
