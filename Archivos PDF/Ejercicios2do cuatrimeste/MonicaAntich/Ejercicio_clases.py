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
    categoria = ""
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
    def __init__(self, 
                 Nombre, 
                 Apellido, 
                 Dni, 
                 Fecha_nac, 
                 Direccion, 
                 Localidad, 
                 Codigo_post, 
                 Provincia, 
                 NroTelefono_celular, 
                 Email):
        
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

class Docente(Usuario):
    clave_acceso = 0
    estado = "Activo"
    def __init__(self, Nombre, Apellido, Dni, Fecha_nac, Direccion, Localidad, Codigo_post, Provincia, NroTelefono_celular, email, Clave_Acceso, Estado):
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
    def __init__(self, Nombre, Apellido, Dni, Fecha_nac, Direccion, Localidad, Codigo_post, Provincia, NroTelefono_celular, email, Fecha_Compra, Monto_Total):
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
        self.fecha_compra =Fecha_Compra
        self.monto_total = Monto_Total
