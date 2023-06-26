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
                
    def buscarProducto(self, id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM productos WHERE id_producto = %s;"
                datos = (id,)
                cursor.execute(sentenciaSQL, datos)
                r = cursor.fetchone()
                self.conexion.commit()
                self.conexion.close()
                return r

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
    def __init__(self, id_receta, pizza_nro,cantidad_insumos, id_insumos,unidad_de_medida) -> None:
        self.id_receta = id_receta
        self.pizza_nro = pizza_nro
        self.cantidad_insumos = cantidad_insumos
        self.id_insumos = id_insumos
        self.unidad_de_medida = unidad_de_medida
         
    def getid_receta(self):
        return self.id_receta
    def getpizza_nro(self):
        return self.pizza_nro
    def getcantidad_insumos(self):
        return self.cantidad_insumos
    def getid_insumos(self):
        return self.id_insumos
    def getunidad_de_medida(self):
        return self.unidad_de_medida
 
    def setid_receta(self, id_receta):
        self.id_receta = id_receta
    def setpizza_nro(self, pizza_nro):
        self.pizza_nro = pizza_nro
    def setcantidad_insumos(self, cantidad_insumos):
        self.cantidad_insumos = cantidad_insumos
    def setid_insumos(self,id_insumos):
        self.id_insumos = id_insumos
    def setunidad_de_medida(self,unidad_de_medida):
        self.unidad_de_medida = unidad_de_medida
        

    def __str__(self) -> str:
        return self.id_receta + self.pizza_nro +  self.cantidad_insumos + self.id_insumos + self.unidad_de_medida
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
                #sentenciaSQL = "SELECT * FROM recetas;"
                #sentenciaSQL = "SELECT productos.nombre, insumos.nombre, recetas.cantidad_insumos  from recetas  INNER JOIN productos  on recetas.pizza_nro=productos.id_producto INNER JOIN insumos on recetas.id_insumos=insumos.id_insumos;"
                sentenciaSQL = "SELECT a.id_receta, b.nombre, c.nombre, a.cantidad_insumos, a.unidad_de_medida from recetas a INNER JOIN productos b on a.pizza_nro=b.id_producto INNER JOIN insumos c on a.id_insumos=c.id_insumos;"
                
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)
                
    def listarEditarRecetas(self,id_receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL="SELECT a.id_receta, b.nombre, c.nombre, a.cantidad_insumos, a.unidad_de_medida  from recetas a INNER JOIN productos b on a.pizza_nro=b.id_producto INNER JOIN insumos c on a.id_insumos=c.id_insumos WHERE a.id_receta=%s;"
                datos=(id_receta,)
                cursor.execute(sentenciaSQL,datos)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)
                
    def listarRecetasDescripcion(self,pizza_nro):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL="SELECT a.id_receta, b.nombre, c.nombre, a.cantidad_insumos, a.unidad_de_medida  from recetas a INNER JOIN productos b on a.pizza_nro=b.id_producto INNER JOIN insumos c on a.id_insumos=c.id_insumos WHERE b.id_producto=%s;"
                datos=(pizza_nro,)
                cursor.execute(sentenciaSQL,datos)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)

    def insertarRecetas(self, parametro): 
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO recetas VALUES(NULL,%s,%s,%s, %s);" 
                datos = (parametro.getpizza_nro(),
                         parametro.getcantidad_insumos(), 
                         parametro.getid_insumos(), 
                         parametro.getunidad_de_medida())
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
                sentenciaSQL = "UPDATE recetas SET pizza_nro= %s, cantidad_insumos=%s, id_insumos=%s, unidad_de_medida=%s  WHERE id_receta=%s;"

                datos = (parametro.getpizza_nro(),
                         parametro.getcantidad_insumos(),
                         parametro.getid_insumos(),
                         parametro.getunidad_de_medida(),
                         parametro.getid_receta(),)

                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Receta actualizada correctamente")

            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)
#-------------------------------------------------------------------------------------------------------------------------------------------------
  
