class Curso():
    nombrecurso = ""
    fecha_inicio = 0
    titulo = ""
    descripcion = ""
    objetivos = ""
    programa = ""
    costo = 0
    duracion_meses = 0
    foto = ""
    estado = True
    def __init__(self, 
                 NombreCurso,   
                 Fecha_Inicio, 
                 Titulo, 
                 Descripcion, 
                 Objetivos, 
                 Programa, 
                 Costo, 
                 Duracion_Meses, 
                 Foto, 
                 Estado):
        self.nombrecurso = NombreCurso
        self.fecha_inicio = Fecha_Inicio
        self.titulo = Titulo
        self.descripcion = Descripcion
        self.objetivos = Objetivos
        self.programa = Programa
        self.costo = Costo
        self.duracion_meses = Duracion_Meses
        self.foto = Foto
        self.estado = Estado
        
    def get_nombrecurso(self):
        return self.nombrecurso

    def get_fecha_inicio(self):
        return self.fecha_inicio

    def get_titulo(self):
        return self.titulo

    def get_descripcion(self):
        return self.descripcion

    def get_objetivos(self):
        return self.objetivos

    def get_programa(self):
        return self.programa
 
    def get_costo(self):
        return self.costo

    def get_duracion_meses(self):
        return self.duracion_meses

    def get_foto(self):
        return self.foto

    def get_estado(self):
        return self.estado
    
    def set_nombrecurso(self, nombrecurso):
        self.nombrecurso = nombrecurso
 
    def set_fecha_inicio(self, fecha_inicio):
        self.fecha_inicio = fecha_inicio

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def set_objetivos(self, objetivos):
        self.objetivos = objetivos

    def set_programa(self, programa):
        self.programa = programa

    def set_costo(self, costo):
        self.costo = costo

    def set_duracion_meses(self, duracion_meses):
        self.duracion_meses = duracion_meses

    def set_foto(self, foto):
        self.foto = foto

    def set_estado(self, estado):
        self.estado = estado

curso1 = Curso("Programación Inicial", "2023-09-01", "Programar en Python", "Enseñar", "Objetivos del curso", "Programa del curso", 100, 3, "imagen.jpg", True) #Creo el objeto curso e instancio
print(curso1.get_titulo())  # Muestro el título del curso
curso1.set_estado(False)  # Modifico el estado del curso (metodo)
print(curso1.get_estado())  # Se muestra el estado actual del curso De verdadero a falso

class Dictado_clase():
    fecha = 0
    titulo = "" 
    contenido = ""
    URLdrive = ""
    def __init__(self, Fecha, Titulo, Contenido, URLDrive):
        self.fecha = Fecha
        self.titulo = Titulo
        self.contenido = Contenido
        self.URLdrive = URLDrive 
    
    def get_fecha(self):
        return self.fecha

    def get_titulo(self):
        return self.titulo

    def get_contenido(self):
        return self.contenido

    def get_URLDrive(self):
        return self.URLdrive  
    
    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_contenido(self, contenido):
        self.contenido = contenido

    def set_URLDrive(self, URLDrive):
        self.URLdrive = URLDrive   

dictado1 = Dictado_clase("2023-09-02", "Analisis Matematico", "Funciones Trigonometricas", "htpps//googledrive.com.ar") #Creo el objeto Dictado de clase e instancio
print(dictado1.get_titulo())  # Muestro el título del dictado de clases
dictado1.set_contenido("Derivadas e Integrales")  # Modifico el contenido (metodo)
print(dictado1.get_contenido())  # Se muestra el contenido de la clase    
    
    
class Categoria(): 
    nombre = ""
    def __init__(self, Nombre):
        self.nombre = Nombre
      
    def set_nombre(self, nombre):
        self.nombre = nombre
      
    def get_nombre(self):
        return self.nombre
   
categoria1 = Categoria("Avanzado") #Creo el objeto categoria e instancio
print(categoria1.get_nombre())  # Muestro la categoria
categoria1.set_nombre("Inicial")  # Modifico la categoria (metodo)
print(categoria1.get_nombre())  # Se muestra la nueva categoria           
      

