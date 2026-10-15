# Constante periodo maximo
MAX_PERIOD = 120

# variables
month = 0

# Datos de entrada
saving_initial = float(input("Ingrese el monto inicial de ahorro: "))
saving_monthly = float(input("Ingrese el monto de ahorro mensual: "))
saving_interest = float(input("Ingrese la tasa de interés mensual: ")) / 100 
saving_goal = float(input("Ingrese el monto objetivo de ahorro: "))
display_frecuency = input("desea ver el estado de cuenta mensual o anual? ").lower()

#calculos
balance = saving_initial

while balance < saving_goal and month < MAX_PERIOD:
    interest = balance * saving_interest
    balance = balance + interest + saving_monthly
    month += 1
    if display_frecuency == "mensual":
        print("Mes:", month, "Balance:", balance)
    elif display_frecuency == "anual" and month % 12 == 0:
        print("Mes:", month, "Balance:", balance)

if balance >= saving_goal:
    print("Meta alcancada en el mes", month, "con un balance de", round(balance,2))
else:
    print("Meta no alcanzada en", MAX_PERIOD, "meses. Balance final:", balance)
    print("Faltante para la meta: ", saving_goal - balance)
