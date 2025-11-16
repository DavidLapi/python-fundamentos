# Reto 2: Validador de formulario
# Enunciado: Crea un programa que pida datos de registro y los valide:
# - Nombre (mínimo 3 caracteres)
# - Email (debe contener @)
# - Edad (debe ser número entre 18 y 100)
# - Contraseña (mínimo 6 caracteres)
#
# **Requisitos**:
# - Usa operador morsa en TODAS las validaciones
# - Repite la pregunta si el dato no es válido
# - Muestra un resumen al final
# - Guarda los datos en un archivo JSON 

# TODO 1: Importar función validador de formularios en el módulo 'formulario'
from formulario import validar_formulario

# TODO 2: Crear función principal
def main():
    # Imprimir título del reto
    print("--- Validador de formulario ---")
    # Llamar función validar_formulario (más información en 'formulario.py')
    validar_formulario()
    # Imprimir mensaje de despedida
    print("\nHasta pronto! 👋")

# TODO 3: Punto de entrada del programa
if __name__ == "__main__":
    main()