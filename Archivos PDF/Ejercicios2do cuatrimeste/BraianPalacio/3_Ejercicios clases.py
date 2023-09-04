class Cursos:
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
    def getestado(self):
        return self.estado
    def getcategoria(self):
        return self.categoria
    

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
        return self.fechaInicio +" "+  self.titulo +" "+  self.descripcion +" "+  self.objetivos +" "+  self.programa +" "+  self.costo +" "+  self.duracionMeses +" "+  self.foto +" "+ self.categoria +" "+ self.estado 
    
    

    
class Clases:
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
        return self.fecha +" "+  self.titulo +" "+  self.contenido +" "+  self.URLDrive 
    
    
class Docentes:
    def __init__(self, apellido, nombre, dni, fechaNacimiento, direccion, localidad, codigoPostal, provincia, telefono, celular, email ) -> None:
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

        
    
    def __str__(self) -> str:
        return self.apellido +" "+  self.nombre +" "+  self.dni +" "+  self.fechaNacimiento +" "+  self.direccion +" "+  self.localidad +" "+  self.codigoPostal +" "+  self.provincia +" "+  self.telefono +" "+  self.celular +" "+  self.email 
    
    
class UsuarioFinal:
    def __init__(self, apellido, nombre, dni, fechaNacimiento, direccion, localidad, codigoPostal, provincia, telefono, celular, email, claveAcceso, estado ) -> None:
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
        self._cuenta_activa = False
  
        
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
    def getclaveAcceso(self):
        return self.claveAcceso
    def getestado(self):
        return self.estado
    
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
        
    
    def activar_cuenta(self):
        self._cuenta_activa = True
        
    def __str__(self) -> str:
        return self.apellido +" "+  self.nombre +" "+  self.dni +" "+  self.fechaNacimiento +" "+  self.direccion +" "+  self.localidad +" "+  self.codigoPostal +" "+  self.provincia +" "+  self.telefono +" "+  self.celular +" "+  self.email +" "+  self.claveAcceso  + " "+ self.estado 
    

class Roles:
    def __init__(self, administrador, docente ) -> None:
        self.administrador = administrador
        self.docente = docente

              
    def getadministrador(self):
        return self.administrador
    def getdocente(self):
        return self.docente

    def setadministrador(self, administrador):
        self.administrador = administrador
    def setdocente(self, docente):
        self.docente = docente

        
    def __str__(self) -> str:
        return self.administrador+" "+  self.docente 





class CarritoDeCompras:
    def __init__(self,item):
        self.item = []

    def getitem(self):
        return self.item
    def setitem(self, item):
        self.item = item
        
    def __str__(self) -> str:
        return self.item
    
    def agregar_item(self, curso):
        self._items.append(curso)

    def confirmar_compra(self):
         print("Compra exitosa")
        


