
from colorama import init,Fore,Back,Style 
init(autoreset=True)

#1. Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir:
#  ¡Usted ha ganado el sorteo!
numero = int(input("Ingrese un numero: "))
if numero == 10:
    print("Usted ha ganado el sorteo")

print(Fore.GREEN+Style.BRIGHT+"""\n****************************************************""")

#2. Sumar al ejercicio anterior, una pregunta: Si el número es menor imprimir: ¡Falto un poco,
#seguí participando! Si es mayor, imprimir: ¡Te pasaste, a seguir intentando!

numero = int(input("Ingrese un numero: "))
if numero == 10:
    print("Usted ha ganado el sorteo")
elif numero < 10:
    print("¡Falto un poco, seguí participando!")
else :
    print("¡Te pasaste, a seguir intentando!")

print(Fore.GREEN+Style.BRIGHT+"""\n****************************************************""")

#3. Pedirle al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
#mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
#ingresado no es ninguno de esos, imprimir otro mensaje.
dia_semana = (input("Ingrese un dia de la semana: "))
if dia_semana == "lunes":
    print("Lunes, a trabajar" )
elif dia_semana == "viernes":
    print("usted ingreso viernes, ultimo dia de la semana")
elif dia_semana == "sabado":
    print ("Usted ingreso sabado, y el cuerpo lo sabe")
elif dia_semana == "domingo":
    print("Usted ingreso domingo, a disfrutar con la familia") 
else :
    print("Usted no ingreso un dia valido")

print(Fore.GREEN+Style.BRIGHT+"""\n****************************************************""")

#4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje
#“es vocal”.

letra = (input("Ingrese una letra: "))
if letra in ["a", "e", "i", "o","u"]:
    print("Usted ingreso una vocal", letra) 
else:
    print("Usted ingreso una consonante: ", letra, " ¡debe ingresar una vocal!")   

print(Fore.GREEN+Style.BRIGHT+"""\n****************************************************""")    
