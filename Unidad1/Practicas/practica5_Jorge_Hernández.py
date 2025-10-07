#Práctica 5. Patrones de diseño
#Singleton

class Logger:
    _instancia = None #Creamos atributo de clase donde se guardara la unica instancia

#new es el método que controla la creación del objeto antes de init. Sirve para asegurarnos de que solo exista una unica instancia de la clase Logger.
    def __new__(cls, *args, **kwargs):
        #args es un argumemto posicional que permite recibir multiples parametros.

        #Validar si existe o no la instancia aún:
        if cls._instancia is None:
            cls._instancia = super().__new__(cls) #Creamos instancia de la clase Logger
            cls._instancia.archivo = open("app.log","a") #Agregando un atributo "archivo" que apunta a un archivo fisico "a" significa append = Todo lo que se escribe se agrega al final del archivo.
        return cls._instancia #Devolvemos siempre la misma instancia
    
    def log(self, mensaje):
        #Simulando un registro de Logs
        self.archivo.write(mensaje + "\n")
        self.archivo.flush()#Método para guardar en el disco

logger1 = Logger() #Creamos la primera y única instancia
logger2 = Logger() #Devolver la misma instancia, sin crear una nueva.

logger1.log("Inicio de sesión en la aplicación")
logger2.log("El usuario se autenticó")

#Comprobaer que son el mismo objeto en memoria
print(logger1 is logger2) #Devuelve true o false

# Actividad de la práctica


class Presidente:
    _instancia = None
    def __new__(cls, nombre):
     if cls._instancia is None:
         cls._instancia = super().__new__(cls)
         cls._instancia.nombre = nombre
         cls._instancia.historial = []
     return cls._instancia
    
    def accion(self, accion):
        evento = f"{self.nombre}{accion}"
        self.historial.append(evento)
        print(evento)

p1 = Presidente("AMLO ")
p2 = Presidente("Peña Nieto")
p3 = Presidente("Fox")

p1.accion("Firmó decreto")
p2.accion("Visitó España")
p3.accion("Aprobó un presupuesto")

print("\nHistorial del presidente:")
print(p1.historial)

#Validación de singleton
print(p1 is p2 is p3) #true o false

# 1. ¿Qué pasaría si eliminamos la verificación if cls._instancia en el metodo new?
# 2. ¿Qué significa el "True" en p1 is p2 is p3 en el contexto del método singleton?
# 3. ¿Es buena idea usar Singleton para todo lo que sea global? Menciona un ejemplo donde no sería recomendable.