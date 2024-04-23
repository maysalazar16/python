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

'''escribe un programa para una empresa que tiene salas de juegos para todas las edades
y quiere calcular de forma automatica el precio que debe cobrar a sus clientes por entrar. el programa debe pregutnar al usuario la edad del cliente
y mostrar el precio de la entrada. si el cliente es menor de 4 años puede entrar gratis. si tiene entre 4 y 18 años debe pagar 5EUROS
y si es mayor de 18 años debe pagar 18 euros'''

edad = int(input("ingrese su edad: "))

if edad == 0 and edad <= 4 :
    print(f"usted tiene {edad} años y puede entrar gratis")
elif edad > 4 and edad <18:
    print(f"su edad es de {edad} años, debe pagar 5 EUROS en caja ")
elif edad >= 18 and edad <100:
    print(f"usted tiene {edad} años debe para 10 EUROS")
else:
    print(f"no puedes tener {edad} años")


'''hacer un programa que pida al usuario su edad y muestre por pantalla si es mayor de edad o no '''

# edad = int(input("ingrese su edad: "))

# if edad >= 18 and edad < 100:
#     print(f"usted es mayor de edad porque tienen {edad} años")
# elif edad ==0 and edad <= 17:
#     print(f"usted es menor de edad porque tiene {edad} años")
# else:
#     print("esa edad no existe")


'''escribir un programa que almacene la cadena de caracter contraseñ en una variable, preguntar al usuario por la contraseña e imprimir si la contraseña
es correcta o incorrecta, tener encuenta mayusculas y minusculas '''


# contrasena = "S0lut3c2012"

# ingreso = input("ingrese las credenciales del aplicatvio:  ")

# if contrasena == ingreso :
#     print("sus credenciales son crorrectas")
# else:
#     print("sus credenciales son incorrectas")



'''escriba un programa que pida al usuario dos numeros y muestre por pantalla su division si su divisor es cero el progrqmq mostrara error '''

# divisor = float(input("escriba el divisor: "))
# dividendo = float(input("escriba el dividendo: "))

# if divisor == 0:
#     print (f"el divisor es {0} SYSTEN ERROR")
# elif divisor >1:
#     division = divisor/dividendo
#     print(f"el resultado es {division: .2f}")



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

'''para tributar un determinado impuesto se debe ser mayor de 16 año y tener unos ingresos iguales o superiores a  1000 E mensuales.
escribir un programa que pregunte al usuario su edad y sus ingresos mensules y muestre por pantalla si el usuario tiene que tributar o no'''



# edad = int(input("ingrese su edad: "))
# sueldo = float(input("ingrese su sueldo mensual: "))

# if edad >= 16 and sueldo >= 1000:
#     print("usted tiene que tributar")
# elif edad >= 16 and  sueldo < 1000:
#     print(f"usted no tributa, su ingreso es de {sueldo} no es el ingreso minimo para tributar ")
# elif edad < 16 and sueldo >= 1000:
#     print(f"usted no tributa,su edad es {edad} años no es mayor de edad aun ")
# elif edad <16 and sueldo < 1000:
#     print("usted no tiene quee tributar, su edad y su sueldo no son los requeridos ")
        

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

# letra = input("digite un caracter: ").lower()              #el .lower() nos convierte el caracter a minuscula si estas escribiendo en mayuscula y recordar que el upeer() la convierte a mayuscula 

# if letra == "a" or letra =="e" or letra =="i" or letra =="o" or letra == "u":
#     print ("es vocal")
# else:
#     ("no es una vocal")


'''---------construir un programa que simule el funcionamiento de una calculadora que puede realizar las cuatro operaciones aritmeticas basicas
(suma,resta,multiplicacion,division). el usuario debe especificar la operacion con el primer caracter del nombre de la operacion '''


# print ('''*******MENU**************
#        SUME ---  S
#        RESTA ----R
#        MUTIPLICACION O PRODUCTO ---M  o  P
#        DIVISION --- D''')

# letra = input("DIGITE LA OPERACION: ").upper()

# if letra == "S":
#     num1 = float(input("digita un numero: "))
#     num2 = float(input("digita otro numero: "))
#     suma = num1 + num2
#     print (f"\nsu resultado de la suma fue {suma}")
# elif letra == "R":
#     num1 = float(input("digita un numero: "))
#     num2 = float(input("digita otro numero: "))
#     resta = num1 - num2
#     print (f"\nsu resultado de la resta fue {resta}")
# elif letra == "M" or letra == "P":
#     num1 = float(input("digita un numero: "))
#     num2 = float(input("digita otro numero: "))
#     multiplicacion = num1 * num2
#     print (f"\nsu resultado de la multiplicacion fue {multiplicacion}")
# elif letra == "D":
#     num1 = float(input("digita un numero: "))
#     num2 = float(input("digita otro numero: "))
#     division = num1 / num2
#     print (f"\nsu resultado de la resta fue {division:.2f}")       #.2f indica que muestre solo dos decimales
# else:
#     print("esta no es una letra correcta ")



'''hacer un programa que simule un cajero automatico con saldo inicial de $1000 y tendra el siguiente menu de opciones:


1. ingrese dinero en la cuenta
2. Retirar dinero de la cuenta 
3. mostrar dinero disponible
4. salir'''

# print('''\t*CAJERO BANCO FACIL*                            
#         1. ingrese dinero en la cuenta
#         2. Retirar dinero de la cuenta 
#         3. mostrar dinero disponible
#         4. salir\n''')                            # \t hace tabulacion en python

# saldo = (1000)

# opcion = float(input("ingrese la opcion deseada: "))

# if opcion == 1:
#     ingreso= float(input("cuanto dinero desea ingresa: "))
#     saldo += ingreso
#     print (f"su saldo total es de {saldo}")
# elif opcion == 2:
#     retiro = float(input("cunto dinero desea retirar: "))
#     if retiro <= 1000:
#         saldo -= retiro
#         print(f"su retiro fue de {retiro} \n su saldo actual es de {saldo}")
#     else:
#         print (" no cuenta con la cantidad para retirar")
# elif opcion == 3:
#     print(f"USTED CUENTA CON UN SALDO DE {saldo}")
# elif opcion== 4:
#     print("gracias por utilizar BANCO FACIL HASTA LUEGO")
# else:
#     print("la opcion no esta disponible intentalo denuevo ")
    
    
