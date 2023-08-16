"""Ejercicios Estructuras Condicionales:
Resolver cada enunciado utilizando las estructuras IF – ELSE – ELIF, según usted crea correspondiente:
1. Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir: ¡Usted ha ganado el sorteo!
2. Sumar al ejercicio anterior, una pregunta: Si el número es menor imprimir: ¡Falto un poco, seguí participando! Si es mayor, imprimir: ¡Te pasaste, a seguir intentando!
3. Pedirle al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.
4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”."""

#1
# numero = int(input("Ingrese un numero: "))
# if numero == 10:   
#     print("¡Usted ha ganado el sorteo!")

#2
# elif numero <= 9:
#     print("¡Falto un poco, seguí participando! ")
# else:
#     print("Te pasaste, a seguir intentando!")

#3
# dia=input("Ingrese un día de la semana: ").lower()
# if dia =="lunes":
#      print("Lunes: ¡Arranca la semana!")
# elif dia == "viernes":
#     print("Viernes: ¡La noche esta en pañales!")
# elif dia == "sabado":
#     print("Sabado de viaje!")
# elif dia == "domingo":
#     print("¡Domingo de familia")
# elif dia == "martes" or dia == "miercoles" or dia == "jueves":
#     print("¡"+dia +" de chambear!")    
# else:
#      print("¡"+dia +" no existe!")
    
#4  
# letra = input("Ingrese una letra: ").lower()
# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#     print(letra +" es vocal")
# else:
#     print(letra +" no es vocal")



"""Ejercicios Estructuras Repetitivas:
Resolver cada enunciado utilizando las estructuras FOR – WHILE, según usted crea correspondiente:

1. Escribir un programa que realice la sumatoria de los números que se quiera hasta ingresar hasta que se ingrese -1.
2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un cero.
4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos."""

# 1
# print("\nCuando quiera finalizar ingrese -1")
# suma=0
# while True:
#     nro= int(input("Ingrese un número:"))
#     if nro == -1:
#         break  
#     suma+=nro
# print("\n El resultado es: " +str(suma))
        
#2
# mayores=0
# menores=0
# iguales=0
# bucle = int(input("Ingrese cuantos números utilizara: "))
# for i in range(bucle):
#     numero = int(input("Ingrese número {}: ".format(i+1)))
    
#     if numero > 0:
#             mayores+= 1
#     elif numero < 0:
#             menores += 1
#     else:
#             iguales+=1
# print("\nHay {} números mayores, {} menores  y {} iguales a [0].".format(mayores, menores, iguales))

#3
# while True:
#     letra = input("Ingrese un carácter: ").lower()
#     if letra == 0:
#         break  
#     if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#         print(letra +" VOCAL")
#     else:
#         print(letra +" NO VOCAL")

# 4
# print("\nCuando quiera finalizar ingrese 0")
# suma=0
# cantidadIngresada=0
# media=0
# while True:
#     nro= int(input("Ingrese un número para sumar: "))
#     if nro == 0:
#         break  
#     suma+=nro
#     cantidadIngresada+=1
    
# media=suma/cantidadIngresada
# print("\n El resultado es: " +str(suma))
# print("\n La media de todos los números es: {}".format(media))