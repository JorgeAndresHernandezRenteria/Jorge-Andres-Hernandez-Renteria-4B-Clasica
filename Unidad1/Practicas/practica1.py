#Hernández Rentería Jorge Andrés 4°B Clásica
"""#Práctica 1 Clases, objetos y atributos
#Una clase es una plantilla o un molde que define como será un objeto

class Persona:
   def __init__(self, nombre, edad): #Constructor de una clase, sirve para agregar atributos a un objeto
    self.nombre = nombre
    self.edad = edad 

   def presentarse(self):
    print(f"Hola mí nombre es {self.nombre} y tengo {self.edad} años")

   def cumplir_anios(self):
    self.edad += 1
    print(f"Esta persona cumplió: {self.edad} años")

#Un objeto es una instancia creada a partir de una clase
#Crear un objeto que pertenece a una clase
estudiante1 = Persona("Jorge", 20)
estudiante2 = Persona("Andrés", 19)
#Asignar métodos a esos objetos (Acciones)
estudiante1.presentarse()
estudiante1.cumplir_anios()

#Paso 1. Agrega un método cumplir_anios() que aumente en 1 la edad

#INSTANCIA: 
#Cada objeto creado de una clase es una instancia. Podemos tener varias instancias que coexistan con sus propios datos
#Objeto = instancia de la clase. Cada vez que se crea un objeto con Clase() se obtiene una instancia dependiente.
#Cada instancia tiene sus propios datos aunque vengan de la misma clase.

#Abstracción
#Representar solo lo importante del mundo real, ocultando detalles inecesarios.

class automovil:
  def __init__(self, marca): 
   self.marca =  marca

  def arrancar(self):
   print(f"{self.marca} arrancó")

#Crear un objeto auto y asignar una marca
auto = automovil("FORD")
auto.arrancar()
#Abstracción: Nos centramos solo en lo que importa (acción) que es arrancar el automovil, ocultando detalles
#internos como: motor, transmisión, tipo_combustible.
#Enfoque solo en la acción del objeto.
#Objetivo es hacer el código más limpio y fácil de usar. """

#Práctica 1.2
#Crear una clase mascotas
#Agregar mínimo 4 atributos
#Definir al menos 4 métodos diferentes
#Crear 2 instancias de la clase
#Llamar los métodos y aplicar abstracción. (Agregar un atributo innecesario).

class Mascotas:
  def __init__(self, raza, tamaño, peso, edad):
    self.raza = raza
    self.tamaño = str(tamaño)
    self.peso = int(peso)
    self.edad = edad

  def raza(self):
    print (f"Es raza: {self.raza}")

  def cumplir_anios(self):
    self.edad += 1
    print(f"Esta mascota cumplió: {self.edad} años")

  def etapa(self):
    if self.tamaño == "Chico":
      print(f"{self.raza} Es cachorro/a")

    else:
      print("Es adulto")

  def padecimiento_peso(self):
    if self.peso >50:
      print(f"{self.raza} tiene sobrepeso")

    else:
      print("Esta mascota esta saludable")

mascota1 = Mascotas(f"Pastor Alemán","Grande",51, "2 años")
mascota2 = Mascotas(f"Pastor Belga","Chico",41, "1 año")
#Asignar métodos a esos objetos (Acciones)
mascota1.padecimiento_peso()
mascota2.etapa()

class Mascotas:
  def __init__(self, tipo): 
   self.tipo = tipo

  def etapa (self):
   print(f"{self.tipo} es Cachorro")

tipo = Mascotas ("Pastor Belga")
tipo.etapa()
