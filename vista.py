# MODULO QUE EL USUARIO VE E INTERACTUA CON EL PROGRAMA
import controlador


print("""---------------------------------------------------------------------------------------------
|            ISPC Tecnico Superior en Innovacion 4.0               Cohorte 2023             |
|-------------------------------------------------------------------------------------------|
|            Materia  : Programacion y Base de datos Lenguaje : Python 1er año              |
|            Profesor : Kevin  Kessler                                                      |
|            Repositorio :                                                                  |
|            https://github.com/MonicaAntich/ISPC---Programacion-1---Equipo-9-              |
|            Alumnos  : Velazquez Hebe                                                      |
|                       Palacio Braian                                                      |
|                       Antich Monica                                                       |
---------------------------------------------------------------------------------------------""")



print("BUENOS DIAS ¿QUE OPERACION DESEA REALIZAR?")    

while True:
        print("""\n 
              1) Produccion del día    
              2) Productos    
              3) Recetas   
              4) Insumos    
              5) Salir  """)

        menu = input("\nSeleccione una opción: ")

        if menu=="1":#PRODUCCION DEL DÍA-----------------------------------------------------------------------------------------------------
            print("""\n 1) Mostrar producciones   2) Ingresar produccion del día   3) Eliminar una produccion   4) Editar produccion""")

        elif menu == "2":#PRODUCTOS-----------------------------------------------------------------------------------------------------------
            print("""PRODUCTOS \n\n 1) Mostrar pizzas   2) Insertar un producto    3) Eliminar producto   4) Editar producto""")
            
            menuProducto = input("\n-Seleccione una opción: ")
            if menuProducto == "1":
                controlador.listarProductos()
            elif menuProducto == "2":
                controlador.crearProducto()
            elif menuProducto == "3":
                controlador.eliminarProducto()
            elif menuProducto == "4":    
                 controlador.editarProducto()
            
        elif menu == "3":#RECETAS-----------------------------------------------------------------------------------------------------------
            print("""RECETAS  \n\n 1) Mostrar recetas    2) Insertar receta    3) Eliminar receta   4) Editar receta""")
            
            menuReceta = input("\n-Seleccione una opción:")
            if menuReceta == "1":
                controlador.listarRecetas()
            elif menuReceta == "2":
                controlador.crearReceta() 
            elif menuReceta == "3":
                controlador.eliminarReceta()
            elif menuReceta == "4":
                controlador.editarReceta() 
                                                 
        elif menu == "4":#INSUMOS-----------------------------------------------------------------------------------------------------------
            print("""INSUMOS \n\n 1) Mostrar insumos    2) Insertar insumo    """)
            
            menuInsumo = input("\n-Seleccione una opción: ")
            if menuInsumo == "1":
                controlador.listarInsumos()
            elif menuInsumo == "2":
                controlador.crearInsumo()
            # elif menuInsumo == "3":
            #     controlador.eliminarInsumos() 
            
            #-------------------------------------------------------------------------------------------------------------
       
        elif menu == "5":print("\nOff"); exit()#SALIR
        else: print("Opcion no valida")

