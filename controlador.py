# TODAS LAS FUNCIONALIDADES DEL PROYECTO
import modelo

def listarProductos():
    con = modelo.ConectarProductos()
    listado = con.listarProductos()
    print("")
    for producto in listado:
        print(
            #str(listarRecetas())+
            "Pizza: " + str(producto[2]) )
           # " || Receta numero: "+str(producto[1] )+
            
        
def crearProducto():
    nombre = input("Ingrese el nombre completo: ")
    receta = input("Ingrese la receta:")
    
    productoNuevo = modelo.Productos(0, receta, nombre)

    con = modelo.ConectarProductos()
    con.insertarProductos(productoNuevo)

def eliminarProducto():
    con = modelo.ConectarProductos()
    listado = con.listarProductos()
    print("")
    for producto in listado:
        print("NRO "+str(producto[0]) +
              " Nombre: " + str(producto[2]) +
              " Receta: "+ str(producto[1]))

    id_producto = int(input("\nIngrese el nro de pizza a eliminar: "))

    con = modelo.ConectarProductos()
    producto = modelo.Productos(id_producto, '', '')

    con.eliminarProductos(producto)

def editarProducto():
    con = modelo.ConectarProductos()
    listado = con.listarProductos()
    print("")
    for lista in listado:
        print("ID "+str(lista[0]) +
              " Receta: " + str(lista[1]) +
              " Nombre: "+lista[2])

    id_producto = int(input("\nIngrese el ID del producto a editar: "))
    con = modelo.ConectarProductos()
    contacto = con.buscarProducto(id_producto)

    if contacto == None:
        print("\nLa busqueda no arrojo resultados")
    else:
        print("ID "+str(lista[0]) +
              " Receta: " + str(lista[1]) +
              " Nombre: "+lista[2])

        receta = input("\n Ingrese nro receta o Enter para omitir:")
        if receta == "":
            receta = lista[1]

        nombre = input("\n Ingrese el nuevo nombre o Enter para omitir: ")
        if nombre == "":
            nombre = lista[2]
            
        datoEditado = modelo.Productos(id_producto, receta, nombre,)

        conEdit = modelo.ConectarProductos()
        conEdit.modificarProductos(datoEditado)

        input("\n Presione ENTER para continuar")

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def listarRecetas():
    con = modelo.ConectarRecetas()
    listado = con.listarRecetas()
    for lista in listado:
        print(
            " id insumo: "+str(lista[1])+
            " Descripcion: " + str(lista[2])) #si queremos mostrar el id seria con "id: " + str(lista[0])

    #input("\n Presione ENTER para continuar")
   
def crearReceta():
    id_insumo = input("Ingrese id_insumo: ")
    nombre = input("Descripcion de la pizza: ")
    
    productoNuevo = modelo.Recetas(0, id_insumo,nombre)

    con = modelo.ConectarRecetas()
    con.insertarRecetas(productoNuevo)
    
def eliminarReceta():
    con = modelo.ConectarRecetas()
    listado = con.listarRecetas()
    print("")
    for lista in listado:
        print("NRO "+str(lista[0]) +
            " id insumo: "+str(lista[1])+
            " Descripcion: " + str(lista[2]))

    id_receta = int(input("\nIngrese el nro de receta a eliminar: "))

    con = modelo.ConectarRecetas()
    producto = modelo.Recetas(id_receta, '', '')

    con.eliminarRecetas(producto)
    
    #-----------------------------------------------------------------------------------------------------------
def listarInsumos():
    con = modelo.ConectarInsumo()
    listado = con.listarInsumos()
    for lista in listado:
        print(
            " insumo: "+str(lista[1])+ str(lista[2])) #si queremos mostrar el id seria con "id: " + str(lista[0])
        
def crearInsumos():
    nombre = input("Ingrese el nombre del insumo: ")
    cantidad = input("Ingrese la cantidad en grs: ")
    
    productoNuevo = modelo.Insumo
    con = modelo.ConectarInsumo()
    con.crearInsumos(productoNuevo)        
           


    
           
        