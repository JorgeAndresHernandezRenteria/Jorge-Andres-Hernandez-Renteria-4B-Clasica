#Hernández Rentería Jorge Andrés 4°B Clásica
"""
1. Crear una clase Ticket con los siguientes atributos:
-id
-tipo (por ejemplo: software, prueba)
-prioridad (alta, media, baja)
-estado (por defecto 'pendiente')

2. Crear dos tickets de ejemplo y mostrarlos por pantalla.

3. Crear padre (clase) Empleado
   a) Crear la clase Empleado con atributo nombre.
   b) Crear método trabajar_en_ticket(self,ticket) que imprima:
   "El empleado <nombre> revisa el ticket <id>".

4. Crear clase Desarrollador que herede de Empleado y sobrescriba el método trabajar_en_ticket:
- Solo puede resolver tickets de tipo "Software". (validación)
- Si lo hace, cambia el estado a "resuelto" y muestra un mensaje.

5. Crear clase Tester que solo pueda resolver tickets de tipo "prueba". (condición)

6. Crear clase ProjectManager que asigne tickets
a) Crear la clase ProjectManager que herede de Empleado.
b) 

"""
"""
class Ticket:
    def __init__(self, id, tipo, prioridad, estado):
        self.id = id 
        self.tipo = tipo
        self.prioridad = prioridad
        self. estado = "pendiente"
    
class Empleado:
    def __init__(self,nombre):
        self.nombre = nombre

    def trabajar_en_ticket(self,ticket):
        print(f"El empleado {self.nombre} revisa el ticket {self.id}")

#Entre parentesis es la clase padre, Desarrollador es una subclase de la clase Empleado
class Desarrollador(Empleado):
    def trabajar_en_ticket(self,ticket):
        if ticket.tipo == "software":
            ticket.estado = "resuelto"
            print (f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            print ("Este tipo de empleado no puede resolver este ticket")

class Tester(Empleado):
    def trabajar_en_ticket(self,ticket):
        if ticket.tipo == "prueba":
            ticket.estado = "resuelto"
            print (f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            print ("Este tipo de empleado no puede resolver este ticket")
            
class Project_manager(Empleado):
    def asignar_ticket(self, ticket, empleado):
        print (f"{self.nombre} asignó el ticket {ticket.id}, a el empleado: {empleado.nombre}")
        empleado.trabajar_en_ticket(ticket)

#Crear tickets y empleados (Instancias de objetos)
ticket1 = Ticket(1, "software", "alta", "pendiente")
ticket2 = Ticket(2, "prueba", "media", "pendiente")

developer1 = Desarrollador("Jorge")
tester1 = Tester("Pablo")
pm1 = Project_manager("Susana")

pm1.asignar_ticket(ticket1, developer1)
pm1.asignar_ticket(ticket2, tester1) 
"""

#Parte adicional:
"""
Agregar un menú con while y con un if que permita:
1.- Crear un ticket
2.- Ver tickets
3.- Asignar tickets
4.- Salir del programa
"""
class Ticket:
    def __init__(self, id, tipo, prioridad):
        self.id = id 
        self.tipo = tipo
        self.prioridad = prioridad
        self.estado = "pendiente"
    
    def __str__(self):
        return f"Ticket {self.id}: {self.tipo} - Prioridad: {self.prioridad} - Estado: {self.estado}"

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def trabajar_en_ticket(self, ticket):
        print(f"El empleado {self.nombre} revisa el ticket {ticket.id}")

