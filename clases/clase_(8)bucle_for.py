'''bucle FOR son estructuras de codigo que cambian la ejecucion


esta recomentdo para contexti en los que se sabe el numero de iteracione que se van a dar en su ejecucion, es decir, es un bucle que busca ejecutar
un conjunto de instrucciones de forma repetitiva hasta llegar al numero maximo de iteraciones definidas

en python los bucles for se ejecutan sobre elementos iterables, como puden ser listas, tuplas, cadenas de texto, o dicionarios. El numero de teraciones
que se ejecutaran dependera del numero de los elementos de los que esta compiesto el elemento iterable

los bucles for tienen la siguiente sintaxis


for variable in coleccoomIterable:
    .        BloqueInstrucines
    
for: indica el comienzo de un bucle
variabel: vriable que almacena el elemento sobre el que se esta iterand de coleccioniterable
in: indicador wur se utilizs psra definir el elemento itrrable sobre el que se ejecutara el bucle for
ColeccionIterable: elemento sobre el que se ejecuta el bucle
BloqueIstrucciones: conjunto de intrucciones que se ejecuraran en cada cadena '''




#ejemplo


# lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
# for lista in lista :
#     print(lista, end=" ")



# for x in range(0,5):  #range para pango de numero
#     print("hola el numero de X es ", x)

for x in "hola":
    print(x)
#lista

# nombre = ["juan","pedro","elena"]
# print("el tipo de nombre es", type(nombre))     # type indica que tipo es si es tipo lista tipo diccionario
# for nombre in nombre:
#     print("Buenos dias", nombre)

#Tuple

# nombre =("juan", "ana", "elena")
# print("el tipo de nomnre es", type(nombre))
# for nombre in nombre:
#     print("buenos dias ", nombre)


# set    el metodo set altera el orden al momento de imprimir el resultado 

# nombre = {"juan", "ana","elena"}
# print("el tipo de nombre es ", type(nombre))
# for nombre in nombre:
#     print("Buenos dias", nombre)


#Diccionario
# nombre = {"juan" : 1, "ana" : 2, "elena" : 3}
# print("el tipo de nombre es ", type(nombre))
# for nombre in nombre:
#     print("buenos dias", nombre)