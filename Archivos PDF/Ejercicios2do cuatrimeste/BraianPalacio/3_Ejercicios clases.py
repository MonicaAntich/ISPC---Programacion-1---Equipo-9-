
class Cursos:
    fechaInicio = ""
    titulo = ""
    descripcion = ""
    objetivos = ""
    programa = ""
    costo = 0
    duracionMeses = 0
    foto = ""
    estado = bool
    clases=[]
    categoria=""
    CATEGORIAS = ["inicial", "intermedio", "avanzado"]
    def __init__(self, fechaInicio, titulo, descripcion, objetivos, programa, costo, duracionMeses, foto, estado,categoria ) -> None:
        self.fechaInicio = fechaInicio
        self.titulo = titulo
        self.descripcion = descripcion
        self.objetivos = objetivos
        self.programa = programa
        self.costo = costo
        self.duracionMeses = duracionMeses
        self.foto = foto
        self.estado = estado        
        self.clases = []       
        self.categoria = categoria
        
    def getfechaInicio(self):
        return self.fechaInicio
    def gettitulo(self):
        return self.titulo
    def getdescripcion(self):
        return self.descripcion
    def getobjetivos(self):
        return self.objetivos
    def getprograma(self):
        return self.programa
    def getcosto(self):
        return self.costo
    def getduracionMeses(self):
        return self.duracionMeses
    def getfoto(self):
        return self.foto
    def getcategoria(self):
        return self.categoria
    def getestado(self):
        return self.estado
    

    def setfechaInicio(self, fechaInicio):
        self.fechaInicio = fechaInicio
    def settitulo(self, titulo):
        self.titulo = titulo
    def setdescripcion(self, descripcion):
        self.descripcion = descripcion
    def setobjetivos(self, objetivos):
        self.objetivos = objetivos
    def setprograma(self, programa):
        self.programa = programa
    def setcosto(self, costo):
        self.costo = costo
    def setduracionMeses(self, duracionMeses):
        self.duracionMeses = duracionMeses
    def setfoto(self, foto):
        self.foto = foto
    def setestado(self, estado):
        self.estado = estado
    def setcategoria(self, categoria):
        self.categoria = categoria
        
    def agregar_clase(self, clase):
        self.clases.append(clase)    
        
    def setcategoria(self, nuevaCategoria):
        if nuevaCategoria in self.CATEGORIAS:
            self.categoria = nuevaCategoria
        else:
            print("Categoría no válida.")
            
    
        
    def __str__(self) -> str:
        return "\n " +self.titulo + " | Fecha de inicio: "+self.fechaInicio +" | Descripcion: "+  self.descripcion +" | Objetivos: "+  self.objetivos +" | Programa: "+  self.programa +" | Costo:"+  str(self.costo) +" | Duracion: "+   str(self.duracionMeses) +" meses | "+  self.foto +" | Categoria:"+ self.categoria +" " + str(self.estado)

CursoMecanica= Cursos("2023-06-22", "Mecanica", "Mecanica basica de auto ", "1:Aprender todas las partes del motor", "Programa", 10000, 9, "mecanica.jpg", "inicial", str(True))
# print(CursoMecanica)

class Clases:
    fecha = ""
    titulo = "" 
    contenido = ""
    URLDrive = ""
    docente=""
    def __init__(self, fecha, titulo, contenido, URLDrive, docente ) -> None:
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido
        self.URLDrive = URLDrive
        self.docente = docente
        
    def getfecha(self):
        return self.fecha
    def gettitulo(self):
        return self.titulo
    def getcontenido(self):
        return self.contenido
    def getURLDrive(self):
        return self.URLDrive
    
    def setfecha(self, fecha):
        self.fecha = fecha
    def settitulo(self, titulo):
        self.titulo = titulo
    def setcontenido(self, contenido):
        self.contenido = contenido
    def setURLDrive(self, URLDrive):
        self.URLDrive = URLDrive
        
    def __str__(self) -> str:
        return self.fecha +" | "+  self.titulo +" | "+  self.contenido +" | "+  self.URLDrive + " | "+ self.docente
    
# claseMecanica = Clases("2023-04-15", "Mecanica", "Sistema de refrigeracion", "htpps//googledrive.com.ar", "Pepito Sanchez") 
# print(claseMecanica)