class Usuario:
    nombre = ""
    apellido = ""
    dni = 0
    fecha_nac = 0
    direccion = ""
    localidad = ""
    codigo_post = ""
    provincia = ""
    telefono_celular = 0
    email = ""
    def __init__(self, Nombre, Apellido, Dni, Fecha_nac, Direccion, Localidad, Codigo_post, Provincia, NroTelefono_celular, Email):
        self.nombre = Nombre
        self.apellido = Apellido        
        self.dni = Dni
        self.fecha_nac = Fecha_nac
        self.direccion = Direccion
        self.localidad = Localidad
        self.codigo_post = Codigo_post
        self.provincia = Provincia
        self.telefono_celular = NroTelefono_celular
        self.email = Email
        
    def get_nombre(self):
        return self.nombre    
    
    def get_apellido(self):
        return self.apellido

    def get_dni(self):
        return self.dni

    def get_fecha_nac(self):
        return self.fecha_nac

    def get_direccion(self):
        return self.direccion

    def get_localidad(self):
        return self.localidad

    def get_codigo_post(self):
        return self.codigo_post

    def get_provincia(self):
        return self.provincia

    def get_telefono_celular(self):
        return self.telefono_celular

    def get_email(self):
        return self.email  
    
    def set_nombre(self, nombre):
        self.nombre = nombre 

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_dni(self, dni):
        self.dni = dni

    def set_fecha_nac(self, fecha_nac):
        self.fecha_nac = fecha_nac

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_localidad(self, localidad):
        self.localidad = localidad

    def set_codigo_post(self, codigo_post):
        self.codigo_post = codigo_post

    def set_provincia(self, provincia):
        self.provincia = provincia

    def set_telefono_celular(self, telefono_celular):
        self.telefono_celular = telefono_celular

    def set_email(self, email):
        self.email = email

class Docente(Usuario):
    clave_acceso = ""
    mail_activo = ""
    estado1 = ""
    
    def __init__(self, Clave_acceso, Mail_activo, Estado):
        self.clave_acceso = Clave_acceso
        self.mail_activo = Mail_activo
        self.estado1 = Estado
    
    def set_clave_acceso(self, clave_acceso):
        self.clave_acceso = clave_acceso

    def get_clave_acceso(self):
        return self.clave_acceso
    
    def confirmar_clave_acceso(self, confirmar_clave):
                
        if self.clave_acceso == confirmar_clave:    # Método para comparar la clave de acceso
            return True
        else:
            return False 
        
    def mail_activo(self):
        self.mail_activo = True

    def mail_desactivado(self):
        self.mail_activo = False  
        
    def get_estado1(self):
        return self.estado1    
    
    def set_estado1(self, ):
        self.estado1 = estado1
        
    def cambiar_estado1(self):
        if self.estado1 == "Activo":
           self.estado1 = "Inactivo"
        else:
            self.estado1 = "Activo"   
            
            
docente1 = Usuario("Kessler", "Kevin", "23456788", "1998-04-05", "Lucas V Cordoba 1556", "Alta Gracia", "5186", "Cordoba", "3547420747", "kevin@kessler.com") #Creo el objeto docente e instancio
print(docente1.get_apellido())  # Muestro el apellido del docente
docente1.set_email("kevin.kessler@yahoo.com")  # Cambio el correo electrónico
print(docente1.get_email())  # Muestro el nuevo correo electrónico 

docente2 = Usuario("Charletti", "Carlos", "23456789", "1995-05-02", "Agustin Garzon 152", "Dean Funes", "5555", "Cordoba", "3516520321", "charletti@carlos.com") #Creo el objeto docente e instancio
print(docente2.get_apellido())
print(docente2.get_direccion())  # Muestro la direccion del docente
docente2.set_direccion("Santa Ana 1540")  # Cambio la direccion
print(docente2.get_direccion())  # Muestro la nueva direccion             
        
usuario1 = Docente("usuario@example.com", 1234,"Inactivo")
                                
if usuario1.confirmar_clave_acceso("mi_clave"):    # Reconfirmar la clave de acceso
    print("Clave de acceso confirmada")
else:
    print("La clave de acceso no coincide")       
        
    
usuario1 = Docente("usuario@example.com", 1234, "Inactivo")
print(f"Estado actual: {usuario1.get_estado1()}")

usuario1.cambiar_estado1()  # Cambiar el estado
print(f"Nuevo estado: {usuario1.get_estado1()}")   
    
class Roles(Usuario):
    rol = ""
    def __init__(self, id_rol, nombre_rol):
      self.id_rol = Id_rol
      self.nombre_rol = Nombre_rol

def get_id_rol(self):
        return self.id_rol

def get_nombre_rol(self):
        return self.nombre_rol    

def set_id_rol(self, id_rol):
        self.id_rol = id_rol      
 
def set_nombre_rol(self, id_rol):
        self.nombre_rol = nombre_rol          


class Carrito_compra:
    foto = ""
    tit_curso = ""
    duracion = ""
    costo = 0
    def __init__(self, foto, tit_curso, duracion, costo):
        self.foto = Foto
        self.tit_curso = TituloCurso
        self.duracion = Duracion
        self.costo = Costo
    
    def set_foto(self, foto):
        self.foto= foto
        
    def set_tit_curso(self, tit_curso):
        self.tit_curso= tit_curso
   
    def set_duracion(self, duracion):
        self.duracion= duracion
    
    def set_costo(self, costo):
        self.costo = costo             

    def get_foto(self):
        return self.foto
    
    def get_tit_curso(self):
        return self.tit_curso
   
    def get_duracion(self):
        return self.duracion
    
    def get_costo(self):
        return self.costo
    
    
# class Medio_pago:
#      tarjeta = ""   
# class Confirmar_Compra