# MODULO QUE EL USUARIO VE E INTERACTUA CON EL PROGRAMA
import controlador
from colorama import init,Fore,Back,Style #Para dar color cuando trabajamos por consola
init(autoreset=True) # Para que solo se de color a parte que queremos, debemos inicializar 
                     # el módulo con init(autoreset=True)
                    

print(Fore.BLACK+Back.WHITE+"""
---------------------------------------------------------------------------------------------
|            ISPC Tecnicatura Superior en Innovacion con Tecnologias 4.0  Cohorte 2023      |
|-------------------------------------------------------------------------------------------|
|            Materia  : Programacion y Base de datos Lenguaje : Python 1er año              |
|            Profesor : Kevin  Kessler                                                      |
|            Repositorio :                                                                  |
|            https://github.com/MonicaAntich/ISPC---Programacion-1---Equipo-9-              |
|            Alumnos  : Velazquez Hebe                                                      |
|                       Palacio Braian                                                      |
|                       Antich Monica                                                       |
---------------------------------------------------------------------------------------------""")
#Fore es una constante (de la libreria colorama) que junto al color, muestra los colores en las palabras
#.BLACK para cambiar el fondo

 
print(Fore.BLACK+Back.WHITE+"""\n
                            BUENOS DIAS ¿QUE OPERACION DESEA REALIZAR?                       """)    

while True:
    
        print(Fore.BLACK+Back.GREEN+"""\n    1) Produccion del día   2) Productos   3) Recetas   4) Insumos   5) Salir                """) 

        menu = input(Fore.BLACK+Back.GREEN+
            """\nSeleccione una opción: """)

        if menu == "1":#PRODUCCION DEL DÍA-----------------------------------------------------------------------------------------------------
            print("""\n 1) Mostrar producciones   2) Ingresar produccion del día   3) Eliminar una produccion   4) Editar produccion""")
            menuProduccion = input("\nSeleccione una opción: ")
            if menuProduccion == "1": 
                controlador.listarProduccionDiaria ()
            elif menuProduccion == "2":
                controlador.crearProduccion()
            
                            
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
            print("""RECETAS  \n\n 1) Mostrar recetas    2) Insertar receta    3) Eliminar receta   4) Editar receta   5)Descripcion""")
            
            menuReceta = input("\n-Seleccione una opción:")
            if menuReceta == "1":
                controlador.listarRecetas()
            elif menuReceta == "2":
                controlador.crearReceta() 
            elif menuReceta == "3":
                controlador.eliminarReceta()
            elif menuReceta == "4":
                controlador.editarReceta() 
            elif menuReceta == "5":
                controlador.descripcionRecetas() 
               
                                                 
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
       
       
        elif menu == "5":
            
            print("\n Off"); exit()#SALIR
        else: print("Opcion no valida")
        
             
            