# Constante periodo maximo
MAX_PERIOD = 120

# variables
month = 0

# Datos de entrada
saving_initial = float(input("Ingrese el monto inicial de ahorro: "))
saving_monthly = float(input("Ingrese el monto de ahorro mensual: "))
saving_interest = float(input("Ingrese la tasa de interés mensual: ")) / 100 
saving_goal = float(input("Ingrese el monto objetivo de ahorro: "))
display_frecuency = input("desea ver el estado de cuenta mensual o anual? ").strip().lower()

#calculos
balance = saving_initial

while balance < saving_goal and month < MAX_PERIOD:
    interest = balance * saving_interest
    balance = balance + interest + saving_monthly
    month += 1
    if display_frecuency == "mensual":
        print("Mes:", month, "Balance:", round(balance, 2))
    elif display_frecuency == "anual" and (month % 12 == 0 or balance >= saving_goal or month == MAX_PERIOD): # en casos de que la meta se cumpla antes de un año o se llegue al maximo periodo, se imprime el balance final
        print("Mes:", month, "Balance:", round(balance, 2))

if balance >= saving_goal:
    print("Meta alcanzada en el mes", month, "con un balance de", round(balance,2))
else:
    print("Meta no alcanzada en", MAX_PERIOD, "meses. Balance final:", round(balance, 2))
    print("Faltante para la meta: ", round(saving_goal - balance, 2))
