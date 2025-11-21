print ("Hola mundo")

def saludar_nombres(nombres):
    
    # Esta función toma una lista de nombres y saluda a cada uno.
    
    for nombre in nombres:
        print (f"Hola, {nombre}!")

# Llama a la función con una lista de nombres

lista_nombres = ["DAVID", "JUAN JOSE", "JACOBO"]

saludar_nombres(lista_nombres)