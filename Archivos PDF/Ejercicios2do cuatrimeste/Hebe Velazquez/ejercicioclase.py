class tipo_de_cursos: 
    reparacionpc = ""
    reparacionalarmas = ""
    def __init__(self, ReparacionPc, ReparacionAlarmas):
        self.reparacionpc = ReparacionPc
        self.reparacionalarmas = ReparacionAlarmas
                  
    def get_reparacionpc (self):
        return self._reparacionpc
    
    def set_reparacionpc (self, reparacionpc):
        self._reparacionpc = reparacionpc
           
    def get_reparacionalarmas (self): 
        return self._reparacionalarmas

    def set_reparacionalarmas(self,reparacionalarmas):
            self._reparacionalarmas = reparacionalarmas

class nivel_de_cursos:
    nivel_inicial= ""
    nivel_intermedio= ""
    nivel_avanzado= ""
    
    def __init__(self, NivelInicial, NivelIntermedio, NivelAvanzado):
        self.nivel_inicial = NivelInicial
        self.nivel_intermedio = NivelIntermedio
        self.nivel_avanzado = NivelAvanzado
    def get_nivel_inicial (self):
        return self._nivel_inicial
    def set_nivel_inicial (self, nivel_inicial):
        self._nivel_inicial= nivel_inicial
    def get_nivel_intermedio (self):
        return self._nivel_intermedio
    def set_nivel_intermedio (self, nivel_intermedio):
        self._nivel_intermedio= nivel_intermedio
    def get_nivel_avanzado (self):
        return self._nivel_avanzado
    def set_nivel_avanzado (self, nivel_avanzado):
        self._nivel_avanzado= nivel_avanzado
        
class caracteristicas_cursos ():
    fecha_de_inicio= 0
    nombre_curso= ""
    objetivos_habilidades= ""
    programa= ""
    costo= 0
    duracion_mensual= 0
    imagen_portada= ""
    estado= ""
    def __init__(self, FechadeInicio, NombreCurso, ObjetivosHabilidades,
                 Programa, Costo, DuracionMensual, ImagenPortada, Estado):
        self.fecha_de_inicio = FechadeInicio
        self.nombre_curso = NombreCurso
        self.objetivos_habilidades = ObjetivosHabilidades
        self.programa = Programa
        self.costo = Costo
        self.duracion_mensual= DuracionMensual
        self.imagen_portada= ImagenPortada
        self.estado= Estado
    def get_fecha_de_inicio (self):
        return self._fecha_de_inicio
    def set_fecha_de_inicio (self, fecha_de_inicio):
        self._fecha_de_inicio = fecha_de_inicio
        
    def get_nombre_curso (self):
        return self._nombre_curso
    def set_nombre_curso (self, nombre_curso):
        self._nombre_curso= nombre_curso
    def get_objetivos_habilidades (self):
        return self._objetivos_habilidades
    def set_objetivos_habilidades (self, objetivos_habilidades):
        self._objetivos_habilidades= objetivos_habilidades
    
    def get_programa (self):
        return self._programa
    def set_programa (self, programa):
        self._programa= programa
    def get_costo (self):
        return self._costo
    def set_costo (self, costo):
        self._costo= costo
    def get_duracion_mensual (self):
        return self._duracion_mensual
    def set_duracion_mensual (self, duracion_mensual):
        self._duracion_mensual= duracion_mensual
    def get_imagen_portada (self):
        return self._imagen_portada
    def set_imagen_portada (self, imagen_portada):
        self._imagen_portada= imagen_portada
    def get_estado (self):
        return self._estado
    def set_imagen_estado (self, estado):
        self._estado = estado
class clases:
    fecha_de_clase= 0 
    titulo_clase= ""
    contenido_clase= ""
    url= ""
    def __init__ (self, FechadeClase, TituloClase, ContenidoClase, Url):
        self.fecha_de_clase= FechadeClase
        self.titulo_clase = TituloClase
        self.contenido= ContenidoClase 
        self.url= Url
    def get_fecha_de_clase (self):
        return self._fecha_de_clase
    def set_fecha_de_clase (self, fecha_de_clase):
        self._fecha_de_clase = fecha_de_clase
    def get_titulo_clase (self):
        return self._titulo_clase
    def set_titulo_clase (self, titulo_clase):
        self._titulo_clase = titulo_clase
    def get_contenido_clase (self):
        return self._contenido_clase
    def set_contenido_clase (self, contenido_clase):
        self._contenido_clase = contenido_clase
    def get_url (self):
        return self._url
    def set_url (self, url):
        self._url = url
class usuarios:
    nombre= ""
    apellido= ""
    DNI= 0
    direccion= ""
    fecha_nacimiento= 0
    localidad= ""
    provincia= ""
    telefono= 0
    email= ""
    def __init__ (self,  Nombre, Apellido, DNI, Direccion, Fecha_nacimiento, 
              Localidad, Provincia, Telefono, Email):
        self.nombre= Nombre
        self.apellido= Apellido
        self.dni= Dni
        self.direccion= Direccion
        self.fecha_nacimiento= Fecha_nacimiento
        self.localidad= Localidad
        self.provincia= Provincia
        self.telefono= Telefono
        self.email= Email
   
    def get_nombre (self):
        return self._nombre
    def set_nombre (self, nombre):
        self._nombre= nombre
    def get_apellido (self):
        return self._apellido
    def set_apellido (self, apellido):
        self._apellido= apellido
    def get_dni (self):
        return self._dni
    def set_dni (self, dni):
        self._dni= dni
    def get_direccion (self):
        return self._direccion
    def set_direccion (self, direccion):
        self._direccion= direccion 
    def get_fecha_nacimiento (self):
        return self._fecha_nacimiento
    def set_fecha_nacimiento (self, fecha_nacimiento):
        self._fecha_nacimiento= fecha_nacimiento
    def get_localidad (self):
        return self._localidad
    def set_localidad (self, localidad):
        self._localidad= localidad
    def get_provincia (self):
        return self._provincia
    def set_provincia (self, provincia):
        self._provincia= provincia
    def get_telefono (self):
        return self._telefono
    def set_telefono (self, telefono):
        self._telefono= telefono
    def get_email (self):
        return self._email
    def set_email (self, email):
        self._email= email
        
        
