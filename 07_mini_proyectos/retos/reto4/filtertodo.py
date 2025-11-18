# filtertodo.py
# Módulo donde se calcula el conteo, la media, la mediana simple y el top-k más pesados de la lista de gatos

def multitask(archive, list):

    datos_edad = []
    datos_peso = []

    try:
        with open(archive, "r", encoding="utf-8") as file:
            while (linea := file.readline()):
                if (linea_edad := linea.strip()) and linea_edad.startswith("edad"):
                    datos_edad.append(linea_edad)
                elif (linea_peso := linea.strip()) and linea_peso.startswith("peso"):
                    datos_peso.append(linea_peso)

        
        for i in datos_edad:
            print(i)
        
        for y in datos_peso:
            print(y)

    except FileNotFoundError:
        print("❌ No se ha encontrado el archivo")
    except Exception as e:
        print(f"❌ Error en la lectura del archivo: {e}")