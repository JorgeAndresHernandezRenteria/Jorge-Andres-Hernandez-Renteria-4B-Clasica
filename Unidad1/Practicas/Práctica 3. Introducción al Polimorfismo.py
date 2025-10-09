#Hernández Rentería Jorge Andrés 4°B Clásica
#Práctica 3. Introducción al Polimorfismo

#ACTIVIDAD: Replicarlo con un ejemplo de la vida real
#Práctica 3. Introducción al Polimorfismo

class correo:
    def procesar_mensaje(self, cantidad):
        return (f"Tienes {cantidad} notificacion/es de CORREO")

class sms:
    def procesar_mensaje(self, cantidad):
        return (f"Tienes {cantidad} notificacion/es de SMS")

class whatsapp:
    def procesar_mensaje(self, cantidad):
        return (f"Tienes {cantidad} notificacion/es de WHATSAPP")

class mensaje:
    def procesar_mensaje(self, cantidad):
        return (f"Tienes {cantidad} notificacion/es de MENSAJES") 

#Instancia
notificacion1 = correo()
notificacion2 = sms()
notificacion3 = whatsapp()
notificacion4 = mensaje()

#Polimorfismo (mismo método con diferentes objetos)

print (notificacion1.procesar_mensaje(1))
print (notificacion2.procesar_mensaje(2))
print (notificacion3.procesar_mensaje(5))
print (notificacion4.procesar_mensaje(3))
