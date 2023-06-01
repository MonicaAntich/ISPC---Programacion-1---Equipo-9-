# TODAS LAS FUNCIONALIDADES DEL PROYECTO
import modelo

def listarProductos():
    con = modelo.ConectarProductos()
    listado = con.listarProductos()
    print("")
    for producto in listado:
        print(
            str(listarRecetas())+
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

#-----------------------------------------------------------------------------------------------------------------------------------------------------

def listarRecetas():
    con = modelo.ConectarRecetas()
    listado = con.listarRecetas()
    for lista in listado:
        print(
            "id receta: " + str(lista[0]) +
            " || id insumo: "+str(lista[1])+
            " cantidad: " + str(lista[2]) +
            " Descripcion: " + str(lista[3])) #si queremos mostrar el id seria con "id: " + str(lista[0])

    #input("\n Presione ENTER para continuar")
   
def crearReceta():
    id_receta = input("Ingrese id_receta: ")
    id_insumo = input("Ingrese id_insumo: ")
    cantidad = input("Ingrese cantidad: ")
    nombre = input("Ingrese nombre: ")
    
    productoNuevo = modelo.Recetas(id_receta, id_insumo, cantidad,nombre)

    con = modelo.ConectarRecetas()
    con.insertarRecetas(productoNuevo)