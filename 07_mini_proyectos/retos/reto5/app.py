# Reto 5: Mini sistema de tickets
# **Enunciado: **
# - Usa listas y diccionarios para manejar tickets (id, título, estado).
# - Operaciones: crear, listar, cerrar.
# - Persistencia opcional en archivo.
# **Bonus**: Usa operador morsa en el menú principal.

import json
from tickets import mostrar_menu

def main():
    print("--- Mini sistema de tickets ---")

    tickets = []
    next_id = 1
    archivo = "contenido.json"

    print("\nLeyendo archivo...")
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            if (contenido := json.load(file)):
                lista = contenido
                next_id = max(l["id"] for l in lista) + 1

    except FileNotFoundError:
        print("❌ No se ha encontrado el archivo.")
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")

    mostrar_menu(tickets, next_id)

    try:
        with open(archivo, "w", encoding="utf-8") as file:
            print(f"Escribiendo tickets en archivo {archivo}...")
            json.dump(tickets, file, indent=2, ensure_ascii=False)
        print(f"Tickets guardados en {archivo} ✅")
    except Exception as e:
        print(f"❌ Error al escribir el archivo: {e}")

    print("\nHasta pronto 👋")

if __name__ == "__main__":
    main()