class Desarrollador(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo.lower() == "software":
            ticket.estado = "resuelto"  
            print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            print("Este tipo de empleado no puede resolver este ticket")

class Tester(Empleado):
    def trabajar_en_ticket(self, ticket):
        if ticket.tipo.lower() == "prueba":
            ticket.estado = "resuelto"  
            print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            print("Este tipo de empleado no puede resolver este ticket")

class Project_manager(Empleado):
    def asignar_ticket(self, ticket, empleado):
        print(f"{self.nombre} asignó el ticket {ticket.id} al empleado: {empleado.nombre}")
        empleado.trabajar_en_ticket(ticket)

# Sistema de gestión
class SistemaTickets:
    def __init__(self):
        self.tickets = []
        self.empleados = []
        self.contador_tickets = 1
        self.cargar_datos_ejemplo()
    
    def cargar_datos_ejemplo(self):
        # Crear empleados de ejemplo
        self.empleados.append(Desarrollador("Jorge"))
        self.empleados.append(Tester("Pablo"))
        self.empleados.append(Project_manager("Susana"))
        
        # Crear tickets de ejemplo
        self.tickets.append(Ticket(1, "software", "alta"))
        self.tickets.append(Ticket(2, "prueba", "media"))
        self.contador_tickets = 3
    
    def crear_ticket(self):
        print("\n--- CREAR NUEVO TICKET ---")
        
        # Validar tipo
        while True:
            tipo = input("Tipo (software/prueba): ").lower()
            if tipo in ["software", "prueba"]:
                break
            else:
                print("Error: Tipo debe ser 'software' o 'prueba'")
        
        # Validar prioridad
        while True:
            prioridad = input("Prioridad (alta/media/baja): ").lower()
            if prioridad in ["alta", "media", "baja"]:
                break
            else:
                print("Error: Prioridad debe ser 'alta', 'media' o 'baja'")
        
        # Crear ticket
        nuevo_ticket = Ticket(self.contador_tickets, tipo, prioridad)
        self.tickets.append(nuevo_ticket)
        self.contador_tickets += 1
        
        print(f"Ticket {nuevo_ticket.id} creado exitosamente!")
        return nuevo_ticket
    
    def ver_tickets(self):
        print("\n--- LISTA DE TICKETS ---")
        if not self.tickets:
            print("No hay tickets creados.")
            return
        
        for ticket in self.tickets:
            print(ticket)
    
    def asignar_ticket(self):
        print("\n--- ASIGNAR TICKET ---")
        
        # Verificar que hay tickets
        if not self.tickets:
            print("No hay tickets para asignar.")
            return
        
        # Mostrar tickets disponibles
        print("Tickets disponibles:")
        for i, ticket in enumerate(self.tickets, 1):
            print(f"{i}. {ticket}")
        
        # Seleccionar ticket
        try:
            seleccion = int(input("Selecciona el número del ticket: ")) - 1
            if 0 <= seleccion < len(self.tickets):
                ticket_seleccionado = self.tickets[seleccion]
            else:
                print("Selección inválida.")
                return
        except ValueError:
            print("Ingresa un número válido.")
            return
        
        # Mostrar empleados disponibles
        print("\nEmpleados disponibles:")
        for i, empleado in enumerate(self.empleados, 1):
            tipo_empleado = type(empleado).__name__
            print(f"{i}. {empleado.nombre} ({tipo_empleado})")
        
        # Seleccionar empleado
        try:
            seleccion_emp = int(input("Selecciona el número del empleado: ")) - 1
            if 0 <= seleccion_emp < len(self.empleados):
                empleado_seleccionado = self.empleados[seleccion_emp]
            else:
                print("Selección inválida.")
                return
        except ValueError:
            print("Ingresa un número válido.")
            return
        
        # Buscar Project Manager para asignar
        pm = None
        for empleado in self.empleados:
            if isinstance(empleado, Project_manager):
                pm = empleado
                break
        
        if pm:
            pm.asignar_ticket(ticket_seleccionado, empleado_seleccionado)
        else:
            print("No hay Project Manager disponible.")
    
    def menu_principal(self):
        while True:
            print("\n" + "="*50)
            print("        SISTEMA DE GESTIÓN DE TICKETS")
            print("="*50)
            print("1. Crear un ticket")
            print("2. Ver tickets")
            print("3. Asignar tickets")
            print("4. Salir del programa")
            print("-"*50)
            
            opcion = input("Selecciona una opción (1-4): ")
            
            if opcion == "1":
                self.crear_ticket()
            elif opcion == "2":
                self.ver_tickets()
            elif opcion == "3":
                self.asignar_ticket()
            elif opcion == "4":
                print("¡Gracias por usar el sistema!")
                break
            else:
                print("Opción inválida. Por favor, selecciona 1-4.")
            
            # Pausa antes de continuar
            input("\nPresiona Enter para continuar...")

# Ejecutar el sistema
if __name__ == "__main__":
    sistema = SistemaTickets()
    sistema.menu_principal()