'''las listas se manjena por medio de corchetes [] 


    0       1        2           3       4                  em python si queremos llamar los elementos de una lista los contamos de 0 en adelante 
"lunes","martes","miercoles","jueves","viernes"
    -5     -4        -3         -2       -1                recordar que si queremos iniciar desde el ultimo al primero utilizamos numeros negativos 

podemos imprimir sublistas mediante el siguiente codigo (lista[0:4])  esto indica que llamaremos las elementos del 0 hasta el 4

podemos almcenar en una lista muchos datos  cadenas numeros enteros , subcadenas booleanos etc
'''

'''*******len******* esta funcion nos indica cuantos elementos tenemos en la lista print(len(lista)) en este ejemplo tenemos 9 elementos'''

# lista = ["lunes","martes","miercoles","jueves","viernes",40,5.67,[1,2,3],True]

# print(len(lista))  



'''****lista.append()**** este metodo agrega elementos al final de la lista '''

'''*******lista.insert() ****se usa para agregar un elemento en un determinado el lugar, recuerda primero colocas la posiciono el indice dond quieres que valla,
 recordar que las posiciones inician desde 0 y luego colocas lo que vas agrerar lista.insert(3,"hola)'''


# lista =[1,2,3,4,5]

# lista.append(6)
# lista.insert(3,"hola may")
# lista.extend([6,7,8])

# print(lista)



'''********lista.extend*********lista.extend([6,7,8]) este metodo se le pasa una lista y la concatena con la lista que ya tenemos 
    tambien podemos sumar listas 
    lista1=[1,2,3,4,5] 
    lista2=[6,7,8,9]
    
    lista3 = lista1+ lista2
    print(lista3)
    esto lo que ara seria sumar las dos listas concatenarlas '''

# lista1 = [1,2,3,4,5]
# lista2 = [6,7,8,9]

# lista3 = lista1 + lista2
# print(lista3)


'''*****in******* lo utilisamos para preguntar a la lista si elvalor esta o no y de esta manera nos dira true verdadero o false falso'''

# lista = [1,2,3,4,5,"salazar"]

# print(3  in lista)
# print("salazar" in lista)
# print(29 in lista)

'''******lista.index********para saber en que indice se ubica dicho elemento utilisamos el metoo index
lista.index(5) aca nos diria en que posicion esta el numero 5 que en nuestro ejemplo estaria en la posicion 4'''

# lista = [1,2,3,4,5,"salazar"]

# print(lista.index(5))
# print(lista.index("salazar"))


'''******count**** este metodo nos indica cuantos valores repetidos tenemos en suestra lista, recordar que nuestra lista puede tener infinidad de valores repetidos 
 '''

# lista = [1,2,3,4,5,"salazar",1,2,3,4,5,6,"salazar"]

# print(lista.count("salazar"))
# print(lista.count(2))


'''****.pop()***** esta funcion elimina los elemento de la lista
lista.pop()  si no colocamos nada en parentesis eliminara el ultimo elemento que encuentre
lista.pop(2)  si colocamos el indice que queremos eliminar eliminaria el numero 3 de nuestra ejemplo de lista '''

# lista = [1,2,3,4,5,"salazar"]

# print(lista.pop())
# print(lista.pop(2))

# print(lista)


'''*****lista.remove****** este metodo lo utilizamos cuando queremos eliminar un elemento de nuestra lista y no sabemos en que indice o posicion se encuentra
lista.remove(4)  elmiminaria directamente el numero 4 de nuestro ejemplo en lista '''

# lista = [1,2,3,4,5,"salazar"]

# print(lista.remove(4))
# print(lista.remove("salazar"))

# print(lista)

'''*****lista.clear********* elimina el total de una lista'''

# lista = [1,2,3,4,5,"salazar"]

# lista.clear()
# print(lista)

# print(lista.clear())

'''****lista.reverse()*****  esto invierte la posicion de la lista, lo ultimo queda de primeras y lo primero de ultimo'''

# lista = [1,2,3,4,5,"salazar"]

# lista.reverse()
# print(lista)



# lista = [1,2,3,4,5,"salazar"] * 2  # copiaria la lista dos veces

# print(lista)



'''*****lista.sort*********  para ordenar los elemento de la lista en orden asendente de menor a mayor
********lista.sort(reverse=True)los ordena de manera desendente de mayor a menos **************'''


lista=[4,8,9,3,2,-7,-3]

lista.sort()
lista.sort(reverse=True)

print(lista)