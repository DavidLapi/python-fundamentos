# Reto 4: Estadísticas del refugio de gatos
# **Enunciado: **
# - Entrada: archivo o lista de pesos y edades.
# - Tareas: conteo, media, mediana simple, top-k más pesados.
# - Salida: resumen por pantalla y guardado opcional a archivo.
# **Bonus**: Usa operador morsa para leer el archivo línea por línea.

from read_write import read_file, write_file
from filtertodo import multitask, write

def main():

    print("--- Estadísticas del refugio de gatos ---")

    gatos = [
        {"nombre": "Michi", "edad": 9, "peso": 6.9},
        {"nombre": "Leo", "edad": 4, "peso": 4.8},
        {"nombre": "Nico", "edad": 5, "peso": 5.0},
        {"nombre": "Chachito", "edad": 10, "peso": 13.2}
    ]

    write_file("gatos.txt", gatos)

    read_file("gatos.txt")

    media_edad, media_peso, mediana_edad, mediana_peso, top_3_pesados = multitask(gatos)

    resumen = [media_edad, media_peso, mediana_edad, mediana_peso, top_3_pesados]

    write("resumen.txt", resumen)
    

if __name__ == "__main__":
    main()