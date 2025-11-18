# read_write.py
# Módulo para leer y escribir archivos

def read_file(archive):
    try:
        print(f"Leyendo archivo {archive}")
        with open(archive, "r", encoding="utf-8") as file:
            
            print(content := file.read())
        print(f"\nArchivo {archive} leído correctamente. ✅")
    except FileNotFoundError:
        print("❌ No se ha encontrado el archivo.")
    except Exception as e:
        print("❌ Error en la lectura del archivo: {e}")

def write_file(archive, dict):

    try:
        print(f"Escribiendo archivo {archive}")
        with open(archive, "w", encoding="utf-8") as file:
            for i, line in enumerate(dict, 1):
                file.write(f"\nGato {i}")
                for key, value in line.items():
                    file.write(f"\n{key}: {value}")
                file.write("\n----------------")

        print(f"\nArchivo {archive} creado y escrito correctamente. ✅")
    except Exception as e:
        print(f"❌ Error en la escritura del archivo: {e}")