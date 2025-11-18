# tickets.py
# Módulo para crear, listar y cerrar tickets

def mostrar_menu(lista, id):
    while (opcion := input("\nOpciones:\n1)Crear ticket\n2)Listar ticket\n3)Cerrar ticket\n\nElige una opción --> ").strip()) != "4":
        if opcion == "1":
            if (titulo := input("\nTítulo del ticket --> ").strip()):
                lista.append({"id": id, "titulo": titulo, "estado": "abierto"})
                id += 1
                print(f"Ticket creado: {titulo}")
            else:
                print("❌ Título no válido")

        elif opcion == "2":
            if not lista:
                print("No hay tickets")
            else:
                for l in lista:
                    print(f"{l['id']}: {l['titulo']} | Estado: {l['estado']}")

        elif opcion == "3":
            while not (id_str := input("ID del ticket a cerrar: ").strip()).isdigit():
                print("ID no válido")

            id_ticket = int(id_str)
            for t in lista:
                
                if t["id"] == id_ticket:
                    t["estado"] = "cerrado"
                    print("Encontrado!! Ticket cerrado")
                    break
                else:
                    print("No se encontró el ticket o se sigue buscando...")
            
        else:
            print("❌ Opción no válida.")


