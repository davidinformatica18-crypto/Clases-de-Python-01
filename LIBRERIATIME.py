import time

# 1. Temporizador simple: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

print ("1")   # Primero hacemos que muestre en persona
time.sleep(1) # LLamamos a la funcion a que espere 1 segundo

print ("2")
time.sleep(1)

print ("3")
time.sleep(1)

print ("Listo")

# 2. Medir tiempo de escritura _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# Guardar el tiempo antes de escribir
inicio = time.time()

# Pedir al usuario que escriba su nombre
nombre = input("Escribe tu nombre: ")

# Guardar el tiempo después de escribir
fin = time.time()

# Calcular la diferencia
tiempo_total = fin - inicio

# Mostrar resultado
print("Has tardado", tiempo_total, "segundos en escribir tu nombre.")
