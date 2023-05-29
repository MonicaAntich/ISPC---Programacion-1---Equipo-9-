
import mysql.connector

class Conectar():

    def __init__(self) -> None:
        try:
            conexion = mysql.connector.connect(
                host = 'brokergrupo6.ddns.net',
                port = 3306,
                user = 'grupo9',
                password = 'grupo9',
                db='bd_big_bread'
            )
            if conexion.is_connected():
                print("LA CONEXION FUE EXITOSA")

        except:
            print("NO SE PUDO CONECTAR A LA BASE DE DATOS")

        finally:
            if conexion.is_connected():
                conexion.close()
                print("LA CONEXION FUE CERRADA")