# line_filter
# Módulo que filtra las líneas del archivo con los criterios asignados

def filter(entrada, salida):

    procesadas = 0
    ignoradas = 0
    lineas_validas = []

    try:
        with open(entrada, "r", encoding="utf-8") as archivo:
            while (linea := archivo.readline()):
                if (linea_limpia := linea.strip()) and not linea_limpia.startswith("#") and len(linea_limpia) > 10:
                    lineas_validas.append(linea_limpia)
                    procesadas += 1
                else:
                    ignoradas += 1
        
        with open(salida, "w", encoding="utf-8") as archivo:
            for linea in lineas_validas:
                archivo.write(f"\n{linea}")

        print("\n--- Resúmen de la filtración ---")
        print(f"✅ Procesadas: {procesadas} líneas")
        print(f"⏭️  Ignoradas: {ignoradas} líneas")
        print(f"📝 Resultado guardado en: {salida}")
        
    except FileNotFoundError:
        print(f"No se ha encontrado el archivo {entrada}")
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")