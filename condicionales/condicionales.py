'''las condicionasle son estructuras de control, nos ayuda para comparar valores tanto para verdaderos como para falsos, '''

# numero = int(input("digite un numero: "))

# if numero >0:
#     print("el numero es positivo")     #a identacion son los espacios que maneja desde mi condicional hasta mi print
# elif numero == 0:
#     print("el numero es '0' ")
# else:
#     print("el numero es negativo")

# print("fin de programa ")


"--------------------condicionales combinados y anidados con operadores logicos y relacionales----------------------------------- "

# edad = int(input("digite su esdad: "))

# if edad>=0 and edad<100:
#     print("edad correcta")
#     if edad>=18:
#         print("es mayor de edad")

# else:
#     print("edad incorrecta ")



"------------------------------------------------------------------------------------------------------"

'''hacer un programa que pida dos numeros y se de cuenta cual de ellos es par, o si ambos sos '''


# num1 = int(input("ingrese un mumero: "))
# num2 = int(input("ingrese un segundo numero: "))

# if num1%2 == 0 and num2%2 == 0:
#     print("ambos son pares")
# elif num1%2 == 0 and num2%2!=0:
#     (f"{num1} es par")
# elif num1%2!=0 and num2%2 == 0:
#     print(f"{num2} es par")
# else:
#     print("ambos son impares")



"-------------------hacer un programa que pida tre numeros y determine el mayor----------------------------"


# num1 = int(input("ingrese un numero: "))
# num2 = int(input("ingrese el segundo numero: "))
# num3 = int(input("ingrese el tercer numero: "))


# if num1 >= num2 and num1 >= num3:
#     print(f"el numero uno es mayorporque es {num1}")
# elif num2 >= num1 and num2 >= num3:
#     print (f"el numero dos es mayoro porque es {num2}")
# elif num3 >= num1 and num3 >= num2:
#     print(f"el numero 3 es mayor porque es {num3}")
# elif num1 == num2 and num2 == num3:
#     print("los tres on iguales ")


"-----------------------hace un programa que pida un caracter e indique si es una vocal o no--------------------------------"

# vocal = input("escriber un caracter: ")

# if vocal == "a":
#     print(f"su caracter es una vocal {vocal}")
# elif vocal == "e":
#     print(f"su caracter es una vocal {vocal}")
# elif vocal == "i":
#     print(f"su caracter es una vocal {vocal}")
# elif vocal == "o":
#     print(f"su caracter es una vocal {vocal}")
# elif vocal == "u":
#     print(f"su caracter es una vocal {vocal}")
# else:
#     print("no es un vocal")

"---------paso 2------------"

letra = input("digite un caracter: ").lower()              #el .lower() nos convierte el caracter a minuscula si estas escribiendo en mayuscula y recordar que el upeer() la convierte a mayuscula 

if letra == "a" or letra =="e" or letra =="i" or letra =="o" or letra == "u":
    print ("es vocal")
else:
    ("no es una vocal")