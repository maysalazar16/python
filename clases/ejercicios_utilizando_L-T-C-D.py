'''escribe un programa que tenga dos listas y que, acontinuacion, cree las siguientes listas( en las que no debe haber repeticiones)

>Listas de los elementos que aparecen en las dos listas
>listas de elementos que aperecen en la primera lista, pero no en la segunda
>lista de elementos que aperecen en  la segunda lista , pero no en la primera
>liste de elementos que aparecen en ambas listas '''



# lista1 = [1,2,3,4,5,4,3,2,1,5]
# lista2 = [4,5,6,7,8,4,5,6,7,7,8]

# # elimiene los elementos que estan repetidos en las listas

# a = set(lista1)                         # esta forma convierto listas en conjuntos 
# b = set(lista2)

# union = list(a | b)             #elementos que aparecen en las dos listas          
# soloa = list(a - b)             # elementos que aperecen en la primera lista, pero no en la segunda
# solob = list( b - a)            # elementos que aperecen en  la segunda lista , pero no en la primera
# interseccion = list(a & b)      # elementos que aparecen en ambas listas 



# print(f"elementos que aparecen en las dos listas  {union}")
# print(f"elementos que aperecen en la primera lista, pero no en la segunda {soloa}")
# print(f"elementos que aperecen en  la segunda lista , pero no en la primera {solob}")
# print(f"elementos que aparecen en ambas listas {interseccion}")



# //////////////////////////////////////////////////////////////////////////////////////////////////////////

'''escriba un programa donde cree uana lista con los  siguientes peronajes del señor de los anillos 
nombre: aragorn
clase: guerrero
raza dunadan del norte

nombre: legolas
clase: arquero
raza: elfo sindar

nombre: candalf
clase: mago
raza: istar'''

# señor_de_los_anillos = {"Aragon":["guerra","dunada del norte"],"Legolas":["arquero","elfo sindar"],"Camdalf":["mago","istar"]}

# print(señor_de_los_anillos["Aragon"])
# print(señor_de_los_anillos["Legolas"])
# print(señor_de_los_anillos["Camdalf"])

# personaje = []                # crea la lista vacia 

# p = {"nombre":"Aragon","clase":"guerro","raza":"dunadan del norte"}
# personaje.append(p)              # agrega un disccionario a la lista 

# p = {"nombre":"Legolas","clase":"arquero","raza":"elfo sinda"}
# personaje.append(p)

# p = {"nombre":"Candal","clase":"mago","raza":"istar"}
# personaje.append(p)

# print(personaje)



'''***************************** ejercicios de listas y tuplas **********************************'''


'''escriba un programa que almanecene las asignaturas de un curso por ejemplo (matematicas, fisica, quimica, historia, religion )'''

# asignatura = ["matematicas","fisica","quimica","historia","religion"]

# print(asignatura)



'''escribe un programa que almacene las asignaturas de un curso por ejemplo (matematicas, fisica, quimica, historia, religion ) en una lista
y muestre por pantalla el mensaje "yo estudio <asignatura>, donde asignatura es cada una de las asignaturas de la lista "'''

# asignatura = ["matematicas","fisica","quimica","historia","religion"]

# for asignatura in asignatura:
#     print("yo estudio" + asignatura)




