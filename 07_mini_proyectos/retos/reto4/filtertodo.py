# filtertodo.py
# Módulo donde se calcula el conteo, la media, la mediana simple y el top-k más pesados de la lista de gatos

def multitask(list):

    print("\n--- Tareas de la lista de gatos---")

    print("\n--- Conteo ---")
    print(f"Total de gatos: {(contador := len(list))}")

    print("\n--- Media (Promedio) ---")
    media_edad = (suma_edades := sum(gato["edad"] for gato in list)) / contador
    print(f"Promedio de la edad de los gatos: {media_edad:.2f} años")

    media_peso = (suma_peso := sum(gato["peso"] for gato in list)) / contador
    print(f"Promedio del peso de los gatos: {media_peso:.2f} kgs")

    print("\n--- Mediana simple ---")
    # La mediana es el valor central cuando los datos están ordenados
    # Extraemos y ordenamos las edades
    m = len(edades_ordenadas := sorted(gato["edad"] for gato in list))

    # Calcular la mediana de la edad
    if m % 2 == 0: # Si hay cantidad par de elementos
        # Promedio de los dos valores centrales
        mediana_edad = (edades_ordenadas[m//2 - 1] + edades_ordenadas[m//2]) / 2
    else: # Si hay cantidad impar
        # El valor del medio  
        mediana_edad = edades_ordenadas[m//2]
    
    # Extraemos y ordenamod los pesos
    m = len(pesos_ordenados := sorted(gato["peso"] for gato in list))

    # Calcular la mediana del peso
    if m % 2 == 0:
        mediana_peso = (pesos_ordenados[m//2 - 1] + pesos_ordenados[m//2]) / 2
    else:
        mediana_peso = pesos_ordenados[m//2]

    print(f"Mediana de edad: {mediana_edad:.2f} años")
    print(f"Mediana de peso: {mediana_peso:.2f} kgs")

    print("\n===== TOP 3 GATOS MÁS PESADOS =====")
    # Ordenar los gatos por peso de mayor a menor
    # sorted() con key=lambda: Ordena los diccionarios según el campo que elijas
    gatos_por_peso = sorted(list, key=lambda gato: gato["peso"], reverse=True)

    # Tomar sólo los 3 primeros gatos ordenados por peso
    top_3_pesados = gatos_por_peso[:3]

    for i, gato in enumerate(top_3_pesados, 1):
        print(f"{i}. {gato['nombre']} | Edad: {gato['edad']} años | Peso: {gato['peso']} kgs.")
    
    return media_edad, media_peso, mediana_edad, mediana_peso, top_3_pesados

def write(archive_out, resumen):
    try:
        with open(archive_out, "w", encoding="utf-8") as file:
            for i, linea in enumerate(resumen, 1):
                if i == 1:
                    file.write(f"Promedio de edad: {linea} años.\n")
                elif i == 2:
                    file.write(f"\nPromedio de peso: {linea} kgs.\n")
                elif i == 3:
                    file.write(f"\nMediana de edad: {linea} años.\n")
                elif i == 4:
                    file.write(f"\nMediana de peso: {linea} kgs.\n")
                elif i == 5:
                    file.write(f"\nTop 3 gatos más pesados:\n{linea}")
                
        print(f"\nArchivo {archive_out} escrito correctamente ✅")

    except FileNotFoundError:
        print("❌ No se ha encontrado el archivo")
    except Exception as e:
        print(f"❌ Error en la lectura del archivo: {e}")