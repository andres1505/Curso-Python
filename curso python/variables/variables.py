#Las variables son espacios que se almacenan en la memoria de nuestro programa

#Es una variable porque puede cambiar
#definicion de una variable
numero = 10
numero += 5 
numero -= 5
#el += dice que al valor que ya tiene la variable le sume lo que se le asigna asi mismo con el -= que resta el valor al que ya tiene
print(numero)


#definicion de una variable
nombre = "Andres"

#definicion de una variable con camelCase
nombreCompleto ="Juan Luna"

#definicion de una variable con snake_case y la mas recomendable
nombre_completo ="Juan Luna"

#f strings cambia todos los datos a textos
#concatenar con f-strings
bienvenida = f"Hola {nombre} como estas"

#concatenar con +
bienvenida = "Hola " + nombre + " como estas"
print(bienvenida)

del nombre #borra la variable
print(bienvenida)

#operadores de pertencia (in / not in)
#nos dan como respuesta True o False
print("ola" in bienvenida)#busca esa parte del texto en la variable
print("pedro" in bienvenida)#busca esa parte del texto en la variable en este caso es False

print("pedro" not in bienvenida)#me dice si no esta en la variable
#Son operadores de pertenecia. Me dicen si esta o no estan en la variable
#python es un lenguaje sencible a mayusculas y minisculas
