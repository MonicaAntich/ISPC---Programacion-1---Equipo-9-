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

    id = int(input("\nIngrese el ID del producto a editar: "))
    con = modelo.ConectarProductos()
    contacto = con.buscarProducto(id)
    if contacto == None:
        print("\nLa busqueda no arrojo resultados")
    else:
        print("ID "+str(contacto[0]) + " || Pizza: " + str(contacto[1]))

        nombre = input("\n Ingrese el nuevo nombre o Enter para omitir: ")
        if nombre == "":
            nombre = lista[1]
            
        datoEditado = modelo.Productos(id, nombre,)

        conEdit = modelo.ConectarProductos()
        conEdit.modificarProductos(datoEditado)

        #input("\n Presione ENTER para continuar")

#RECETAS-------------------------------------------------------------------------------------------------------------
 
def listarRecetas():
    con = modelo.ConectarRecetas()
    listado = con.listarRecetas()
    print("")
    for lista in listado:
        print(
            ""+str(lista[1])+
            " | " + str(lista[2])+
            "  Cantidad: " + str(lista[3])+
            " " + str(lista[4]))
         
def crearReceta():
    con = modelo.ConectarProductos()
    listado = con.listarProductos()
    print("")
    for producto in listado:
        print(  str(producto[0])+": " + str(producto[1]) )
    pizza_nro = input("\nIngrese el numero de pizza: ")
    
    print("")
    con = modelo.ConectarInsumo()
    listado = con.listarInsumos()
    for lista in listado:
        print( str(lista[0])+": "+str(lista[1]))
        
    id_insumos = input("\nIngrese el numero de insumo: ")
    cantidad_insumos = input("Ingrese la cantidad de insumo: ")
    unidad_de_medida=input("Ingrese unidad de medida: ")
    
    
    productoNuevo = modelo.Recetas(0, pizza_nro,cantidad_insumos,id_insumos, unidad_de_medida)

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
            " ID: "+str(lista[0])+
            " |  " + str(lista[1])+
            " | Insumo: " + str(lista[2])+
            " | Cantidad: " + str(lista[3])+
        " " + str(lista[4]))
        
    print("")
    id_receta = int(input("\nIngrese el ID de la receta a editar: "))
    con = modelo.ConectarRecetas()
    contacto = con.buscarRecetas(id_receta)
    
    con = modelo.ConectarRecetas()
    ler = con.listarEditarRecetas(id_receta)
 
        
    if contacto  == None:
        print("\nLa busqueda no arrojo resultados")
    else:
        
        for dato in ler:
         print(
            " ID: "+str(dato[0])+" | Pizza: " + str(dato[1])+" | Insumo: " + str(dato[2])+" | Cantidad: " + str(dato[3])+" " + str(dato[4]))

        
    
        pizza_nro = contacto[1] 
      
        
        cantidad_insumos = input("\n Ingrese la nueva cantidad de insumos  o Enter para omitir: ")
        if cantidad_insumos == "":
            cantidad_insumos = contacto[2]   
            
            
        con = modelo.ConectarInsumo()
        insumos = con.listarInsumos()
        for i in insumos:
            print("ID: "+str(i[0])+
                " insumo: "+str(i[1]))
            
        id_insumos = input("\n Ingrese el nuevo ID de insumo o Enter para omitir: ")
        if id_insumos == "":
            id_insumos = contacto[3] 
            
        unidad_de_medida = input("\n Ingrese la nueva unidad o Enter para omitir: ")
        if unidad_de_medida == "":
            unidad_de_medida = contacto[4] 
            
        datoEditado = modelo.Recetas(id_receta,pizza_nro, cantidad_insumos,id_insumos,unidad_de_medida)

        conEdit = modelo.ConectarRecetas()
        conEdit.modificarRecetas(datoEditado)

        #input("\n Presione ENTER para continuar")

def descripcionRecetas():
    con = modelo.ConectarProductos()
    listado = con.listarProductos()
    print("")
    for producto in listado:
        print(  str(producto[0])+": " + str(producto[1]) )
        
    pizza_nro = input("\nIngrese número para ver sus ingredientes: ")
    print("")
    con = modelo.ConectarRecetas()
    listado = con.listarRecetasDescripcion(pizza_nro)
    for lista in listado:
        print( str(lista[3])+""+str(lista[4])+" de "+str(lista[2]))
#INSUMOS---------------------------------------------------------------------------------------------------------------------

def listarInsumos():

    con = modelo.ConectarInsumo()
    listado = con.listarInsumos()
    print("")
    for lista in listado:
        print(
            " insumo: "+str(lista[1])) #si queremos mostrar el id seria con "id: " + str(lista[0])

def crearInsumo():
    nombre = input("Ingrese el ingrediente: ")
    productoNuevo = modelo.Insumo(0, nombre)

    con = modelo.ConectarInsumo()
    con.insertarInsumo(productoNuevo)
    
