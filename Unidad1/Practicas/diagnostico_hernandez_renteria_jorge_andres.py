#Simulador de pedidos
#Conceptos basicos: variables, inputs, condicionales, funciones y bucles

#Elegir una temática de tienda y escribir 3 productos
productos = ["Regla", "Cinta","Pegamento"]
precios = [27, 25, 62]

#funcion para calcular total
def calcular_total(cantidad, precios):
    total=0
    for i in range(len(cantidad)):
        total += cantidad [i] * precios[i]
    return total

#Menu para usuario (Outputs e Inputs)
print("Menu de papelería, Bienvenido")
nombre = (input("Ingresa tu nombre: "))
cantidad = []
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad_agregar = int(input(f"¿Cuantos/as {productos[i]} desea?"))
    cantidad.append(cantidad_agregar)

total = calcular_total(cantidad, precios)

print(f"Hola {nombre}, compraste:")
for i in range(len(productos)):
    if cantidad[i] > 0:
        print(f"{cantidad[i]} {productos[i]} - ${cantidad[i] * precios[i]}")
print(f"Total a pagar: ${total}")