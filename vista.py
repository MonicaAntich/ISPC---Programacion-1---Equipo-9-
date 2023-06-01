# MODULO QUE EL USUARIO VE E INTERACTUA CON EL PROGRAMA
import controlador

while True:
        print("""\n1) Produccion del día    2) Productos    3) Recetas   4) Insumos    5) Salir""")

        menu = input("\nSeleccione una opción: ")

        if menu=="1":#PRODUCCION DEL DÍA-----------------------------------------------------------------------------------------------------
            print("""\n 1) Pizza Argentina    2) Pizza Napolitana 3) Pizza...""")

        elif menu == "2":#PRODUCTOS-----------------------------------------------------------------------------------------------------------
            print("""PRODUCTOS \n\n 1) Mostrar pizzas   2) Insertar un producto    3) Eliminar producto   4) Editar producto""")
            
            menuProducto = input("\n-Seleccione una opción: ")
            if menuProducto == "1":
                controlador.listarProductos()
              # controlador.listarRecetas()
            elif menuProducto == "2":
                controlador.crearProducto()
            elif menuProducto == "3":
                controlador.eliminarProducto()
            elif menuProducto == "4":    
                 controlador.editarProducto()
            
        elif menu == "3":#RECETAS-----------------------------------------------------------------------------------------------------------
            print("""RECETAS  \n\n 1) Mostrar recetas    2) Insertar receta    3) Eliminar receta""")
            
            menuReceta = input("\n-Seleccione una opción: ")
            if menuReceta == "1":
                controlador.listarRecetas()
            elif menuReceta == "2":
                controlador.crearReceta() 
            elif menuReceta == "3":
                controlador.eliminarReceta() 
                                        
        elif menu == "4":#INSUMOS-----------------------------------------------------------------------------------------------------------
            print("""INSUMOS \n\n 1) Mostrar insumos    2) Insertar insumo    """)
            
            menuInsumo = input("\n-Seleccione una opción: ")
            
        elif menu == "5":print("\nOff"); exit()#SALIR
        else: print("Opcion no valida")