class tipo_usuarios:
    registrados="" 
    alumnos= ""
    compradores= ""
    administradores= ""
    def __init__ (self, Registrados, Alumnos, Compradores, Administradores):
        self.registrados= Registrados
        self.alumnos= Alumnos
        self.compradores= Compradores
        self.administradores= Administradores
        
    
    def get_registrados (self):
        return self._registrados 
    def set_registrados (self, registrados):
        self._registrados= registrados
    def get_alumnos (self):
        return self._alumnos 
    def set_alumnos (self, alumnos):
        self._alumnos= alumnos
    def get_compradores (self):
        return self._compradores
    def set_compradores (self, compradores):
        self._compradores= compradores
    def get_administradores (self):
        return self._administradores 
    def set_administradores (self, administradores):
        self._administradores= administradores
            
    
class carrito_compra:
    foto= ""
    nombre_curso= ""
    duracion= ""
    costo= 0   
    def __init__(self, Foto, Nombre_Curso, Duracion, Costo):
        self.foto= Foto
        self.nombre_curso1= Nombre_Curso
        self.duracion= Duracion
        self.costo= Costo
    def get_foto (self):
        return self._foto
    def set_foto (self, foto):
        self._foto = foto
    def get_nombre_curso (self):
        return self._nombre_curso
    def set_nombre_curso (self, nombre_curso):
       self._nombre_curso = nombre_curso
    def get_duracion (self):
        return self._duracion  
    def set_duracion (self, duracion):
       self._duracion = duracion
    def get_costo (self):
        return self._costo   
    def set_costo (self, costo ):
       self._costo = costo     
    
class medio_pago:
    tarjeta_credito= ""
    tarjeta_debito= ""
    transferencia_bancaria=""
    titular_compra= ""
    fecha_compra= 0
    monto_total= 0
    
    def __init__ (self, TarjetaCredito, TarjetaDebito, TarjetaBancaria, TitularCompra, 
                   FechaCompra, MontoTotal):
        self.tarjeta_credito= ""
        self.tarjeta_debito= ""
        self.transferencia_bancaria= ""
    def get_tarjeta_credito (self):
        return self._tarjeta_credito
    def set_tarjeta_credito (self, tarjeta_credito):
       self._tarjeta_credito = tarjeta_credito
    def get_tarjeta_debito (self):
        return self._tarjeta_debito
    def set_tarjeta_debito (self, tarjeta_debito):
       self._tarjeta_debito = tarjeta_debito
    def get_transferencia_bancaria (self):
        return self._transferencia_bancaria
    def set_transferencia_bancaria (self, transferencia_bancaria):
       self._transferencia_bancaria = transferencia_bancaria
class docentes (usuarios):
    materias= ""
    cantidad_horas= 0
    def __init__(self, Nombre, Apellido, DNI, Direccion, Fecha_Nacimiento, 
                 Localidad, Provincia, Telefono, Email, Materias, Cantidad_Horas):
        self.nombre= Nombre
        self.apellido= Apellido
        self.DNI= DNI
        self.direccion= Direccion
        self.fecha_nacimiento= Fecha_Nacimiento
        self.localidad= Localidad
        self.provincia= Provincia
        self.telefono= Telefono
        self.email= Email
        self.materias= Materias
        self.cantidad_horas= Cantidad_Horas
class compra:
    id_compra= ""
    id_carrito_compra= ""
    id_medios_pago= ""
    id_usuarios= ""
    id_fecha= 0
    id_monto_total= 0
    def __init__(self, Id_Compra, Id_Carrito_Compra,Id_Medios_Pagos,
                Id_Usuarios, Id_Fecha, Id_Monto_Total):
        self.id_compra= Id_Compra
        self.id_carrito_compra= Id_Carrito_Compra
        self.medios_pago= Id_Medios_Pagos
        self.usuarios= Id_Usuarios
        self.fecha= Id_Fecha
        self.id_monto_total= Id_Monto_Total
    
class medios_de_contactos:
    id_medio_contacto= ""
    fecha= 0
    email= ""
    telefono= 0
    direccion= ""
    nombre= ""
    def __init__ (self, Id_Medio_Contacto, Fecha, Email, Telefono, Direccion, Nombre):
        self.id_medio_contacto= Id_Medio_Contacto
        self.fecha= Fecha  
        self.email= Email
        self.telefono= Telefono
        self.direccion= Direccion
        self.nombre= Nombre

    
from enum import Enum       
class tipos_medios_de_contacto (medios_de_contactos, Enum): #hereda el método constructor de medios de contacto 
    whatsapp:1
    correo_electronico= 2
    call_center= 3
    interno_referido= 4
    def __init__ (self, Id_Medio_contacto, Fecha, Email, Telefono, Direccion, 
        Nombre, Whatsapp,Correo_Electronico, Call_Center, Interno_Referido):
        self.whatsapp= Whatsapp
        self.correo_electronico= Correo_Electronico
        self.call_center= Call_Center
        self.id_medio_contacto= Id_Medio_contacto
        self.fecha= Fecha  
        self.email= Email
        self.telefono= Telefono
        self.direccion= Direccion
        self.nombre= Nombre
        
    
    
        
        
    
        
        