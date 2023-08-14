import time
import random

# Ejercicios Listas:
# Crear cuatro listas:
print("Nombres de su familia:")
Familia=["Lionel Messi", "Antonela Roccuzzo", "Mateo Messi", "Thiago Messi ", "Ciro Messi", "Eusebio Messi", "Celia Oliveira Cuccittini", "Rosa Maria Pérez", "Antonio Cuccittini"]
print(Familia)
time.sleep(2)
print()  

print("Valores de la temperatura de agosto:")
Agosto=[19, 5, 28, 12, 23, 14, 7, 30, 1, 8, 16, 26, 3, 25, 20, 9, 10, 21, 17, 2, 15, 6, 22, 11, 4, 27, 13, 18, 24, 29]
print(Agosto)
time.sleep(2)
print()  

print("Nombres de ciudades que hayan visitado:")
Ciudades=["Cordoba", "Alta Gracia", "Villa Carlos Paz","Mina Clavero","Villa María"]
print(Ciudades)
time.sleep(2)
print()  

print("Fechas y nombres de eventos importantes de su vida:")
Eventos=["Egreso", "Debut en primera"]
print(Eventos)
time.sleep(2)
print()  

print("Ordenar alfabéticamente la lista de los nombres de familia:")
Familia.sort()
print(Familia)
time.sleep(2)
print()  

print("Ordenar ascendentemente la lista de temperaturas:")
Agosto.sort()
print(Agosto)
time.sleep(2)
print()  
#Agosto.sort(reverse=True)#Para que la lista sea descendente 

print("Agregar en la lista de temperaturas, las temperaturas de los 15 días del mes siguiente:")
Agosto.extend([31,32,33,34,35])
print(Agosto)
time.sleep(2)
print()  

Familia=["Lionel Messi", "Antonela Roccuzzo", "Mateo Messi", "Thiago Messi ", "Ciro Messi", "Eusebio Messi", "Celia Oliveira Cuccittini", "Rosa Maria Pérez", "Antonio Cuccittini"]
print("Quitar de la lista de los nombres de familia, a tus abuelos: ")
del Familia[5:9]
print(Familia)
time.sleep(2)
print()  

print("Quitar de la lista de ciudades la ciudad menos linda que hayas visitado: ")
del Ciudades[4:5]
print(Ciudades)
time.sleep(2)
print()  

print("Mostrar todas las listas: ")
Listas=Familia+Agosto+Ciudades+Eventos 
print(Listas)
time.sleep(2)
print()  

#Ejercicios Tuplas:
print("Crear tres tuplas con datos random:")
tuplaRandom1=('a','e','i','o','u','10-08-2023')
print(tuplaRandom1)
time.sleep(2)
print()

tuplaRandom2=(1,2,3,4,5,6.6, False)
print(tuplaRandom2)
time.sleep(2)
print()  

tuplaRandom3=('Enero',1,'Febrero',2,'Marzo',3,'Abril',4)
print(tuplaRandom3)
time.sleep(2)
print()  

print("Crear una lista que las contenga y mostrarla.")
tuplas=[tuplaRandom1+tuplaRandom2+tuplaRandom3]
print(tuplas)
time.sleep(2)
print()  

#Ejercicio Diccionarios:
print("Crear el siguiente diccionario: Las claves serán los dni de su núcleo familiar, y el valor será SOLO el nombre de la persona.")
FamiliaMessi={19283746:"Lionel", 72819354:"Antonela", 25648901:"Mateo",  87654321:"Thiago", 36987410:"Ciro"}
print(FamiliaMessi)
time.sleep(2)
print()  

print("Luego deberán añadir los datos de familia ampliada (abuelos, familia política, etc)")
FamiliaMessi[43216789]="Eusebio"
FamiliaMessi[75892641]="Celia"
FamiliaMessi[28374956]="Rosa"
FamiliaMessi[61459802]="Antonio"
print(FamiliaMessi)
time.sleep(2)
print()  

#• Crear un nuevo diccionario con claves autogeneradas y valores de números de teléfono.
#Ambos deben ser mostrados.
print("Crear un nuevo diccionario con claves autogeneradas y valores de números de teléfono.")
agenda = {}
for i in range(10):
    clave = random.randint (1, 100)
    telefono = random.randint (100000000, 999999999)
    agenda[clave] = telefono
time.sleep(2)
print(agenda)

