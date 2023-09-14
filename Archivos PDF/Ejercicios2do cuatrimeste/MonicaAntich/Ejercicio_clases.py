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

class Categoria(Enum):
    avanzado = ""
    intermedio = ""
    inicial =""
    def __init__(self, Avanzado, Intermedio, Inicial):
      self.avanzado = Avanzado
      self.intermedio = Intermedio
      self.inicial = Inicial
      
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
    def __init__(self, Foto,TituCurso, Duracion, Costo):
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
    
    
class Confirmar_Compra():
    fecha_compra= date
    monto_total = 0
    def __init__(self,Fecha_Compra, Monto_Total):
        self.fecha_compra =Fecha_Compra
        self.monto_total = Monto_Total
        
class Compra():
    id_compra = 0
    id_carrito_compra = 0
    id_medio_pago = ""
    id_usuario = 0
    fecha = date
    monto_total = 0        
    def __init__(self, Id_Compra, Id_Carrito_compra, Id_Medios_Pago, Id_Usuario, Fecha, Monto_Total):
        self.id_compra = Id_Compra
        self.Id_carrito_compra = Id_Carrito_compra
        self.id_medios_pago = Id_Medios_Pago
        self.id_usuario = Id_Usuario
        self.fecha = Fecha
        self.monto_total = Monto_Total
        
class MediosDeContacto():
    id_medio_contacto = 0
    fecha = date 
    email = ""
    telefono = 0 
    direccion = ""
    nombre = ""
    def __init__(self, Id_Medio_Contacto, Fecha, Email, Telefono, Direccion, Nombre):
        self.id_medio_contacto = Id_Medio_Contacto
        self.fecha = Fecha
        self.email = Email
        self.telefono = Telefono
        self.direccion = Direccion
        self.nombre = Nombre

class TiposDeMedioDeContacto(MediosDeContacto):
    whatsApp = ""
    correo_electronico = ""
    callcenter = 0
    referido_interno = ""
    def __init__(self, Id_Medio_Contacto, Fecha, Email, Telefono, Direccion, Nombre, WhatsApp, Correo_Electronico, CallCenter, Referido_Interno):
        self.id_medio_contacto = Id_Medio_Contacto
        self.fecha = Fecha
        self.email = Email
        self.telefono = Telefono
        self.direccion = Direccion
        self.nombre = Nombre
        self.whatsApp = WhatsApp
        self.correo_electronico = Correo_Electronico
        self.callcenter = CallCenter
        self.referido_interno = Referido_Interno
        
        