def eliminarInsumo():
    con = modelo.ConectarInsumo()
    listado = con.listarInsumos()
    print("")
    for lista in listado:
        print(
            " Numero: "+str(lista[0])+ " Nombre: "+str(lista[1])) 

    id_insumos= int(input("\nIngrese el Nro de insumo a eliminar: "))
    con = modelo.ConectarInsumo()
    producto = modelo.Insumo(id_insumos, " ")
    con.eliminarInsumo(producto)   
    
     
def editarInsumo():
    con = modelo.ConectarInsumo()
    listado = con.listarInsumos()
    print("")
    for lista in listado:
        print("Nro: "+str(lista[0]) +
              " Nombre: " + str(lista[1]))

    id_insumos = int(input("\nIngrese el nro de insumo a editar: "))
    con = modelo.ConectarInsumo()
    contacto = con.buscarInsumo(id_insumos)
    if contacto == None:
        print("\nLa busqueda no arrojo resultados")
    else:
        print("Numero "+str(contacto[0]) +
              " Nombre: " + str(contacto[1]))

        nombre = input("\n Ingrese el nuevo nombre o Enter para omitir: ")
        if nombre == "":
            nombre = lista[1]
            
        datoEditado = modelo.Insumo(id_insumos, nombre,)

        conEdit = modelo.ConectarInsumo()
        conEdit.modificarInsumo(datoEditado)
           
#PRODUCCCION DIARIA----------------------------------------------------------------------------------------------------------------

def listarProduccionDiaria ():
    con = modelo.ConectarProduccion ()
    listado = con.listarProduccion()
    
    print ("")         
    for lista in listado:
        print( "Fecha: " + str(lista[0]) + #fecha
                " | " + str(lista[2])+#cantidad
           " " + str(lista[1])+"s")#pizzas
        
def crearProduccion():
    cantidad =input ("Ingrese la cantidad: ")
    con = modelo.ConectarProductos()
    listado = con.listarProductos()
    print("")
    for producto in listado:
        print( str(producto[0])+" Pizza: " + str(producto[1]) )
    id_producto = input("Ingrese el id del producto: ")
    
    productoNuevo = modelo.Produccion_diaria(0, 0, cantidad, id_producto)
    con = modelo.ConectarProduccion()
    con.insertarProduccion (productoNuevo)
    
    
def eliminarProduccion ():
    con = modelo.ConectarProduccion()
    listado = con.listarProduccionId()
    print("")
    for lista in listado:
        print( 
            " Numero: "+str(lista[0])+
            " | Fecha: "+str(lista[1])+
            " | Pizza: " + str(lista[2])+
            " | Cantidad: " + str(lista[3])) 

    id_pd= int(input("\nIngrese el nro de Produccioon a eliminar: "))

    con = modelo.ConectarProduccion()
    producto = modelo.Produccion_diaria(id_pd, '', '','')

    con.eliminarProduccion(producto)


def editarProducciondiaria():
    con = modelo.ConectarProduccion()
    listado = con.listarProduccion()
    print("")
    for lista in listado:
        print(
            " ID: "+str(lista[3])+
            "Fecha: " + str(lista[0]) + #fecha
            " | " + str(lista[2])+#cantidad
            " " + str(lista[1])+"s")#pizzas

        
    print("")
    id_pd = int(input("\nIngrese el ID de la produccion a editar: "))
    con = modelo.ConectarProduccion()
    contacto = con.buscarProduccion(id_pd)
    
    con = modelo.ConectarProduccion()
    ler = con.listarEditarProduccion(id_pd)
 
    if contacto  == None:
        print("\nLa busqueda no arrojo resultados")
    else:
        
        for dato in ler:
         print(
            " ID: "+str(dato[3])+" | Fecha: " + str(dato[0])+" | Pizza: " + str(dato[1])+"  " + str(dato[2]))

        #fecha = input("\n Presione Enter ")
        #if fecha == "":
        fecha = contacto[1] 
            
        con = modelo.ConectarProductos()
        listado = con.listarProductos()
        print("")
        for lista in listado:
            print("ID: "+str(lista[0]) +" || Pizza: " + str(lista[1]))  
              
        id_producto = input("\n Ingrese la nueva pizza por su NRO o Enter para omitir ")
        if id_producto == "":
            id_producto = contacto[3] 
        
        cantidad = input("\n Ingrese la nueva cantidad  o Enter para omitir: ")
        if cantidad == "":
            cantidad = contacto[2]   
                       
        datoEditado = modelo.Produccion_diaria(id_pd,fecha, cantidad,id_producto)
        conEdit = modelo.ConectarProduccion()
        conEdit.modificarProduccion(datoEditado)

        #input("\n Presione ENTER para continuar")

        
