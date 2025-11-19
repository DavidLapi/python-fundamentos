# logs.py
# Módulo donde lee un archivo de logs, separa por espacio, cuenta por tipo o fecha
# Además, guarda los logs en 'resumen.txt'

# Función para leer archivo logs y escribir su resumen
def log(entrada, salida):

    contador_fecha = {}
    contador_tipo = {}

    try:
        with open(entrada, "r", encoding="utf-8") as file:
            
            for line in file:
                line = line.strip()

                if not line:
                    continue

                if len(partes := line.split()) < 3:
                    continue

                fecha = partes[0]
                hora = partes[1]
                tipo = partes[2]

                # Contar por tipo de log
                if tipo in contador_tipo:
                    contador_tipo[tipo] += 1
                else:
                    contador_tipo[tipo] = 1
            
                # Contar por fecha
                if fecha in contador_fecha:
                    contador_fecha[fecha] += 1
                else:
                    contador_fecha[fecha] = 1

        # Mostrar resultados en pantalla
        print("--- RESUMEN DE LOGS ---")

        print("\n🔍 Conteo por tipo de log:")
        for tipo, cantidad in sorted(contador_tipo.items()):
            print(f"  {tipo}: {cantidad}")

        print("📅 Conteo por fecha:")
        for fecha, cantidad in sorted(contador_fecha.items()):
            print(f"  {fecha}: {cantidad}")

        # Guardar resultados en resumen.txt
        with open(salida, "w", encoding="utf-8") as out:
            out.write("RESUMEN DE ANÁLISIS DE LOGS\n")

            # Escribir conteo por tipo
            out.write("CONTEO POR TIPO DE LOG:\n")
            for tipo, cantidad in sorted(contador_tipo.items()):
                out.write(f"{tipo}: {cantidad}\n")
            out.write("\n")
    
            # Escribir conteo por fecha
            out.write("CONTEO POR FECHA:\n")
            for fecha, cantidad in sorted(contador_fecha.items()):
                out.write(f"{fecha}: {cantidad}\n")
            out.write("\n")
    
            # Escribir totales
            total_logs = sum(contador_tipo.values())
            out.write(f"TOTAL DE LOGS PROCESADOS: {total_logs}\n")

        print(f"Resumen guardado en {salida}")
    
    except FileNotFoundError:
        print("❌ No se ha encontrado el archivo.")
    except Exception as e:
        print(f"❌ Error al leer o escribir datos: {e}")