class Insumo:#Creamos el metodo constructor del objeto Insumo, en python se llama init. Esta es la formula basica de la funcion constructora
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
class ConectarInsumo:#Ahora la clase conexion

    def __init__(self) -> None: #Clase constructora para entrar a la base de datos
        try:
            self.conexion = mysql.connector.connect(    #Aca van los parametros para conectar a la base de datos
                host = 'brokergrupo6.ddns.net',          
                port = 3306,
                user = 'grupo9',
                password = 'grupo9',
                db='bd_big_bread'
            )
        except mysql.connector.Error as cantidadError:  #El except avisa si no se conecto y que error
            print("No se pudo conectar debido: ", cantidadError)
            
    def listarInsumos(self):        #Aca trae todos los datos q tiene la tabla insumos
        if self.conexion.is_connected(): 
            try:
                cursor = self.conexion.cursor()     #se refiere a una estructura de control utilizada para el recorrido (y potencial procesamiento) de los registros del resultado de una consulta
                sentenciaSQL = "SELECT * FROM insumos;" # Se crea una variable (sentencia sql)
                cursor.execute(sentenciaSQL)            # Recupera resultados
                resultados = cursor.fetchall()      #Se crea una variable (resultados) para q almacene todos los datos q nos trajo de la tabla
                self.conexion.close()               #Se cierra la conexion
                return resultados                   #Devuelve los datos en la variable resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)
                            
    def insertarInsumo(self, insumos):       #Aca insertamos datos a la tabla insumos
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO insumos VALUES(NULL,%s);"
                datos = (insumos.getnombre(),)
                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()         #El commit es para confirmar que se insertaron datos
                self.conexion.close()
                print("Insumo insertado correctamente")

            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)  
             
    def eliminarInsumo(self, parametro):       ##Aca eliminamos datos de la tabla insumos
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM insumos WHERE id_insumos = %s;"

                datos = (parametro.getid_insumos(),)
                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Insumo eliminado correctamente")
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)   
     
    def buscarInsumo(self, id_insumos): # Este metodo trabaja como el metodo listar, pero lista solo un dato con su ID
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM insumos WHERE id_insumos = %s;"
                datos = (id_insumos,)
                cursor.execute(sentenciaSQL, datos)
                resultados = cursor.fetchone()
                self.conexion.commit()
                self.conexion.close()
                return resultados

            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)
    
    def modificarInsumo(self, insumo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE insumos SET nombre=%s WHERE id_insumos= %s;" #El porcentaje(%) se utiliza para recibir los parametros

                datos = (                           #Se crea la variable datos para guardar los parametros q se van introducir en la sentencia
                         insumo.getnombre(),        #El get es el metodo con el atributo, donde nos llegan los datos
                         insumo.getid_insumos(),)

                cursor.execute(sentenciaSQL, datos) 
                self.conexion.commit()
                self.conexion.close()
                print("Insumo actualizado correctamente")

            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)                    
     
#-------------------------------------------------------------------------------------------------------------------------------------------------
                
class Produccion_diaria:
    def __init__(self, id_pd, fecha, cantidad, id_producto)->None:
        self.id_pd = id_pd
        self.fecha = fecha
        self.cantidad = cantidad
        self.id_producto = id_producto
    def getid_pd (self):
        return self.id_pd
    def getfecha (self):
        return self.fecha
    def getcantidad (self):
        return self.cantidad
    def getid_producto (self):
        return self.id_producto 
    
    def setid_pd(self, id_pd):
        self.id_pd = id_pd
    def setfecha (self, fecha):
        self.fecha = fecha
    def setcantidad (self, cantidad):
        self.cantidad = cantidad
    def setid_producto (self, id_producto):
        self.id_producto = id_producto
        
    def __str__(self) -> str:
        return self.id_pd + self.fecha + self.cantidad + self.id_producto   
