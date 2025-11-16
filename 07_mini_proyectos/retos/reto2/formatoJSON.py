# formatoJSON.py
# Módulo donde se almacenan funciones de leer y guardar archivo en formato JSON

# TODO 1: Importar módulos 'os' y'json'
import os, json

# TODO 2: Función que guarda datos al archivo JSON
def guardar_archivo(ruta, datos):
    
    # Validación por si el nombre del archivo introducido ya existe
    # Si existe el archivo, salta el mensaje de error y muestra el contenido de dicho archivo
    if os.path.exists(ruta):
        print(f"\n❌ El archivo {ruta} existe.")
        print("\nMostrando contenido del archivo existente...")
        leer_archivo(ruta)
    else:
        # Si no existe, se empieza a crear el archivo
        print(f"Escribiendo datos en {ruta}...")
        # Intentemos escribir el archivo JSON si no hay error
        try:
            # Escribimos archivo JSON usando 'with open()' y 'json.dump()'
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            # Mensaje de éxito de escritura de datos
            print(f"Archivo {ruta} creado y escrito correctamente. ✅")
            # Leer los datos escritos
            print(f"\nImprimiendo archivo {ruta}...")
            leer_archivo(ruta)
        # Mensaje de error si hay error al escribir
        except Exception as e:
            print(f"❌ Ups! Ha habido un error: {e}")

# TODO 3: Función para leer un archivo
def leer_archivo(ruta):
    # Intentemos que lea el archivo si se encuentra el archivo
    try:
        # Leemos archivo JSON usando 'with open()' y 'json.load()'
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            print(f"\n{datos}")
        print(f"Archivo {ruta} leído correctamente ✅")
    # Mensaje de error si no se encuentra el archivo
    except FileNotFoundError:
        print(f"\n❌ No se ha encontrado el archivo {ruta}")
    # Mensaje de error si hay error al leer
    except Exception as e:
            print(f"❌ Ups! Ha habido un error: {e}")