class Usuario:
    id_Usuario=0
    apellido = ""
    nombre = ""
    dni = 0
    fechaNacimiento = ""
    direccion = ""
    localidad = ""
    codigoPostal = 0
    provincia = ""
    telefono = 0
    celular = 0
    email = ""
    claveAcceso=""
    estado=bool
    def __init__(self, id_Usuario, apellido, nombre, dni, fechaNacimiento, direccion, localidad, codigoPostal, provincia, telefono, celular, email, claveAcceso,estado ) -> None:
        self.id_Usuario = id_Usuario
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.fechaNacimiento = fechaNacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigoPostal = codigoPostal
        self.provincia = provincia
        self.telefono = telefono
        self.celular = celular
        self.email = email
        self.claveAcceso = claveAcceso
        self.estado = estado
        
    def getid_Usuario(self):
        return self.id_Usuario 
    def getapellido(self):
        return self.apellido
    def getnombre(self):
        return self.nombre
    def getdni(self):
        return self.dni
    def getfechaNacimiento(self):
        return self.fechaNacimiento
    def getdireccion(self):
        return self.direccion
    def getlocalidad(self):
        return self.localidad
    def getcodigoPostal(self):
        return self.codigoPostal
    def getprovincia(self):
        return self.provincia
    def gettelefono(self):
        return self.telefono
    def getcelular(self):
        return self.celular
    def getemail(self):
        return self.email
    def getestado(self):
        return self.estado
    def getclaveAcceso(self):
        return self.claveAcceso

    def setid_Usuario(self, id_Usuario):
        self.id_Usuario = id_Usuario
    def setapellido(self, apellido):
        self.apellido = apellido
    def setapellido(self, apellido):
        self.apellido = apellido
    def setnombre(self, nombre):
        self.nombre = nombre
    def setdni(self, dni):
        self.dni = dni
    def setfechaNacimiento(self,fechaNacimiento ):
        self.fechaNacimiento = fechaNacimiento
    def setdireccion(self, direccion):
        self.direccion = direccion
    def setlocalidad(self,localidad ):
        self.localidad = localidad
    def setcodigoPostal(self,codigoPostal ):
        self.codigoPostal = codigoPostal
    def setprovincia(self, provincia):
        self.provincia = provincia
    def settelefono(self, telefono):
        self.telefono = telefono
    def setcelular(self,celular ):
        self.celular = celular
    def setemail(self, email):
        self.email = email
    def setclaveAcceso(self, claveAcceso):
        self.claveAcceso = claveAcceso
    def setestado(self, estado):
        self.estado = estado

        
    
    def __str__(self) -> str:
        return "\nID:" + str(self.id_Usuario)+ " | Nombre: "+self.apellido +" "+  self.nombre +" | DNI: "+  str(self.dni) +" | Nacimiento: "+  self.fechaNacimiento +" | Direccion: "+  self.direccion +" | Localidad: "+  self.localidad +" | CP: "+  str(self.codigoPostal) +" | Provincia: "+  self.provincia +" | Telefono: "+  str(self.telefono) +" | Celular: "+  str(self.celular) +" | Email: "+  self.email + str(self.estado)
    
# User1= Usuario(1, "Lopez", "Mario", 36521203, "1962-08-29", "27 de Abril de 1995", "Cordoba", 5000, "Cordoba", 563210, 3571541385, "mario@gmail.com", str(True))
# print(User1)
    
class Docente(Usuario):
    def __init__(self, apellido, nombre, dni, fechaNacimiento, direccion, localidad, codigoPostal, provincia, telefono, celular, email, claveAcceso, estado) -> None:
        super().__init__(apellido, nombre, dni, fechaNacimiento, direccion, localidad, codigoPostal, provincia, telefono, celular, email, claveAcceso, estado)

# Docente1= Docente("Lopez", "Mario", 36521203, "1962-08-29", "27 de Abril de 1995", "Cordoba", 5000, "Cordoba", 563210, 3571541385, "Mario@gmail.com", str(True), "dsasad")
# print(Docente1)        
    
class Administrador(Usuario):
    def __init__(self, apellido, nombre, dni, fechaNacimiento, direccion, localidad, codigoPostal, provincia, telefono, celular, email, claveAcceso, estado) -> None:
        super().__init__(apellido, nombre, dni, fechaNacimiento, direccion, localidad, codigoPostal, provincia, telefono, celular, email, claveAcceso, estado)


