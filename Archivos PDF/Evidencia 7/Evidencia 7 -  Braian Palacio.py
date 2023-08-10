# Ejercicios Listas:
# Crear cuatro listas:
# 1. Con los nombres de su familia.
Familia=["Lionel Messi", "Antonela Roccuzzo", "Mateo Messi", "Thiago Messi ", "Ciro Messi", "Eusebio Messi", "Celia Oliveira Cuccittini"
, "Rosa Maria Pérez", "Antonio Cuccittini"]
#2. Con los valores de la temperatura de un mes ent,ero (mes a elección, pero definirlo).
Agosto=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#3. Con los nombres de ciudades que hayan visitado.
Ciudades=["Cordoba", "Alta Gracia", "Villa Carlos Paz","Villa María","Mina Clavero"]
#4. Con las fechas y nombres de eventos importantes de su vida.
Eventos=["Egreso", "Debut en primera"]

#Luego:
#1. Ordenar alfabéticamente la lista de los nombres de familia.
#Familia.sort()

#2. Ordenar ascendentemente la lista de temperaturas.
#Agosto.sort()
#Agosto.sort(reverse=True)#Para que la lista sea descendente 

#3. Agregar en la lista de temperaturas, las temperaturas de los 15 días del mes siguiente.
#Agosto.extend([31,32,33,34,35])

#4. Quitar de la lista de los nombres de familia, a tus abuelos.
#del Familia[5]
#del Familia[5]
#del Familia[5]
#del Familia[5]
#-----------------------------------
del Familia[5:9]


#5. Quitar de la lista de ciudades la ciudad menos linda que hayas visitado.
#del Ciudades[0]
#del Ciudades[0]
#del Ciudades[0]
#del Ciudades[0]
#---------------------------------
#del Ciudades[0:4]

#6. Mostrar todas las listas.
#print(Familia)
#print(Agosto)
#print(Ciudades)
#print(Eventos)

#-----------------------------------
#Listas=Familia +Agosto+Ciudades+Eventos #Agrupa todas las listas en una sola
#print(Listas)


#Ejercicios Tuplas:
#Crear tres tuplas con datos random.
tuplaRandom1=('a','e','i','o','u','10-08-2023')
tuplaRandom2=(1,2,3,4,5,6.6, False)
tuplaRandom3=('Enero',1,'Febrero',2,'Marzo',3,'Abril',4)
#Crear una lista que las contenga y mostrarla.
tuplas=[tuplaRandom1+tuplaRandom2+tuplaRandom3]
#print(tuplas)

#Ejercicio Diccionarios:
#Crear el siguiente diccionario:
# Las claves serán los dni de su núcleo familiar, y el valor será SOLO el nombre de la persona.
#Luego deberán añadir los datos de familia ampliada (abuelos, familia política, etc)
FamiliaMessi={19283746:"Lionel", 72819354:"Antonela", 25648901:"Mateo",  87654321:"Thiago", 36987410:"Ciro"}
FamiliaMessi[43216789]="Eusebio"
FamiliaMessi[75892641]="Celia"
FamiliaMessi[28374956]="Rosa"
FamiliaMessi[61459802]="Antonio"
#print(FamiliaMessi)

# Crear un nuevo diccionario con claves autogeneradas y valores de números de teléfono.
#Ambos deben ser mostrados.

