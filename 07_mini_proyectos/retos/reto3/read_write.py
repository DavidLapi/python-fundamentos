# read_write.py
# Módulo para leer y escribir archivos

def read_content(archive):
    try:
        with open(archive, "r", encoding="utf-8") as file:

            print(f"Leyendo archivo {archive}...")
            print(file.read())
            
        return True

    except FileNotFoundError:
        print("❌ No se ha encontrado el archivo a leer.")
        return False
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return False

def write_content(archive, lines):

    try:
        with open(archive, "w", encoding="utf-8") as file:
            print(f"\nEscribiendo archivo {archive}...")
            for line in lines:
                file.write(f"\n{line}")

        print(f"Archivo {archive} escrito correctamente ✅")
        return True
    except Exception as e:
        print(f"❌ Error al escribir el archivo: {e}")
        return False