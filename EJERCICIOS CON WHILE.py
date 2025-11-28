# ============================================================================================================================================
#   EJERCICIOS CON WHILE EJERCICIOS CON WHILE EJERCICIOS CON WHILE EJERCICIOS CON WHILE EJERCICIOS CON WHILE EJERCICIOS CON WHILE
# ============================================================================================================================================

# 1. contar_hasta_10(): Debe usar un bucle while para mostrar los números del 1 al 10 separados por comas.
#    Debe retornar un string, por ejemplo: "1,2,3,4,5,6,7,8,9,10" TODO: Implementar. _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

numero = 1
resultado = ""

while numero <= 10:
    resultado += str(numero) + ","
    numero += 1
  
print(resultado)

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 


# 2. suma_hasta_cero(): Pedir números al usuario hasta que introduzca 0.
#    Sumar todos los números (excepto el 0 final) y devolver el resultado. Usa un while.
#    IMPORTANTE: para testear este ejercicio no se usará input(),
#    sino que el alumno debe simular la lógica con input real.
#    En este archivo solo retorna un valor de ejemplo.
#    TODO: Implementar la lógica sin usar input()
#    pass _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

suma = 0
numero = int(input("Introduce un número: "))

while numero != 0:
    suma = suma + numero
    numero = int(input("Introduce un número: "))

print("Suma de todos los números introducidos:", suma)

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

# 3. def adivinar_numero(): Simula un juego donde el número secreto es 7.
#    Usa un while que repita intentos hasta acertar.
#    Para pruebas, simula una secuencia de intentos: 3, 5, 7.
#    Retorna la cantidad de intentos usados.
#    TODO: Implementar pass _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    
#    if __name__ == "__main__": print("Ejecutando tests...")
#    Test contar_hasta_10 assert contar_hasta_10() == "1,2,3,4,5,6,7,8,9,10", \
#    f"contar_hasta_10() debería devolver '1,2,3,4,5,6,7,8,9,10', pero devolvió {contar_hasta_10()}"
#    Test suma_hasta_cero  Para pruebas: 5 + 3 + 2 = 10 (El alumno debe simularlo en su código)
#    print("Cuando te lo pida introduce los numeros 5,3 y 2")
#    assert suma_hasta_cero() == 10, \ f"suma_hasta_cero() debería devolver 10, pero devolvió {suma_hasta_cero()}"

#    Test adivinar_numero Secuencia simulada: 3, 5, 7 → 3 intentos
#    assert adivinar_numero() == 3, \ "adivinar_numero() debería devolver 3, pero devolvió {adivinar_numero()}"

def adivinar_numero():
    intentos_simulados = [3, 5, 7]  # simula intentos
    secreto = 7
    indice = 0
    intentos = 0

    while True:
        intentos += 1
        if intentos_simulados[indice] == secreto:
            return intentos
        indice += 1

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _  _

# TAREA PARA CASA CREAR UNA PIRAMIDE

base = 10
cadena = "10"

print(cadena)

while base > 0:
    base -= 1
    cadena += str(base)
    print(cadena)

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 