# formulario.py
# Archivo donde se almacena la validación del formulario

# TODO 1: Importar función que guarda datos de formulario en un archivo JSON en el módulo formatoJSON
from formatoJSON import guardar_archivo

# TODO 2: Función que valida el formulario
def validar_formulario():
    # Validación de nombre que tenga más de 3 carácteres
    while not (nombre := input("\nIntroduce un nombre: ")) or len(nombre) < 3:
        print("❌ Nombre inválido. El nombre debe tener al menos 3 caracteres.")
    # Validación de email que contenga al menos un '@' y un '.'
    while "@" not in (email := input("\nIntroduce un email válido: ")) or "." not in email:
        print("❌ Email inválido. El email debe contener al menos un @ y un punto (.).")
    # Validación de edad que sea número entero y que esté comprendido entre 18 y 100
    while True:
        try:
            if not (edad := int(input("\nIntroduce su edad: "))) or edad < 18 or edad > 100:
                print("❌ Edad no válida. La edad debe ser entre 18 y 100 años.")
                continue
            break
        except ValueError:
            print("❌ Edad no válida. La edad debe ser un número.")
            continue
    # Validación de contraseña que tenga más de 6 carácteres 
    while not (contrasena := input("\nIntroduce una contraseña: ")) or len(contrasena) < 6:
        print("❌ Contraseña no válida. Debe tener al menos 6 caracteres.") 
    # Imprimimos resumen del formulario
    print("\n--- Resumen ---")

    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print(f"Edad: {edad}")
    print(f"Contraseña: {contrasena}")
    # Pregunta del programa si desea guardar los datos en un archivo JSON o perder los datos para siempre
    if not (guardar := input("\n¿Desea almacenar estos datos en un archivo JSON? (s/n) --> ")) or guardar != "s":
        print("Datos no almacenados en JSON. Eliminando datos introducidos 🗑️")
    else:
        # Pedir al usuario un nombre para el archivo JSON (Inválido estar vacío o que sólo tenga números)
        while not (texto := input("\nEscribe un nombre para el archivo JSON --> ")) or texto.isdigit():
            print("❌ Nombre inválido.")

        # Declarar diccionario con los datos guardados
        resumen = {
            "nombre": nombre,
            "email": email,
            "edad": edad,
            "contrasena": contrasena
        }
        # Convertir texto en archivo JSON
        textoJSON = texto + ".json"
        # Llamar función 'guardar_archivo' para almacenar los datos en JSON (más información en formatoJSON.py)
        guardar_archivo(textoJSON, resumen)  