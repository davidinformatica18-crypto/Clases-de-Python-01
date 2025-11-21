import os

# 1. Directorio actual
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# 2. Crear carpeta
nombre_carpeta = "prueba_python"

# Comprobar si la carpeta ya existe para evitar errores
if not os.path.exists(nombre_carpeta):
    os.mkdir(nombre_carpeta)
    print(f"Carpeta '{nombre_carpeta}' creada correctamente.")
else:
    print(f"La carpeta '{nombre_carpeta}' ya existe.")

# 3. Listar archivos y carpetas
print("\nArchivos y carpetas en el directorio actual:")
for elemento in os.listdir():
    print("-", elemento)

    