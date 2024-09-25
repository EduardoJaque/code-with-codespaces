# Explicar que es esto
print("Esta es una calculadora de ahorros anuales")

# Pedir nombre a la persona y saludar
nombre = input("¿Cuál es tu nombre? ")
print("Hola", nombre)

# Pedir horas trabajadas, ganancia por hora, y gastos
ganancia = int(input("¿Cuánto ganas por hora? "))
horas = int(input("¿Cuántas horas trabajas a la semana? "))
gastos = int(input("¿Cuánto gastas a la semana? "))

# Calcular salario semanal
salario_semanal = ganancia * horas - gastos

# Calcular salario anual
salario_anual = (salario_semanal * 52 )

# Calcular ahorros anuales
ahorros_anuales = (ganancia * horas * 52) - salario_anual

# Mostrar resultados
print("Tienes una ganancia anual de:", salario_anual, "esto es descontando los gastos")
print("Tus ahorros pueden ser de:", ahorros_anuales)
print("Gastos anuales:", gastos * 52)
