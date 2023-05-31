# TODAS LAS FUNCIONALIDADES DEL PROYECTO
import modelo

def listarProductos():
    con = modelo.ConectarProductos()
    listado = con.listarProductos()
    print("")
    for producto in listado:
        print(
            "Pizza: " + str(producto[2]) +
            " || Receta numero: "+str(producto[1] ))

    input("\n Presione ENTER para continuar")
   
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

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def listarNombreClase():
    con = modelo.ConectarNombreClase()
    listado = con.listarProductos()
    print("")
    for lista in listado:
        print(
            "variable1: " + str(lista[1]) +
            " || variable2: "+str(lista[2] )) #si queremos mostrar el id seria con "id: " + str(lista[0])

    input("\n Presione ENTER para continuar")
   
def crearNombreClase():
    variable1 = input("Ingrese la variable1: ")
    variable2 = input("Ingrese la variable2:")
    
    datoNuevo = modelo.Productos(0, variable1, variable2) #el 0 seria el id

    con = modelo.ConectarNombreClase()
    con.insertarNombreClase(datoNuevo)