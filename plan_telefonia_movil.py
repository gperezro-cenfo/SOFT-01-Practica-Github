# Ejercicio realizado en clase de programación 1, 2026 #

# Plan de telefonía móvil #

plan = input("Ingrese el plan seleccionado (Basico, Plus o Pro): ")
gb_consumidos = float(input("Ingrese la cantidad de GB consumidos: "))
meses = int(input("Ingrese la cantidad de meses con la empresa: "))

# Determinar precio y GB incluidos según el plan
if plan == "basico":
    precio_plan = 8000
    gb_incluidos = 10
    nombre_plan = "Básico"

elif plan == "plus":
    precio_plan = 12000
    gb_incluidos = 25
    nombre_plan = "Plus"

elif plan == "pro":
    precio_plan = 18000
    gb_incluidos = 50
    nombre_plan = "Pro"

else:
    print("Plan inválido")
    exit()


# variables
gb_adicionales = 0
costo_adicional = 0
descuento = 0


# Calcular consumo adicional
if gb_consumidos > gb_incluidos:
    gb_adicionales = gb_consumidos - gb_incluidos
    costo_adicional = gb_adicionales * 500


# Calcular descuento por antigüedad
if meses >= 12:
    descuento = precio_plan * 0.10


# Calcular total de la factura
total_factura = precio_plan - descuento + costo_adicional


# Mostrar resultados
print("--- FACTURA DEL PLAN MÓVIL ---")
print("Plan seleccionado:", nombre_plan)
print("GB incluidos:", gb_incluidos)
print("GB consumidos:", gb_consumidos)
print("GB adicionales:", gb_adicionales)
print("Costo adicional: ₡", costo_adicional)
print("Descuento: ₡", descuento)
print("Precio del plan: ₡", precio_plan)
print("Total de la factura: ₡", total_factura)