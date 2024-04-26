'''las TUPLAS son simplemente otro tipo de coleccion que realmente son muy parecidos a las listas, pero con la gran diferencia que las TUPLAS son listas inmutabes
a que me refiero con esto, sencillamente a que no vamos a poder modificsrlas, es decir no vamos a poder añadir nuevos elementos,
no vamos a poder eliminar elementos de las tuplas, ni tampoco modificar los elemento que ya tenemos  

recordar que  las tuplas van en parentesis ()'''

'''son mucho mas rapidas a sus momentos de ejecucion y pues consumen mucho menos memoria que las listas '''


'''          ***NO PODEMOS HACER***                                                             ***SI PODEMOS HACER*** 
.append() = agrega elementos al final de la lista                            print(tupla[1]) = podemos mostrar lo que hay en cada indice
lista[0] = 8  = nos modifica el valor de indice                              print(tupla[1:]) = que nos muestre todos los elemento desde la posicion 1 en adelante
tupla.pop() eliminar un indice de una tupla                                  print(4 in tupla) = busca si el valor de 4 esta en nuestra tupla
tupla.pop() eliminar                                                        .index(()) = indica el indice donde esta dicho elemento ***print(tupla.index(5))***                            
.                                                                           .count(()) = indica cuantas veces esta repetido un valor en la tupla ***print(tupla.count("salazar"))***
.                                                                            list(tupla) combierte nuestra Tupla en una lista '''




# tupla = (4,"hola",6.78,[1,2,3],4)

# print(tupla[-1])
# print(tupla[1:])
# print(4 in tupla)
# print(tupla.index(6.78))
# print(tupla.count(6))

'''tambien podemos transformar listas en tuplas y tuplas en listas '''

# tupla = (4,"hola",6.78,[1,2,3],4)
# lista= list(tupla)                  #la funcion list tranformara nuestra tupla en una lista 

# print(lista)



''''''