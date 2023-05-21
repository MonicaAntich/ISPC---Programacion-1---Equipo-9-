import mysql.connector 
#from mysql.connector import Error

#class Conectar_Base_de_Datos():
    #def __init__(self):
        #try:
            #print("Hol Mundo")
conexion = mysql.connector.connect(
                host= 'localhost',
                port= 3306,
                user= 'root',
                password= '',
                db='bd_ejemplo_innova'
            )
print("Conexion exitosa")
        #except mysql.connector.Error as descripcionError:
           #print("No se conecto la base de datos", descripcionError)



