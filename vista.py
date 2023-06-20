# MODULO QUE EL USUARIO VE E INTERACTUA CON EL PROGRAMA
import controlador

from colorama import init,Fore,Back,Style #Para dar color cuando trabajamos por consola
init(autoreset=True) # Para que solo se de color a parte que queremos, debemos inicializar 
                     # el módulo con init(autoreset=True)
                    

controlador.cabecera_presentacion ()


controlador.limpia()
#Fore es una constante (de la libreria colorama) que junto al color, muestra los colores en las palabras
#.BLACK para cambiar el fondo

print("""\n
                            Buenos días, ¿qué operacion desea realizar?                      """)    

while True:
        print(Fore.GREEN+Style.BRIGHT+"""\n    1) Producción del día    """+Fore.BLUE+"""2) Productos    """+Fore.LIGHTMAGENTA_EX+"""3) Recetas    """+Fore.YELLOW+"""4) Insumos    """+Fore.RED+   """5) Salir                """) 

        menu = input(Fore.WHITE+
            """\nSeleccione una opción: """)

        if menu == "1":#PRODUCCION DEL DÍA-----------------------------------------------------------------------------------------------------
            print(Fore.GREEN+Style.BRIGHT+"""
------------------------  
|  Producción del día  |
------------------------""")
            print(Fore.GREEN+"""\n1) Mostrar producciones   2) Ingresar produccion del día   3) Eliminar una produccion   4) Editar produccion""")
            menuProduccion = input(Fore.GREEN+"\n-Seleccione una opción: ")
            if menuProduccion == "1": 
                controlador.listarProduccionDiaria ()
            elif menuProduccion == "2":
                controlador.crearProduccion()
            elif menuProduccion == "3":
                controlador.eliminarProduccion()
            elif menuProduccion == "4":
                controlador.editarProducciondiaria ()
                        
                            
        elif menu == "2":#PRODUCTOS-----------------------------------------------------------------------------------------------------------
            print(Fore.BLUE+Style.BRIGHT+"""
---------------
|  Productos  |
---------------""")
            print(Fore.BLUE+""" \n1) Mostrar pizzas   2) Insertar un producto    3) Eliminar producto   4) Editar producto""")
            
            menuProducto = input(Fore.BLUE+"\n-Seleccione una opción: ")
            if menuProducto == "1":
                controlador.listarProductos()
            elif menuProducto == "2":
                controlador.crearProducto()
            elif menuProducto == "3":
                controlador.eliminarProducto()
            elif menuProducto == "4":    
                 controlador.editarProducto()
              
                 
        elif menu == "3":#RECETAS-----------------------------------------------------------------------------------------------------------
            print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"""
-------------
|  Recetas  |
-------------""")
            print(Fore.LIGHTMAGENTA_EX+"""\n1) Mostrar recetas    2) Insertar receta    3) Eliminar receta   4) Editar receta   """)
            
            menuReceta = input(Fore.LIGHTMAGENTA_EX+"\n-Seleccione una opción: ")
            if menuReceta == "1":
                controlador.descripcionRecetas()
            elif menuReceta == "2":
                controlador.crearReceta() 
            elif menuReceta == "3":
                controlador.eliminarReceta()
            elif menuReceta == "4":
                controlador.editarReceta() 
            # elif menuReceta == "5":
            #     controlador.descripcionRecetas() 
               
                                                 
        elif menu == "4":#INSUMOS-----------------------------------------------------------------------------------------------------------
            print(Fore.YELLOW+Style.BRIGHT+"""
-------------
|  Insumos  |
-------------""")
            print(Fore.YELLOW+"""\n1) Mostrar insumos    2) Insertar Insumo   3) Eliminar Insumo   4) Editar Insumo  """)
            
            menuInsumo = input(Fore.YELLOW+"\n-Seleccione una opción: ")
            if menuInsumo == "1":
                controlador.listarInsumos()
            elif menuInsumo == "2":
                controlador.crearInsumo()
            elif menuInsumo == "3":
                controlador.eliminarInsumo() 
            elif menuInsumo == "4":
                controlador.editarInsumo()    
            
            #-------------------------------------------------------------------------------------------------------------
       
       
        elif menu == "5":#SALIR
            
            print(Fore.RED+"\n Muchas gracias, adios."); exit()
        else: print(Fore.RED+"Opcion no valida")
        
        
            
        