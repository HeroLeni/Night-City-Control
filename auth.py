import csv
from storage import admin_route

def autenticar_usuario():
    usuario = input("Ingresa tu usuario: ")
    password = input("Ingresa tu contraseña: ")
    with open(admin_route, newline='', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila['username'] == usuario and fila['password'] == password:
                if fila['role'].lower() == "superadmin":
                    return True
    print("Usuario o contraseña incorrectos. Intenta nuevamente.")
    return autenticar_usuario()