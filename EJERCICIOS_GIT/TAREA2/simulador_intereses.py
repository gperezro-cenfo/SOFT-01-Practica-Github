# Constantes
MAX_PERIOD = 120
MONTHS_PER_YEAR = 12
PERCENTAGE_BASE = 100

# Variables generales
month = 0

# Datos de entrada
saving_initial = float(input("Ingrese el monto inicial de ahorro: "))
saving_monthly = float(input("Ingrese el monto de ahorro mensual: "))
saving_interest = (
    float(input("Ingrese la tasa de interés mensual: ")) / PERCENTAGE_BASE
)
saving_goal = float(input("Ingrese el monto objetivo de ahorro: "))
display_frequency = input(
    "¿Desea ver el estado de cuenta mensual o anual? "
).strip().lower()

while display_frequency not in ("mensual", "anual"):
    print("Frecuencia de visualización no válida. Vuelva a intentarlo.")
    display_frequency = input(
        "¿Desea ver el estado de cuenta mensual o anual? "
    ).strip().lower()

# Cálculos
balance = saving_initial

while balance < saving_goal and month < MAX_PERIOD:
    interest = balance * saving_interest
    balance = balance + interest + saving_monthly
    month += 1

    if display_frequency == "mensual":
        print("Mes:", month, "Balance:", round(balance, 2))
    elif display_frequency == "anual" and (
        month % MONTHS_PER_YEAR == 0
        or balance >= saving_goal
        or month == MAX_PERIOD
    ):
        # Muestra el saldo anual o si termina anticipadamente.
        print("Mes:", month, "Balance:", round(balance, 2))

if balance >= saving_goal:
    print(
        "Meta alcanzada en el mes", month,
        "con un balance de", round(balance, 2)
    )
else:
    print(
        "Meta no alcanzada en", MAX_PERIOD,
        "meses. Balance final:", round(balance, 2)
    )
    print("Faltante para la meta:", round(saving_goal - balance, 2))