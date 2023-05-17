import mysql.connector 
from mysql.connector import Error

# class Conectar_Base_de_Datos():
#     def __init__(self):
#         try:
#             print("Hol Mundo")
#             self.conexion = mysql.connector.connect(
#                 host= 'localhost',
#                 port= 3306,
#                 user= 'root',
#                 password= '2468vale',
#                 db='bd_ejemplo_innova',
#             )
#             print("Hol Mundo")
#         except mysql.connector.Error as descripcionError:
#             print("No se conecto la base de datos", descripcionError)


class DAO():
    def __init__(self):
        try:
            self.inmobiliaria =  mysql.connector.connect(
                host='mgalarmasserver1.ddns.net',                           # direccion de la base de datos
                database='inmobiliaria',                                    # nombre de la base de datos
                user='ispc_',                                   # usuario de la bd
                password='ispc_inmobiliaria')                               # password de la bd
            if self.inmobiliaria.connect():                                 # condicional de inmobiliaria
                db_Info = self.inmobiliaria.get_server_info()               # informacion de servicio
                print()                                                     # salto de linea
                print("Conexion Exitosa !!! ")                              # imprimo mensaje
                print("Version: ", db_Info)                                 # imprimo mensaje + db_Info
                cursor = self.inmobiliaria.cursor()                                # inicio cursor de la bd
                cursor.execute("select database();")                        # selecciono la base de datos declarada
                record = cursor.fetchone()                                  # grabo en record el retorno de cursor
                print("Conectado a la base de datos: ", record)             # imprimo mensaje + nombre de la BD conectada
                print()                                                     # salto de linea
        except ValueError as e:                                             # exception error
            print("No de pudo conectar a la base de datos !!", e)
    