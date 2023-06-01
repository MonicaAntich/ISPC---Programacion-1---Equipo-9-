import Conexion as Conector # esta linea importa el archivo conexion.py con alias conector, sino se invoca da error de base de datos, 

print("Para conectarse a la Base de Datos presione 1")
print("Para cerrar la Base de Datos presione 2")
variableAuxiliar= int(input()) #input deja ingresar un dato
if(variableAuxiliar == 1):
    conn = Conector.Conectar()
else: 
    print("Gracias por cerrar la Base de Datos.")
 
 
 
