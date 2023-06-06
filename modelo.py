# AQUI VAN TODAS LAS CLASES DEL PROYECTO
import mysql.connector


class Productos:
    def __init__(self, id_producto, nombre) -> None:
        self.id_producto = id_producto
        self.nombre = nombre

    def getid_producto(self):
        return self.id_producto
    def getnombre(self):
        return self.nombre

    def setid_producto(self, id_producto):
        self.id_producto = id_producto
    def setnombre(self, nombre):
        self.nombre = nombre
    def __str__(self) -> str:
        return self.id_producto +  self.nombre 

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
        except mysql.connector.Error as cantidadError:
            print("No se pudo conectar debido: ", cantidadError)

    def listarProductos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM productos;"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)

    def insertarProductos(self, producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO productos VALUES(NULL,%s);"
                datos = (producto.getnombre(),)
                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Producto insertada correctamente")

            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)

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
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)
                
    def buscarProducto(self, id_producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM productos WHERE id_producto = %s;"
                datos = (id_producto,)
                cursor.execute(sentenciaSQL, datos)
                resultados = cursor.fetchone()
                self.conexion.commit()
                self.conexion.close()
                return resultados

            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)

    def modificarProductos(self, producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE productos SET nombre= %s WHERE id_producto=%s;"

                datos = (producto.getnombre(),
                         producto.getid_producto(),)

                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Pizza actualizada correctamente")

            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)

#-------------------------------------------------------------------------------------------------------------------------------------------------

class Recetas:
    def __init__(self, id_receta, pizza_nro,cantidad_insumos, id_insumos) -> None:
        self.id_receta = id_receta
        self.pizza_nro = pizza_nro
        self.cantidad_insumos = cantidad_insumos
        self.id_insumos = id_insumos
         
    def getid_receta(self):
        return self.id_receta
    def getpizza_nro(self):
        return self.pizza_nro
    def getcantidad_insumos(self):
        return self.cantidad_insumos
    def getid_insumos(self):
        return self.id_insumos
 
    def setid_receta(self, id_receta):
        self.id_receta = id_receta
    def setpizza_nro(self, pizza_nro):
        self.pizza_nro = pizza_nro
    def setcantidad_insumos(self, cantidad_insumos):
        self.cantidad_insumos = cantidad_insumos
    def setid_insumos(self,id_insumos):
        self.id_insumos = id_insumos
        

    def __str__(self) -> str:
        return self.id_receta + self.pizza_nro +  self.cantidad_insumos + self.id_insumos

class ConectarRecetas:
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'brokergrupo6.ddns.net',
                port = 3306,
                user = 'grupo9',
                password = 'grupo9',
                db='bd_big_bread'
            )
        except mysql.connector.Error as cantidadError:
            print("No se pudo conectar debido: ", cantidadError)

    def listarRecetas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM recetas;"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)

    def insertarRecetas(self, parametro): 
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO recetas VALUES(NULL,%s,%s,%s);" #El NULL sería el id que se pone solo cuando insertamos un dato. Cada atributo que se agregue en datos, debera llevar una %s en la sentencia
                datos = (parametro.getpizza_nro(),
                         parametro.getcantidad_insumos(), 
                         parametro.getid_insumos())
                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Dato insertado correctamente")

            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)

    def eliminarRecetas(self, parametro):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM recetas WHERE id_receta = %s;"

                datos = (parametro.getid_receta(),)
                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Receta eliminada correctamente")
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)

    def buscarRecetas(self, id_receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM recetas WHERE id_receta = %s;"
                datos = (id_receta,)
                cursor.execute(sentenciaSQL, datos)
                resultados = cursor.fetchone()
                self.conexion.commit()
                self.conexion.close()
                return resultados

            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)

    def modificarRecetas(self, parametro):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE recetas SET pizza_nro= %s, cantidad_insumos=%s, id_insumos=%s  WHERE id_receta=%s;"

                datos = (parametro.getpizza_nro(),
                         parametro.getcantidad_insumos(),
                         parametro.getid_insumos(),
                         parametro.getid_receta(),)

                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Receta actualizada correctamente")

            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)

#-------------------------------------------------------------------------------------------------------------------------------------------------
  
class Insumo:#Creamos el metodo constructor del objeto persona, en python se llama init. Esta es la formula basica de la funcion constructora
    def __init__(self, id_insumos, nombre) -> None:  #Constructor con las variables
        self.id_insumos= id_insumos
        self.nombre = nombre    #Creamos el objeto id y nombre  son parametros, atributos
    # Ahora se crean los setter and getter, porq si creamos un objeto y despues necesitamos hacer cambios no lo podriamos hacer
    # Se crea un set y un get por cada atributo
    def getid_insumos(self):
        return self.id_insumos
    def getnombre(self):
        return self.nombre

    # Los set nos van a permitir definir, lo nuevo q quiera agregar o modificar
    def setid_insumos(self,id_insumos):
        self.id_insumos= id_insumos
    def setnombre(self,nombre):
        self.nombre= nombre
    # El siguiente metodo es para que nos retorne los atributos
    def __str__(self) -> str:
        return self.id_insumos + self.nombre  

#Ahora la clase conexion
class ConectarInsumo:
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'brokergrupo6.ddns.net',
                port = 3306,
                user = 'grupo9',
                password = 'grupo9',
                db='bd_big_bread'
            )
        except mysql.connector.Error as cantidadError:
            print("No se pudo conectar debido: ", cantidadError)
            
    def listarInsumos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM insumos;"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)
                            
    def insertarInsumo(self, insumo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO insumos VALUES(NULL,%s);"
                datos = (insumo.getnombre(),)
                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Insumo insertado correctamente")

            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)               
 
