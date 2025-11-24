from auth import autenticar_usuario
from visitors import registrar_visitante
from artifacts import registrar_artefacto
from security import registrar_reporte_seguridad

print("Night City Control")

def menu_principal():
    while True:
        print("1. Registro de Visitantes")
        print("2. Reporte de artefactos")
        print("3. Reporte de seguridad")
        print("4. Salir")
        opcion_menu = input("Ingresa una opción del menú (1-4): ")

        match opcion_menu:
            case "1":
                registrar_visitante()
            case "2":
                registrar_artefacto()
            case "3":
                registrar_reporte_seguridad()
            case "4":
                print("Que tengas una excelente noche")
                break
            case _:
                print("Error, opción inválida")

# Inicio de sesión:
#importa del auth y aca se verifica
es_super_admin = autenticar_usuario()

if es_super_admin:
    print("Bienvenido al Control Night City!")
    menu_principal()
else:
    print("Error, contraseña o usuario incorrecto")