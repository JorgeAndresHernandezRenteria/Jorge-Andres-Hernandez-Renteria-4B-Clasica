#Hernández Rentería Jorge Andrés 4°B Clásica

# Práctica 2. Atributos públicos y privados 

class Persona:
   def __init__(self, nombre, edad): #Constructor de una clase, sirve para agregar atributos a un objeto
    self.nombre = nombre
    self.edad = edad 
    self.__cuenta = None #Atributo privado

   def presentarse(self):
    print(f"Hola mí nombre es {self.nombre} y tengo {self.edad} años")

   def cumplir_anios(self):
    self.edad += 1
    print(f"Esta persona cumplió: {self.edad} años")

   def asignar_cuenta(self, cuenta):
     self.__cuenta = cuenta 
     print(f"{self.nombre} ahora tiene una cuenta bancaria")

   def consultar_saldo(self):
     if self.__cuenta:
       print(f"El saldo de {self.nombre} es $[{self.__cuenta.mostrar_saldo()}]")
     else:
       print(f"{self.nombre} aún no tiene cuenta bancaria")

class cuenta_bancaria: 
  def __init__(self, num_cuenta, saldo):
    self.cuenta = num_cuenta
    self.__saldo = saldo #atributo privado
  
  def mostrar_saldo(self):
    return self.__saldo

  def depositar(self, cantidad):
    if cantidad > 0:
      self.__saldo += cantidad
      print(f"Se depositó la cantidad de ${self.cantidad} a la cuenta, nuevo saldo es: ${self.__saldo}")
    
    else:
      print("Ingresa una cantidad válida")

  def retirar(self, retirar):
    if retirar > self.__saldo:
      print ("Saldo insuficiente")

    else:
      print(f"Se retiró la cantidad de ${self.retirar} de la cuenta, el nuevo saldo es:  ${self.__saldo}")
      
    

#Crear un objeto o instancia de la clase
persona1 = Persona("Miguel", 20)
persona1.presentarse()

#Acceder a los valores de los atributos públicos
print(persona1.nombre)
print(persona1.edad)
