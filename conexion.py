import mysql.connector 
from mysql.connector import Error

class Conectar_Base_de_Datos():
    def __init__(self):
        try:
            print("Hol Mundo")
            self.conexion = mysql.connector.connect(
                host= 'localhost',
                port= 3306,
                user= 'root',
                password= '2468vale',
                db='bd_ejemplo_innova',
            )
            print("Hol Mundo")
        except mysql.connector.Error as descripcionError:
            print("No se conecto la base de datos", descripcionError)


