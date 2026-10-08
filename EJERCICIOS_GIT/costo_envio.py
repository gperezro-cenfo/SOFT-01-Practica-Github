peso = float(input("Peso del paquete (kg): "))
destino = input("Destino (N = nacional, I = internacional): ")
costo = 2500
if peso > 5:
    costo = costo + (peso - 5) * 800
if destino == "I":
    costo = costo * 3
elif destino != "N":
    costo = 0
    print("Destino no válido")
print("Costo del envío:", costo)