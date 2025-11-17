# Reto 3: Analizador de archivo línea por línea
# Enunciado: Crea un programa que lea un archivo línea por línea y procese solo las que cumplan ciertos criterios.
#
# **Requisitos**:
# - Usa operador morsa en el bucle de lectura
# - Filtra líneas que:
#   - No estén vacías
#   - No empiecen con `#` (comentarios)
#   - Tengan más de 10 caracteres
# - Cuenta cuántas líneas procesaste vs. cuántas ignoraste
# - Guarda las líneas válidas en otro archivo

# TODO 1: Importar módulos necesarios para las funciones
from read_write import read_content, write_content 
from line_filter import filter

# TODO 2: Crear función principal
def main():
    print("--- Analizador de archivos línea por línea ---")

    lista = [
        "# Este es un comentario",
        "Línea válida para procesar",
        "Corta",
        "",
        "# Otro comentario",
        "Esta línea también es válida y debe procesarse"
    ]

    # Pedir al usuario un nombre para el archivo de entrada para ver el contenido completo
    # while not (entrada := input("\nEscribe un nombre para el archivo de lineas --> ")) or entrada.isdigit():
        #print("❌ Nombre de entrada inválido.")
    
    # Pedir al usuario un nombre para el archivo de salida con las lineas filtradas
    # while not (entrada := input("\nEscribe un nombre para el archivo de lineas --> ")) or entrada.isdigit():
        # print("❌ Nombre de entrada inválido.")

    write_content("archivo.txt", lista)
    
    if read_content("archivo.txt"):
        filter("archivo.txt", "salida.txt")


# TODO 3: Punto de entrada del programa
if __name__ == "__main__":
    main()