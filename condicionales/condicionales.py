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


num1 = int(input("ingrese un mumero: "))
num2 = int(input("ingrese un segundo numero: "))

if num1%2 == 0 and num2%2 == 0:
    print("ambos son pares")
elif num1%2 == 0 and num2%2!=0:
    (f"{num1} es par")
elif num1%2!=0 and num2%2 == 0:
    print(f"{num2} es par")
else:
    print("ambos son impares")