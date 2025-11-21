import datetime

# 1. Fecha y hora actual
fecha_hora_actual = datetime.datetime.now()
print(f"Fecha y hora actual: {fecha_hora_actual}")

# 2. Cálculo de edad
anio_nacimiento = int(input("\nIntroduce tu año de nacimiento: "))
anio_actual = datetime.date.today().year
edad = anio_actual - anio_nacimiento
print(f"Tu edad es: {edad} años")

# 3. Días restantes del año
hoy = datetime.date.today()
fin_de_anio = hoy.replace(month=12, day=31)
dias_restantes = (fin_de_anio - hoy).days
print(f"\nDías restantes para que termine el año: {dias_restantes} días")
