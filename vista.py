# MODULO QUE EL USUARIO VE E INTERACTUA CON EL PROGRAMA
import controlador

while True:

    print("\n")
    print("Seleccione una opción: \n")
    print("1 - Mostrar pizzas")
    print("2 - Insertar una pizza")
    print("3 - Eliminar una pizza")
    #print("(nro) - Accion que realiza")
    print("9 - Salir")

    opcion = input("\nIngrese una opcion: ")

    if opcion == "1":
        controlador.listarProductos()
    elif opcion == "2":
        controlador.crearProducto()
    elif opcion == "3":
        controlador.eliminarProducto()
    #elif opcion == "nro":
        #controlador.metodo() #llama el metodo que se necesita para la accion en el controlador 
    elif opcion == "9":
        print("\nOff")   
        exit()
    else:
        print("Opcion incorrecta")