class CarritoDeCompra:
    id_Carrito_Compra=0
    items=[]
    id_Medio_Pago=0
    tarjeta=0
    cuotas=0
    #0=credito 1=debito 2=tranferencia
    def __init__(self, id_Carrito_Compra,id_Medio_Pago):
        self.id_Carrito_Compra = id_Carrito_Compra
        self.id_Medio_Pago = id_Medio_Pago
        self.items = []
        
    def getid_Carrito_Compra(self):
        return self.id_Carrito_Compra 
    def getid_Medio_Pago(self):
        return self.id_Medio_Pago
    def setid_Carrito_Compra(self, id_Carrito_Compra):
        self.id_Carrito_Compra = id_Carrito_Compra
    def setid_Medio_Pago(self, id_Medio_Pago):
        self.id_Medio_Pago = id_Medio_Pago


    def agregaritem(self, curso):
        self.items.append(curso)

    def eliminaritem(self, curso):
        self.items.remove(curso)

    def costoTotal(self):
        total = 0
        for curso in self.items:
            total += curso.costo
        return total

    def medioDePago(self):
        id_Medio_Pago = input("Ingrese medio de pago 0=crédito 1=débito 2=transferencia ")
        if id_Medio_Pago == 0:
             tarjeta = input("\nIngrese su numero de tarjeta de crédito: ")
             codigo=input("\nY el codigo de atras: ")
             cuotas=input("\nIngrese en cuantas cuotas hara el pago(máximo 3): ")
        elif id_Medio_Pago == 1:
             tarjeta = input("\nIngrese su numero de tarjeta de débito: ")
             codigo=input("\nY el codigo de atras: ")
        elif id_Medio_Pago == 2:
            print("CBU:1654584652486")
        else:
             print("Número incorrecto")


class Compra:
    id_Compra=0
    id_Carrito_Compra=0
    id_Medio_Pago=0
    id_Usuario=0
    fecha=""
    montoTotal=0
    def __init__(self, id_Compra, id_Carrito_Compra, id_Medio_Pago, id_Usuario, fecha, montoTotal):
        self.id_Compra = id_Compra
        self.id_Carrito_Compra = id_Carrito_Compra
        self.id_Medio_Pago = id_Medio_Pago
        self.id_Usuario = id_Usuario
        self.fecha = fecha
        self.montoTotal = montoTotal


    def getid_Compra(self):
        return self.id_Compra
    def getid_Carrito_Compra(self):
        return self.id_Carrito_Compra
    def getid_Medio_Pago(self):
        return self.id_Medio_Pago
    def getid_Usuario(self):
        return self.id_Usuario
    def getfecha(self):
        return self.fecha
    def getmontoTotal(self):
        return self.montoTotal
    
    
    def setid_Compra(self, id_Compra):
        self.id_Compra = id_Compra
    def setid_Carrito_Compra(self, id_Carrito_Compra):
        self.id_Carrito_Compra = id_Carrito_Compra
    def setid_Medio_Pago(self, id_Medio_Pago):
        self.id_Medio_Pago = id_Medio_Pago
    def setid_Usuario(self, id_Usuario):
        self.id_Usuario = id_Usuario
    def setfecha(self, fecha):
        self.fecha = fecha
    def setmontoTotal(self, montoTotal):
        self.montoTotal = montoTotal
    
    def confirmar_compra(self):
         print("Compra exitosa")  
 
        
class MediosDeContacto:
    id_MedioContacto=0
    fecha=""
    email=""
    telefono=0
    direccion=""
    nombre=""
    def __init__(self, id_MedioContacto, fecha, email, telefono, direccion, nombre):
        self.id_MedioContacto = id_MedioContacto
        self.fecha = fecha
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.nombre = nombre
        
    def getid_MedioContacto(self):
        return self.id_MedioContacto
    def gefecha(self):
        return self.fecha
    def getemail(self):
        return self.email
    def gettelefono(self):
        return self.telefono
    def getdireccion(self):
        return self.direccion
    def getnombre(self):
        return self.nombre
    
    
    def setid_MedioContacto(self, id_MedioContacto):
        self.id_MedioContacto = id_MedioContacto
    def setfecha(self, fecha):
        self.fecha = fecha
    def setemail(self, email):
        self.email = email
    def settelefono(self, telefono):
        self.telefono = telefono
    def setdireccion(self, direccion):
        self.direccion = direccion
    def setnombre(self, nombre):
        self.nombre = nombre        
        
        
class TiposDeContacto(MediosDeContacto):
    whatsApp=0
    correo=""
    callCenter=0
    referidoInterno=0
    def __init__(self, id_MedioContacto, fecha, email, telefono, direccion, nombre,whatsApp,correo, callCenter,referidoInterno):
        super().__init__(id_MedioContacto, fecha, email, telefono, direccion, nombre,whatsApp,correo, callCenter,referidoInterno)
            
        self.whatsApp = whatsApp
        self.correo = correo
        self.callCenter = callCenter
        self.referidoInterno = referidoInterno
     
    def getwhatsApp(self):
        return self.whatsApp
    def getcorreo(self):
        return self.correo
    def getcallCenter(self):
        return self.callCenter
    def getreferidoInterno(self):
        return self.referidoInterno
  
    def setwhatsApp(self, whatsApp):
        self.whatsApp = whatsApp
    def setcorreo(self, correo):
        self.correo = correo
    def setcallCenter(self, callCenter):
        self.callCenter = callCenter
    def setreferidoInterno(self, referidoInterno):
        self.referidoInterno = referidoInterno
  
  

