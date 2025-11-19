# Reto 6: Parser de logs simple
# **Enunciado: **
# - Lee un archivo de logs, separa por espacio, cuenta por tipo o fecha.
# - Guarda resultados en `resumen.txt`.
# **Bonus**: Usa operador morsa para leer y filtrar líneas en una sola expresión.

from logs import log

def main():
    print("--- Parser de logs simple ---")
    
    archivo_entrada = "logs.log"
    archivo_salida = "resumen.txt"

    log(archivo_entrada, archivo_salida)

if __name__ == "__main__":
    main()