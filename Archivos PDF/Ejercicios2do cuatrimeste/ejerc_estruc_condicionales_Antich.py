



from colorama import init,Fore,Back,Style #Para mostrar una separacion entre ejercicios
init(autoreset=True)
print(Fore.GREEN+Style.BRIGHT+"""\n****************************************************""")
# #1. Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir:
# #  ¡Usted ha ganado el sorteo!

numero = int(input("Ingrese un numero del 1 al 10 para saber si gano el sorteo: ")) #Se pide al usuario que ingrese un numero
if numero == 10: #Si el nro es igual a 10, se cumple la condicion
    print("Usted ha ganado el sorteo") #Se muestra por consola el resultado solicitado
else:
    print("Ese no es el numero ganador")    

print(Fore.GREEN+Style.BRIGHT+"""\n****************************************************""")

# #2. Sumar al ejercicio anterior, una pregunta: Si el número es menor imprimir: ¡Falto un poco,
# #seguí participando! Si es mayor, imprimir: ¡Te pasaste, a seguir intentando!

numero = int(input("Ingrese un numero del 1 al 10 para saber si gano el sorteo: "))#Se pide al usuario que ingrese un numero
if numero == 10: #Si el nro es igual a 10, se cumple esta condicion
    print("Usted ha ganado el sorteo")
elif numero < 10: #Si el nro es menor a 10, se cumple esta condicion
    print("¡Falto un poco, seguí participando!")
else :
    print("¡Te pasaste, a seguir intentando!")

print(Fore.GREEN+Style.BRIGHT+"""\n****************************************************""")

# #3. Pedirle al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
# #mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
# #ingresado no es ninguno de esos, imprimir otro mensaje.

dia_semana = str(input("Ingrese un dia de la semana en letras, ej: lunes: "))#Se pide al usuario que ingrese un dia de la semana en letras
if dia_semana == "lunes":
    print("Lunes, a trabajar" )# De acuerdo a la condicion anterior, es el cartel q va mostrar
elif dia_semana == "viernes":
    print("usted ingreso viernes, ultimo dia de la semana")# De acuerdo a la condicion anterior, es el cartel q va mostrar
elif dia_semana == "sabado":
    print ("Usted ingreso sabado, y el cuerpo lo sabe")# De acuerdo a la condicion anterior, es el cartel q va mostrar
elif dia_semana == "domingo":
    print("Usted ingreso domingo, a disfrutar con la familia")# De acuerdo a la condicion anterior, es el cartel q va mostrar
else :
    print("Usted no ingreso un dato valido") # De acuerdo a la condicion anterior, es el cartel q va mostrar

print(Fore.GREEN+Style.BRIGHT+"""\n****************************************************""")

# #4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje
# #“es vocal”.

letra = str(input("Ingrese una vocal: "))#Se pide al usuario que ingrese una vocal
if letra in ["a", "e", "i", "o","u"]: 
    print("Usted ingreso una vocal", letra) #Si se cumple la condicion de ingresar una vocal, muestra este cartel
else:
    print("Usted ingreso una consonante: ", letra, " ¡debe ingresar una vocal!")#Si no se cumple la condicion, muestra este cartel 

print(Fore.GREEN+Style.BRIGHT+"""\n****************************************************""")    


# Ejercicios Estructuras Repetitivas:
# Resolver cada enunciado utilizando las estructuras FOR – WHILE, según usted crea
# correspondiente:

# 1. Escribir un programa que realice la sumatoria de los números que se quiera hasta que se ingrese -1.

suma=0 #Primero las variables en 0
numeros=0 
while numeros != -1: #Este bucle se ejecutara hasta q se introduzca un -1
    numeros = int(input("Ingrese numeros para sumar entre si, NOTA:si ingresa -1 se termina de sumar: "))#Se pide al usuario que ingrese un numero distinto de -1
    if numeros != -1: #ACA se verifica si el nro ingresado es distinto de -1
        suma+= numeros #Si el nro es diferente de -1, se suma a la variable suma
print ("LA SUMA ES: ", suma) #Se muestra x consola la suma de los nros ingresados  

print(Fore.GREEN+Style.BRIGHT+"""\n****************************************************""")  

# 2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a
# introducir). El programa debe informar de cuantos números introducidos son mayores que
# 0, menores que 0 e iguales a 0.

#  Pido la cantidad de números a introducir
cant_num = int(input("Ingrese la cantidad de números a introducir: "))

# Inicializo los contadores que voy utilizar
mayor= 0
menor = 0
igual= 0

# Pido los números y cuento cuántos son mayor, menor o igual a cero
i = 0 #Inicializo la variable
while i < cant_num: #Mientras se cumpla la condicion cant_num
    numero = float(input(f"Ingrese el número {i+1}: ")) #Float para que tome los numeros negativos y {i+1} para saber en q numero introducido va
    if numero > 0:
        mayor += 1
    elif numero < 0:
        menor += 1
    else:
        igual += 1
    i += 1 # Empieza con i=0 y aca incrementa en uno

# Para que se vean los resultados
print("La cantidad de números ingresados mayores a cero es : ", mayor)
print("La cantidad de números ingresados menores a cero es : ", menor)
print("La cantidad de números ingresados iguales a cero es : ", igual)

print(Fore.GREEN+Style.BRIGHT+"""\n****************************************************""")  

# 3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso
# contrario, el programa termina cuando se introduce un cero.
caracter = (input("Ingrese un caracter para saber si es o no una vocal, con O (cero) para terminar: "))# Pido un caracter
while caracter != "0": #Mientras caracter es distinto de cero, el algoritmo sigue pidiendo
    if caracter in "aeiouAEIOU": #Pregunta si es o no vocal, y habilta para minus o mayus
        print("Usted ingreso una vocal", caracter) 
    else:
        print("Usted NO ingreso una vocal! ")   
    caracter = (input("Ingrese un caracter o O (cero) para terminar: "))# Pido un nuevo caracter

print(Fore.GREEN+Style.BRIGHT+"""\n****************************************************""") 

# 4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la
# media de todos los números introducidos.

suma1=0 #Inicializo las variables suma1, conta y prom a cero
conta = 0
prom = 0

while True: #Creo un bucle while que se ejecutara hasta que se ingrese un cero
    num = int(input("Ingrese numeros para sumar entre si, NOTA:si ingresa 0 se termina de sumar: "))#Pido al usuario que ingrese un nro
    if num == 0: #Verifica si el numero ingresado es cero. Si es cero sale del bucle
        break #Cierro el ciclo while
    suma1 += num #Si el nro ingresado no es cero, se agrega a la suma y se aumenta el contador
    conta += 1
if conta > 0: #Aca se verifica si se ingreso un nro
        
    prom= suma1/conta #si se ingresa un nro, se calcula la media/promedio y se muestra por pantalla con la suma
    
print ("La SUMA es: ", suma1)  
print("La MEDIA de los numeros ingresados: ", prom)  

print(Fore.GREEN+Style.BRIGHT+"""\n****************************************************""") 