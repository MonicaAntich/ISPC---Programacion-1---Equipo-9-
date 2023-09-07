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
    self.categoria = ""
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
                 Estado,
                 Categoria):
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
        self.categoria = Categoria
       
#     def get_nombrecurso(self):
#         return self.nombrecurso


#     def get_fecha_inicio(self):
#         return self.fecha_inicio


#     def get_titulo(self):
#         return self.titulo


#     def get_descripcion(self):
#         return self.descripcion


#     def get_objetivos(self):
#         return self.objetivos


#     def get_programa(self):
#         return self.programa
 
#     def get_costo(self):
#         return self.costo


#     def get_duracion_meses(self):
#         return self.duracion_meses


#     def get_foto(self):
#         return self.foto


#     def get_estado(self):
#         return self.estado
   
#     def set_nombrecurso(self, nombrecurso):
#         self.nombrecurso = nombrecurso
 
#     def set_fecha_inicio(self, fecha_inicio):
#         self.fecha_inicio = fecha_inicio


#     def set_titulo(self, titulo):
#         self.titulo = titulo


#     def set_descripcion(self, descripcion):
#         self.descripcion = descripcion


#     def set_objetivos(self, objetivos):
#         self.objetivos = objetivos


#     def set_programa(self, programa):
#         self.programa = programa


#     def set_costo(self, costo):
#         self.costo = costo


#     def set_duracion_meses(self, duracion_meses):
#         self.duracion_meses = duracion_meses


#     def set_foto(self, foto):
#         self.foto = foto


#     def set_estado(self, estado):
#         self.estado = estado


# curso1 = Curso("Programación Inicial", "2023-09-01", "Programar en Python", "Enseñar", "Objetivos del curso", "Programa del curso", 100, 3, "imagen.jpg", True) #Creo el objeto curso e instancio
# print(curso1.get_titulo())  # Muestro el título del curso
# curso1.set_estado(False)  # Modifico el estado del curso (metodo)
# print(curso1.get_estado())  # Se muestra el estado actual del curso De verdadero a falso


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
   
#     def get_fecha(self):
#         return self.fecha


#     def get_titulo(self):
#         return self.titulo


#     def get_contenido(self):
#         return self.contenido


#     def get_URLDrive(self):
#         return self.URLdrive  
   
#     def set_fecha(self, fecha):
#         self.fecha = fecha


#     def set_titulo(self, titulo):
#         self.titulo = titulo


#     def set_contenido(self, contenido):
#         self.contenido = contenido


#     def set_URLDrive(self, URLDrive):
#         self.URLdrive = URLDrive  


# dictado1 = Dictado_clase("2023-09-02", "Analisis Matematico", "Funciones Trigonometricas", "htpps//googledrive.com.ar") #Creo el objeto Dictado de clase e instancio
# print(dictado1.get_titulo())  # Muestro el título del dictado de clases
# dictado1.set_contenido("Derivadas e Integrales")  # Modifico el contenido (metodo)
# print(dictado1.get_contenido())  # Se muestra el contenido de la clase    
   
class Usuario():
    id_usuario = 0
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
    clave_acceso = 0
    estado = "Activo"
    def __init__(self, Id_Usuario, Nombre, Apellido, Dni, Fecha_nac, Direccion, Localidad, Codigo_post, Provincia, NroTelefono_celular, Email, Clave_acceso, Estado):
        self.id_usuario = Id_Usuario
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
        self.clave_acceso = Clave_acceso
        self.estado = Estado
       
#     def get_nombre(self):
#         return self.nombre    
   
#     def get_apellido(self):
#         return self.apellido


#     def get_dni(self):
#         return self.dni


#     def get_fecha_nac(self):
#         return self.fecha_nac


#     def get_direccion(self):
#         return self.direccion


#     def get_localidad(self):
#         return self.localidad


#     def get_codigo_post(self):
#         return self.codigo_post


#     def get_provincia(self):
#         return self.provincia


#     def get_telefono_celular(self):
#         return self.telefono_celular


#     def get_email(self):
#         return self.email
   
#     def get_clave_acceso(self):
#         return self.clave_ac.casefold()
   
#     def get_estado(self):
#         return self.estado
   
#     def set_nombre(self, nombre):
#         self.nombre = nombre


#     def set_apellido(self, apellido):
#         self.apellido = apellido


#     def set_dni(self, dni):
#         self.dni = dni


#     def set_fecha_nac(self, fecha_nac):
#         self.fecha_nac = fecha_nac


#     def set_direccion(self, direccion):
#         self.direccion = direccion


#     def set_localidad(self, localidad):
#         self.localidad = localidad


#     def set_codigo_post(self, codigo_post):
#         self.codigo_post = codigo_post


#     def set_provincia(self, provincia):
#         self.provincia = provincia


#     def set_telefono_celular(self, telefono_celular):
#         self.telefono_celular = telefono_celular


#     def set_email(self, email):
#         self.email = email
       
#     def set_clave_acceso(self, clave_acceso):
#         self.clave_acceso = clave_acceso
       
#     def set_estado(self, estado):
#         self.estado = estado
class Docente(Usuario):
    def __init__(self, Nombre, Apellido, Dni, Fecha_nac, Direccion, Localidad, Codigo_post, Provincia, NroTelefono_celular, email):


class Adminsitrador(Usuario):
        def __init__(self, Nombre, Apellido, Dni, Fecha_nac, Direccion, Localidad, Codigo_post, Provincia, NroTelefono_celular, Email, Clave_acceso, Estado) -> None:
        super().__init__(self, id_Usuario, Nombre, Apellido, Dni, Fecha_nac, Direccion, Localidad, Codigo_post, Provincia, NroTelefono_celular, Email, Clave_acceso, Estado)
         




class Carrito_compra():
    foto = ""
    tit_curso = ""
    duracion = ""
    costo = 0
    def __init__(self, foto, tit_curso, duracion, costo):
        self.foto = Foto
        self.tit_curso = TituloCurso
        self.duracion = Duracion
        self.costo = Costo
   
#     def set_foto(self, foto):
#         self.foto= foto
       
#     def set_tit_curso(self, tit_curso):
#         self.tit_curso= tit_curso
   
#     def set_duracion(self, duracion):
#         self.duracion= duracion
   
#     def set_costo(self, costo):
#         self.costo = costo            


#     def get_foto(self):
#         return self.foto
   
#     def get_tit_curso(self):
#         return self.tit_curso
   
#     def get_duracion(self):
#         return self.duracion
   
#     def get_costo(self):
#         return self.costo
   
   
class Medio_pago():
    tarjeta_credito = ""
    tarjeta_debito = ""
    transferencia = ""
    def __init__(self, Tarjeta_Credito, Tarjeta_Debito, Transferencia):
      self.tarjeta_credito = Tarjeta_Credito
      self.tarjeta_debito = Tarjeta_Debito
      self.transferencia = Transferencia
   
   
class Confirmar_Compra(Usuario):
    fecha_compra= date
    monto_total = 0
   
    def __init__(self, Fecha_Compra, MontoTotal):
        self.fecha_compra = Fecha_Compra
        self.montototal = MontoTotal


