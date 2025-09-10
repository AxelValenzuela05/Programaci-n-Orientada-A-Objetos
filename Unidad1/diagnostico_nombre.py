# practica diagnostico_nombre.py

productos = ["USB-32GB", "USB-64GB", "USB-128GB"]
precios = [80, 120, 170]

# Funcion para calcular el total 
def calcular_total(cantidades, precios):
    total = 0
    for i in range(len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

# menu usuario
print("Bienvenido a tienda de sistemas")
nombre = input("Ingresa tu nombre: ")

cantidades = []
print("\nSelecciona tu pedido (ingresa la cantidad de cada producto):\n")
for i in range(len(productos)):
    print(f"[{i}] {productos[i]} - ${precios[i]}")
    cantidad = int(input(f"Cantidad de {productos[i]}: "))
    cantidades.append(cantidad)

# Calcular total
total = calcular_total(cantidades, precios)

# Aplicar descuento (10% si el total es mayor a $500)
descuento = 0
if total > 500:
    descuento = total * 0.10

total_final = total - descuento

# Ticket
print("\n------ TICKET DE COMPRA ------")
print(f"Cliente: {nombre}\n")

print("Productos:")
for i in range(len(productos)):
    if cantidades[i] > 0:
        subtotal = cantidades[i] * precios[i]
        print(f"{cantidades[i]} x {productos[i]} - ${subtotal}")

print(f"\nSubtotal: ${total}")
print(f"Descuento: ${descuento}")
print(f"TOTAL A PAGAR: ${total_final}")
print("------------------------------")