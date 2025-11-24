import csv

# Ruta al archivo de administradores
admin_route = "csv/admins.csv"
# Ruta al archivo de artefactos
artifact_route = "csv/artefactos.csv"
# Ruta al archivo de visitantes
visitors_route = "csv/visitors.csv"
# Ruta al archivo de reportes de seguridad
security_route = "csv/security.csv"

def leer_csv(ruta):
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        return [dict(fila) for fila in lector]

def escribir_csv(ruta, campos, datos):
    with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for fila in datos:
            escritor.writerow(fila)

def agregar_fila_csv(ruta, campos, fila):
    with open(ruta, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writerow(fila)

def reescribir_csv_sin_fila(ruta, campos, datos, id_eliminar, campo_id='id'):
    nueva_lista = [fila for fila in datos if fila[campo_id] != id_eliminar]
    escribir_csv(ruta, campos, nueva_lista)
