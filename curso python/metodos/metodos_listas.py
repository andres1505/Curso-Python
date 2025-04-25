
#Creando una lista con el constructor list()
lista = list([5, 32, 100, 525, 21])


#Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append(65)

#agregando un elemento a la lista con un indece en especifico
lista.insert(2, True)

#agregando varior elementos a la lista
lista.extend([2030])

#eliminando un elemento de la lista por su indice
lista.pop(-1)#nos elimna el ultimo elemento de la lista, -2 para el anteultimo, -3 para el anteultimo y asi sucesivamente

#remueve un elemento de la lista por su valor
lista.remove(5)#si no existe lanza una excepcion

#Elimina todo los elementos de la lista
#lista.clear()

#organiza la lista de menor a mayor
#si usamos el parametro reverse=True lo hace de mayor a menor
lista.sort()

#invierte los elementos de la lista
lista.reverse()

#devuelve el indice del primer elemento que coincide con el valor dado
elemento_encontrado = lista.index(525)
print(lista)