class ConectarProduccion:
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
                        
    def listarProduccion (self):
        if self.conexion.is_connected ():
             try:
                 cursor = self.conexion.cursor()
                 #sentenciaSQL = "SELECT * FROM produccion_diaria; "
                 sentenciaSQL = "SELECT a.fecha, b.nombre, a.cantidad, a.id_pd from produccion_diaria a INNER JOIN productos b on a.id_producto=b.id_producto;"
                 
                 cursor.execute(sentenciaSQL)
                 resultados = cursor.fetchall ()
                 self.conexion.close ()
                 return resultados 
             except mysql.connector.Error as cantidadError:
                print("No se pudo conectar debido: ", cantidadError)
                
    def insertarProduccion (self, parametro):
        
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO produccion_diaria VALUES (NULL, current_timestamp, %s, %s);"
                datos  = (
                        parametro.getcantidad(), 
                        parametro.getid_producto(),)
                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Producción insertada correctamente")
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar debido: ", cantidadError)
                
    def listarInsumosProduccion(self,id_producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL="SELECT a.id_receta, b.nombre, c.nombre, a.cantidad_insumos * d.cantidad,  a.unidad_de_medida   from recetas a INNER JOIN productos b on a.pizza_nro=b.id_producto INNER JOIN produccion_diaria d on b.id_producto=d.id_producto INNER JOIN insumos c on a.id_insumos=c.id_insumos WHERE d.fecha=CURRENT_DATE  and pizza_nro=%s"
                datos=(id_producto,)
                cursor.execute(sentenciaSQL,datos)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)    
                              
    def listarProduccionId(self):
        if self.conexion.is_connected ():
             try:
                 cursor = self.conexion.cursor()
                 #sentenciasql = "SELECT * FROM produccion_diaria; 
                 sentenciaSQL = "SELECT a.id_pd, a.fecha, b.nombre, a.cantidad from produccion_diaria a INNER JOIN productos b on a.id_producto=b.id_producto;"
                 
                 cursor.execute(sentenciaSQL)
                 resultados = cursor.fetchall ()
                 self.conexion.close ()
                 return resultados 
             except mysql.connector.Error as cantidadError:
                print("No se pudo conectar debido: ", cantidadError)
                
    def eliminarProduccion (self, parametro):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM produccion_diaria WHERE id_pd = %s;"

                datos = (parametro.getid_pd (),)
                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Receta eliminada correctamente")
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)               
                
    def buscarProduccion(self, id_pd):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM produccion_diaria WHERE id_pd = %s;"
                datos = (id_pd,)
                cursor.execute(sentenciaSQL, datos)
                resultados = cursor.fetchone()
                self.conexion.commit()
                self.conexion.close()
                return resultados

            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)

    def modificarProduccion(self, parametro):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE produccion_diaria SET fecha = %s, cantidad =%s, id_producto=%s WHERE id_pd =%s;"

                datos = (parametro.getfecha(),
                         parametro.getcantidad(),
                         parametro.getid_producto(),
                         parametro.getid_pd(),)

                cursor.execute(sentenciaSQL, datos)
                self.conexion.commit()
                self.conexion.close()
                print("Producción actualizada correctamente")

            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)
                                
    def listarEditarProduccion(self,id_pd):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL="SELECT  a.fecha, b.nombre, a.cantidad, a.id_pd from produccion_diaria a INNER JOIN productos b on a.id_producto=b.id_producto WHERE a.id_pd=%s;"
                datos=(id_pd,)     
                cursor.execute(sentenciaSQL,datos)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)


    def sentenciasSQL (self):
        if self.conexion.is_connected ():
                 cursor = self.conexion.cursor()
                 #La misma retornará los insumos con sus cantidades requeridas para la producción indicada. 
                 sentenciaSQL = "SELECT a.id_receta,\
                     b.nombre, \
                         c.nombre, \
                             a.cantidad_insumos * d.cantidad   \
                                 from recetas a  INNER JOIN productos b on a.pizza_nro=b.id_producto \
                                     INNER JOIN produccion_diaria d on b.id_producto=d.id_producto \
                                         INNER JOIN insumos c on a.id_insumos=c.id_insumos \
                                             WHERE pizza_nro=%s"
                                                                     
                                                            
                 sentenciaSQL = "SELECT a.id_receta, b.nombre, c.nombre, a.cantidad_insumos * d.cantidad   from recetas a INNER JOIN productos b on a.pizza_nro=b.id_producto INNER JOIN produccion_diaria d on b.id_producto=d.id_producto INNER JOIN insumos c on a.id_insumos=c.id_insumos WHERE d.fecha='2023-06-06' and pizza_nro='2'"
                
                 #•Producción total de un día ingresado.
                 sentenciaSQL="SELECT a.fecha, b.nombre, a.cantidad from produccion_diaria a INNER JOIN productos b on a.id_producto=b.id_producto  WHERE a.fecha='2023-06-06'"
                 sentenciaSQL =" SELECT a.id_receta,d.fecha, b.nombre, c.nombre, a.cantidad_insumos * d.cantidad   from recetas a INNER JOIN productos b on a.pizza_nro=b.id_producto INNER JOIN produccion_diaria d on b.id_producto=d.id_producto INNER JOIN insumos c on a.id_insumos=c.id_insumos WHERE d.fecha='2023-06-06'"
                 
                 #•Cantidad de insumos utilizados en un día ingresado. 
                 sentenciaSQL="SELECT d.fecha, c.nombre, a.cantidad_insumos * d.cantidad   from recetas a INNER JOIN productos b on a.pizza_nro=b.id_producto INNER JOIN produccion_diaria d on b.id_producto=d.id_producto INNER JOIN insumos c on a.id_insumos=c.id_insumos WHERE d.fecha='2023-06-06'"
                                
                 #•Producción total de un rango de tiempo ingresado.
                 sentenciaSQL="SELECT a.fecha, b.nombre, a.cantidad from produccion_diaria a INNER JOIN productos b on a.id_producto=b.id_producto WHERE a.fecha >= '2023-06-07' AND a.fecha < '2023-06-10'"
                 sentenciaSQL="SELECT a.id_receta,d.fecha, b.nombre, c.nombre, a.cantidad_insumos * d.cantidad   from recetas a INNER JOIN productos b on a.pizza_nro=b.id_producto INNER JOIN produccion_diaria d on b.id_producto=d.id_producto INNER JOIN insumos c on a.id_insumos=c.id_insumos WHERE d.fecha >= '2023-06-07' AND d.fecha < '2023-06-10'"
  

    def ProduccionDiaEspecifico(self,fecha):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL="SELECT b.id_producto, a.fecha, b.nombre, a.cantidad from produccion_diaria a INNER JOIN productos b on a.id_producto=b.id_producto  WHERE a.fecha=%s"

                datos=(fecha,)
                cursor.execute(sentenciaSQL,datos)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)    
                
    def ProduccionDiaEspecificoPorFechas(self,fecha,fecha1):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL="SELECT b.id_producto, a.fecha, b.nombre, a.cantidad from produccion_diaria a INNER JOIN productos b on a.id_producto=b.id_producto  WHERE a.fecha >= %s AND a.fecha < %s"
                
                datos=(fecha,fecha1,)
                cursor.execute(sentenciaSQL,datos)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)      
                         
    def listarInsumosTotales(self,fecha,pizza_nro):
        if self.conexion.is_connected():
            
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL="SELECT d.fecha, b.nombre, c.nombre, a.cantidad_insumos * d.cantidad, a.unidad_de_medida    from recetas a INNER JOIN productos b on a.pizza_nro=b.id_producto INNER JOIN produccion_diaria d on b.id_producto=d.id_producto INNER JOIN insumos c on a.id_insumos=c.id_insumos WHERE d.fecha=%s and pizza_nro=%s"
                datos=(fecha,pizza_nro,)
                cursor.execute(sentenciaSQL,datos)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)                
    
    def listarInsumosTotalesPorFechas(self,fecha,fecha1,pizza_nro):
        if self.conexion.is_connected():          
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL="SELECT d.fecha, b.nombre, c.nombre, a.cantidad_insumos * d.cantidad, a.unidad_de_medida    from recetas a INNER JOIN productos b on a.pizza_nro=b.id_producto INNER JOIN produccion_diaria d on b.id_producto=d.id_producto INNER JOIN insumos c on a.id_insumos=c.id_insumos WHERE d.fecha >= %s AND d.fecha < %s and pizza_nro=%s"
                datos=(fecha,fecha1,pizza_nro,)
                cursor.execute(sentenciaSQL,datos)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)   
                 
    def listarInsumosTotalesDia(self,fecha):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL="SELECT  c.nombre, SUM(a.cantidad_insumos * d.cantidad)  as total_cantidad, a.unidad_de_medida\
                        from recetas a INNER JOIN productos b on a.pizza_nro=b.id_producto \
                        INNER JOIN produccion_diaria d on b.id_producto=d.id_producto\
                        INNER JOIN insumos c on a.id_insumos=c.id_insumos \
                        WHERE d.fecha=%s GROUP BY c.nombre;"
                datos=(fecha,)
                cursor.execute(sentenciaSQL,datos)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as cantidadError:
                print("No se pudo conectar! debido: ", cantidadError)            
    
   
#-------------------------------------------------------------------------

                
            
                
   
   
             