import math

# 1. Cálculo de raíz cuadrada
numero = float(input("Introduce un número para calcular su raíz cuadrada: "))
raiz = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es: {raiz}")

# 2. Área de un círculo
radio = float(input("\nIntroduce el radio de un círculo: "))
area = math.pi * math.pow(radio, 2)
print(f"El área del círculo con radio {radio} es: {area}")

# 3. Seno y coseno de un ángulo
angulo = float(input("\nIntroduce un ángulo en grados: "))
radianes = math.radians(angulo)
seno = math.sin(radianes)
coseno = math.cos(radianes)

print(f"El seno de {angulo}° es: {seno}")
print(f"El coseno de {angulo}° es: {coseno}")