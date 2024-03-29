# Ejercicios Listas - Crear Cuatro listas
import random
import time
from colorama import init,Fore,Back,Style 
init(autoreset=True)


#Lista con nombres de la familia
print(Fore.GREEN+Style.BRIGHT+"""\n***** La familia *****""")
familia = ['Valentina', 'Mario', 'Hannah', 'Monica', 'Alicia', 'Luis', 'Carlos', 'Hilda', 'Miguel', 'Leonor']
time.sleep(1)
print(familia)
#Quitar de la lista familia a los abuelos
print(Fore.GREEN+Style.BRIGHT+"""\n*****Sacar de la lista a los abuelos*****""")
del (familia[6:10])
time.sleep(1)
print(familia)
familia1 = ['Valentina', 'Mario', 'Hannah', 'Monica', 'Alicia', 'Luis', 'Carlos', 'Hilda', 'Miguel', 'Leonor']
#Ordenar alfabeticamente la lista con nombres de la familia
print(Fore.GREEN+Style.BRIGHT+"""\n *****La familia ordenada alfabeticamente*****""")
familia1.sort()
time.sleep(1)
print(familia1)
print(Fore.BLUE+Style.BRIGHT+"""\n****************************************************************************************************""")
#Lista con los valores de temperatura del mes de Junio
#junio = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16','17', '18','19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
print(Fore.GREEN+Style.BRIGHT+"""\n *****Las temperaturas del mes de Junio*****""")
temperaturamaxjunio = [ '15°', '18°', '10°', '12°', '08°', '11°', '17°', '09°', '12°', '07°', '15°', '13°', '22°', '12°', '05°', '08°', '17°', '08°', '10°', '07°', '11°', '17°', '09°', '12°', '07°', '15°', '13°', '25°', '12°', '05°']
time.sleep(1)
print(temperaturamaxjunio)
#Ordenar ascendentemente las temperaturas
print(Fore.GREEN+Style.BRIGHT+"""\n*****Las temperaturas ordenadas de forma ascendente*****""")
temperaturamaxjunio.sort()
time.sleep(1)
print(temperaturamaxjunio)
#Agregar temperaturas
print(Fore.GREEN+Style.BRIGHT+"""\n*****Agregar temperaturas*****""")
temperaturamaxjunio.extend(['35°', '28°', '14°', '12°','17°', '18°', '10°', '11°','16°', '18°', '19°', '22°','25°', '38°', '12°'])
time.sleep(1)
print(temperaturamaxjunio)
print(Fore.BLUE+Style.BRIGHT+"""\n****************************************************************************************************""")
#Lista con nombres de ciudades visitadas
print(Fore.GREEN+Style.BRIGHT+"""\n*****Ciudades visitadas*****""")
ciudades = ['Mina Clavero', 'Alta Gracia', 'Rio Tercero', 'Villa Maria', 'San Francisco', 'Bell Ville', 'Laboulaye']
time.sleep(1)
print(ciudades)
print(Fore.GREEN+Style.BRIGHT+"""\n*****La ciudad que menos me gusto*****""")
time.sleep(1)
print(ciudades[5])
del ciudades[5]
print(Fore.GREEN+Style.BRIGHT+"""\n*****Ciudades que si me gustaron*****""")
time.sleep(1)
print(ciudades)
print(Fore.BLUE+Style.BRIGHT+"""\n****************************************************************************************************""")
#Lista con fechas y eventos importantes
fechasimportantes = ['02/08/2000 Nacimiento Valentina', '18/10/1986 Noviazgo con Mario', '01/08/1994 Primer trabajo' ]
print(Fore.GREEN+Style.BRIGHT+"""\n*****Fechas importantes*****""")
time.sleep(1)
print(fechasimportantes)
print(Fore.BLUE+Style.BRIGHT+"""\n****************************************************************************************************""")

#Ejercicios Tuplas
#Crear tres tuplas con datos random y tambien crear una lista que las ontenga y mostrarla

fechasvs=('15 de Enero', '10 de Marzo', '25 de Mayo', 'Vacaciones', 'Comienzo de clases', 'Fecha Patria')
print(Fore.GREEN+Style.BRIGHT+"""\n*****Tupla Fechas varias*****""")
time.sleep(1)
print(fechasvs)
cumpleaños=('09/08 Valentina', '12/02 Mario', '29/09 Monica', '02/09 Alicia', '10/08 Luis', '27/09 Hannah')
print(Fore.GREEN+Style.BRIGHT+"""\n*****Tupla Cumpleaños*****""")
time.sleep(1)
print(cumpleaños)
persona=('23', 'Valentina', 'Perez', 'Signo: Leo', 'Hobbie: Bailar')
print(Fore.GREEN+Style.BRIGHT+"""\n*****Tupla Datos de una persona*****""")
time.sleep(1)
print(persona)
datosvarios=[fechasvs + cumpleaños + persona]
print(Fore.GREEN+Style.BRIGHT+"""\n***** Lista que contiene las tuplas*****""")
time.sleep(1)
print(datosvarios)
print(Fore.BLUE+Style.BRIGHT+"""\n****************************************************************************************************""")
#Diccionario
#Crear diccionario, con dni como claves y el valor solo el nombre
print(Fore.GREEN+Style.BRIGHT+"""\n***** Datos personales nucleo familiar*****""")
datospersonales={'22372219': 'Monica', '42693265':'Valentina', '21394943':'Mario' }
time.sleep(1)
print(datospersonales)
print(Fore.GREEN+Style.BRIGHT+"""\n***** Datos personales familia ampliada*****""")
datospersonales['5455215']='Alicia'
datospersonales['7958452']='Luis'
datospersonales['3154526']='Carlos'
datospersonales['1234567']='Miguel'
datospersonales['3216458']='Leonor'
datospersonales['44444444']='Hannah'
time.sleep(1)
print(datospersonales)

#Diccionario con claves autogeneradas y valores de nros de telefono

 #Creo un diccionario vacio y luego se genera 5 claves y le asigno los numeros de telefono
print(Fore.GREEN+Style.BRIGHT+"""\n***** Agenda telefonica*****""")
agenda = {}
for i in range(5):
    clave = random.randint (1, 100)
    telefono = random.randint (100000000, 999999999)
    agenda[clave] = telefono
time.sleep(1)
print(agenda)
print(Fore.BLUE+Style.BRIGHT+"""\n*********************************************** FIN ************************************************""")
