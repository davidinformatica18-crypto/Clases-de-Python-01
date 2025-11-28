import random

# 1. Genera un número aleatorio entre 1 y 10 _ _ _ _ _ _ _ _
num = random.randint(0, 10)

# Pide al usuario que lo adivine
adivina = int(input("Adivina un número entre 1 y 10: "))

# Comprueba si acertó
if adivina == num:
    print("¡Has acertado! El número era", num)
else:
    print("No has acertado. El número era", num)

# 2. Generar tres números aleatorios entre 1 y 100 _ _ _ _ _ _
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

# Mostrar los números
print("Los 3 números aleatorios son:", num1, num2, num3)

# Calcular el promedio
promedio = (num1 + num2 + num3) / 3 

print("El promedio de los tres números es:", promedio)

# 3. Simulación de un dado:_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
dado = random.randint(1, 6)

#Mostrar el numero al tirar el dado
print("El numero de las 6 caras del dado", dado)