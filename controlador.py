# TODAS LAS FUNCIONALIDADES DEL PROYECTO
import modelo




#PRODUCTOS----------------------------------------------------------------------------------------------------------------

def listarProductos():
    con = modelo.ConectarProductos()
    listado = con.listarProductos()
    print("")
    for producto in listado:
        print( "Pizza: " + str(producto[1]) )

def crearProducto():
    nombre = input("Ingrese la pizza: ")
    productoNuevo = modelo.Productos(0, nombre)
    con = modelo.ConectarProductos()
    con.insertarProductos(productoNuevo)

def eliminarProducto():
    con = modelo.ConectarProductos()
    listado = con.listarProductos()
    print("")
    for producto in listado:
        print("ID "+str(producto[0]) +
              " || Pizza: " + str(producto[1]))

    id_producto = int(input("\nIngrese el nro de pizza a eliminar: "))
    con = modelo.ConectarProductos()
    producto = modelo.Productos(id_producto, '')
    con.eliminarProductos(producto)

def editarProducto():
    con = modelo.ConectarProductos()
    listado = con.listarProductos()
    print("")
    for lista in listado:
        print("ID "+str(lista[0]) +
              " || Pizza: " + str(lista[1]))

    id_producto = int(input("\nIngrese el ID del producto a editar: "))
    con = modelo.ConectarProductos()
    contacto = con.buscarProducto(id_producto)

    if contacto == None:
        print("\nLa busqueda no arrojo resultados")
    else:
        print("ID "+str(lista[0]) +
              " || Pizza: " + str(lista[1]))

        nombre = input("\n Ingrese el nuevo nombre o Enter para omitir: ")
        if nombre == "":
            nombre = lista[1]
            
        datoEditado = modelo.Productos(id_producto, nombre,)

        conEdit = modelo.ConectarProductos()
        conEdit.modificarProductos(datoEditado)

        #input("\n Presione ENTER para continuar")

#RECETAS-------------------------------------------------------------------------------------------------------------
 
def listarRecetas():

    con = modelo.ConectarRecetas()
    listado = con.listarRecetas()
    for lista in listado:
        print(
            " id receta: "+str(lista[0])+#si queremos mostrar el id seria con "id: " + str(lista[0])
            " | Pizza nro: " + str(lista[1])+
            " | Insumo: " + str(lista[3])+
            " | Cantidad de insumo: " + str(lista[2])) 
    #input("\n Presione ENTER para continuar")
   
def crearReceta():
    pizza_nro = input("Ingrese el numero de pizza: ")
    id_insumos = input("Ingrese el ID de insumo: ")
    cantidad_insumos = input("Ingrese la cantidad de insumo en la pizza ")
    
    
    productoNuevo = modelo.Recetas(0, pizza_nro,cantidad_insumos,id_insumos)

    con = modelo.ConectarRecetas()
    con.insertarRecetas(productoNuevo)
    
def eliminarReceta():
    con = modelo.ConectarRecetas()
    listado = con.listarRecetas()
    print("")
    for lista in listado:
        print(
            " id receta: "+str(lista[0])+
            " | Pizza nro: " + str(lista[1])+
            " | Insumo: " + str(lista[3])+
            " | Cantidad de insumo: " + str(lista[2])) 

    id_receta = int(input("\nIngrese el nro de receta a eliminar: "))

    con = modelo.ConectarRecetas()
    producto = modelo.Recetas(id_receta, '', '','')

    con.eliminarRecetas(producto)
    
def editarReceta():
    con = modelo.ConectarRecetas()
    listado = con.listarRecetas()
    print("")
    for lista in listado:
        print(
            " id receta: "+str(lista[0])+
            " | Pizza nro: " + str(lista[1])+
            " | Insumo: " + str(lista[3])+
            " | Cantidad de insumo: " + str(lista[2])) 

    id_receta = int(input("\nIngrese el ID de la receta a editar: "))
    con = modelo.ConectarRecetas()
    contacto = con.buscarRecetas(id_receta)

    if contacto == None:
        print("\nLa busqueda no arrojo resultados")
    else:
        print(
            " id receta: "+str(lista[0])+
            " | Pizza nro: " + str(lista[1])+
            " | Insumo: " + str(lista[3])+
            " | Cantidad de insumo: " + str(lista[2]))  

        Pizza_nro = input("\n Ingrese el nuevo numero de pizza o Enter para omitir: ")
        if Pizza_nro == "":
            Pizza_nro = lista[1]
        cantidad_insumos = input("\n Ingrese la nueva cantidad de insumos nombre o Enter para omitir: ")
        if cantidad_insumos == "":
            cantidad_insumos = lista[2]   
        id_insumos = input("\n Ingrese el nuevo id de insumo o Enter para omitir: ")
        if id_insumos == "":
            id_insumos = lista[3] 
        datoEditado = modelo.Recetas(id_receta, Pizza_nro,cantidad_insumos,id_insumos,)

        conEdit = modelo.ConectarRecetas()
        conEdit.modificarRecetas(datoEditado)

        #input("\n Presione ENTER para continuar")

#INSUMOS---------------------------------------------------------------------------------------------------------------------

def listarInsumos():

    con = modelo.ConectarInsumo()
    listado = con.listarInsumos()
    for lista in listado:
        print(
            " insumo: "+str(lista[1])) #si queremos mostrar el id seria con "id: " + str(lista[0])

def crearInsumo():
    nombre = input("Ingrese el ingrediente: ")
    productoNuevo = modelo.Insumo(0, nombre)

    con = modelo.ConectarInsumo()
    con.insertarInsumo(productoNuevo)
           
#PRODUCCCION DIARIA----------------------------------------------------------------------------------------------------------------
def listarProduccionDiaria ():
    con = modelo.ConectarProduccion ()
    listado = con.listarProduccion()
    
    print ("")         
    for lista in listado:
        print( "fecha: " + str(lista [1] ) + 
          "id_producto : " + str(lista [3] ) +
           "cantidad : " + str(lista [2] ) )
    
    
def crearProduccion():
    cantidad =input ("Ingrese la cantidad: ")
    id_producto = input("Ingrese el id del producto: ")
    productoNuevo = modelo.Produccion_diaria(0, 0, cantidad, id_producto)
    con = modelo.ConectarProduccion()
    con.insertarProduccion (productoNuevo)
        
        
        
        
        
    