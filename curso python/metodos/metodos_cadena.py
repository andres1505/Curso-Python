cadena1 = "Hola,Mundo,como,estas"
cadena2 = "Bienvenido crack"

#resultado = dir(cadena1)#dir devulve la lista de atributos validos del objeto

#Los metodos son el DATO.METODO() esta es la estructura de un metodo

#convierte la cadena a mayusculas
resultado = cadena1.upper()

#convierte la cadena a minusculas
resultado = cadena1.lower()

#convierte la primera letra a mayuscula
resultado = cadena1.capitalize()

#buscamos una cadena en otra cadena
busqueda_find = cadena1.find("o") #busca la cadena y devuelve la posicion de la primera letra, si no existe devuelve -1

#Buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
busqueda_index = cadena1.index("a")

#si es numerico devuelve True, si no False, no importa si es un string desde que tenga numeros
es_numerico = cadena1.isnumeric()

#si es alfanumerico devuelve True, si no devuelve False
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena dentro de otra cadena, devulve la cantidad de coincidencias
contar_coincidencias = cadena1.count("o")

#contamos cuantos caracteres tiene la cadena
#len es una funcion
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada si es asi devuelve true, si no false
empieza_con = cadena1.startswith("hola")

#verificamos si una cadena termina con otra cadena dada si es asi devuelve true, si no false
termina_con = cadena1.endswith("o")

#reemplaza un ppedazo de la cadena dada por otra cadena dada
cadena_nueva = cadena1.replace(",", " ")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print((cadena_separada[0])) 