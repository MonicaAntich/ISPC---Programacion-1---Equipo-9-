# TODAS LAS CLASES DEL PROYECTO
import mysql.connector


class Productos:
    def __init__(self, id_producto, receta, nombre) -> None:
        self.id_producto = id_producto
        self.receta = receta
        self.nombre = nombre

    def getid_producto(self):
        return self.id_producto
    def getreceta(self):
        return self.receta
    def getnombre(self):
        return self.nombre

    def setid_producto(self, id_producto):
        self.id_producto = id_producto
    def setreceta(self, receta):
        self.receta = receta
    def setnombre(self, nombre):
        self.nombre = nombre
    def __str__(self) -> str:
        return self.id_producto + self.receta + self.nombre 

class ConectarProductos:
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'brokergrupo6.ddns.net',
                port = 3306,
                user = 'grupo9',
                password = 'grupo9',
                db='bd_big_bread'
            )
        except mysql.connector.Error as descripcionError:
            print("No se pudo conectar debido: ", descripcionError)

    def listarProductos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM productos;"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("No se pudo conectar! debido: ", descripcionError)

    def insertarProductos(self, producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO productos VALUES(NULL,%s,%s);"

                datos = (producto.getreceta(),
                         producto.getnombre())

                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Producto insertada correctamente")

            except mysql.connector.Error as descripcionError:
                print("No se pudo conectar! debido: ", descripcionError)

    def eliminarProductos(self, producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM productos WHERE id_producto = %s;"

                datos = (producto.getid_producto(),)
                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Pizza eliminada correctamente")
            except mysql.connector.Error as descripcionError:
                print("No se pudo conectar! debido: ", descripcionError)

#-----------------------------------------------------------------------------------------------------------------------------------------------------

class NombreClase:
    def __init__(self, atributo1, atributo2) -> None:
        self.atributo1 = atributo1
        self.atributo2 = atributo2
        
    def getatributo1(self):
        return self.atributo1
    def getatributo2(self):
        return self.atributo2

    def setatributo1(self, atributo1):
        self.atributo1 = atributo1
    def setatributo2(self, atributo2):
        self.atributo2 = atributo2

    def __str__(self) -> str:
        return self.atributo1 + self.atributo2

class ConectarNombreClase:
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'brokergrupo6.ddns.net',
                port = 3306,
                user = 'grupo9',
                password = 'grupo9',
                db='bd_big_bread'
            )
        except mysql.connector.Error as descripcionError:
            print("No se pudo conectar debido: ", descripcionError)

    def listarNombreClase(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM nombreDeLaTabla;"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("No se pudo conectar! debido: ", descripcionError)

    def insertarNombreClase(self, parametros): 
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO nombreDeLaTabla VALUES(NULL,%s,%s);" #El null sería el id que se pone solo cuando insertamos un dato. Cada atributo que se agregue en datos, debera llevar una %s en la sentencia

                datos = (parametros.atributo1(),
                         parametros.atributo2())

                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Dato insertado correctamente")

            except mysql.connector.Error as descripcionError:
                print("No se pudo conectar! debido: ", descripcionError)

#-----------------------------------------------------------------------------------------------------------------------------------------------------

