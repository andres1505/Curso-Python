#son datos que tienen otros datos por dentro

#listas
#creando una lista (se puede modificar)
lista = ["Andres luna","HOLAA", True, 1.75]
print(lista[1])

#creando una tupla (no se puede modificar)
tupla = ("Andres luna","HOLAA", True, 1.75)#las tuplas no se pueden modificar
print(tupla[1])

#esto es valido
lista[1] = "Luna"
print(lista[1])

#esto no
#tupla[2] ="sapa"
#print(tupla[2])

#creando un conjunto (set)
conjunto = {"Andres luna","HOLAA", True, 1.75} #no tienen un orden fijo

#conjunto[1] = "pedrin" No se pueden modificar elementos
#(No se accede a los elementos por indice, no almacena datos duplicados)
conjunto = "jajaj maquina te jodi" 
#print(conjunto[2]) -> no puede accecder al elemento

#creando un diccionario (dict)
#la estructura del diccionario es key :value y separamos con comas
diccionario = {
    'nombre' : "Andres Luna",
    'canal' : "Krait",
    'altura' : 1.75,
    'dato_duplicado' : "Andres Luna"    
}
print(diccionario['nombre'])


