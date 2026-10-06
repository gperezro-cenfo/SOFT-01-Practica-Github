# Ejercicio: Análisis y mejora 
# de programas con flujo condicional

# Datos de entrada
compra = float( input( "Monto de la compra: "))

# Definición de constantes
# Se determina que estos valores no cambiarán 
# durante la ejecución del programa,
# por lo que se definen como constantes.
RANGO_UNO = 100000
RANGO_DOS = 60000
RANGO_TRES = 30000

# Definición de variables
# Se determina que estos valores pueden 
# cambiar durante la ejecución del programa,
# por lo que se definen como variables.
descuento = 0
descuento_uno = 0.15
descuento_dos = 0.10
descuento_tres = 0.05

# condicionales
if compra >= RANGO_UNO:
    descuento = compra * descuento_uno
elif compra >= RANGO_DOS:
    descuento = compra * descuento_dos
elif compra >= RANGO_TRES:
    descuento = compra * descuento_tres

# Cálculo del total
total = compra - descuento

# Datos de salida
print("Descuento:", descuento)
print("Total:", total)