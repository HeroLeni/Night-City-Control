from storage import leer_csv, escribir_csv, agregar_fila_csv, artifact_route
import shutil

CAMPOS_ARTEFACTOS = [
    "id_artefacto",
    "nombre_artefacto",
    "tipo_artefacto",
    "peso_artefacto",
    "tamaño_artefacto"
]



def exportar_artefactos_csv():
    destino = 'C:/Users/juane/Downloads/artefactos.csv'  # Ruta de destino
    shutil.copy(artifact_route, destino)
    print(f"El archivo se ha copiado a: {destino}")

def obtener_nuevo_id_artefacto():
    artefactos = leer_csv(artifact_route)
    if not artefactos:
        return "A001"
    ids = [int(a['id_artefacto'][1:]) for a in artefactos if a['id_artefacto'].startswith('A')]
    max_id = max(ids) if ids else 0
    return f"A{str(max_id + 1).zfill(3)}"

def registrar_artefacto():
    id_nuevo = obtener_nuevo_id_artefacto()
    print(f"ID asignado: {id_nuevo}")
    datos = {
        "id_artefacto": id_nuevo,
        "nombre_artefacto": input("Nombre del artefacto: "),
        "tipo_artefacto": input("Tipo de artefacto: "),
        "peso_artefacto": input("Peso del artefacto: "),
        "tamaño_artefacto": input("Tamaño del artefacto: ")
    }
    agregar_fila_csv(artifact_route, CAMPOS_ARTEFACTOS, datos)
    print("Artefacto registrado exitosamente.")

def listar_artefactos():
    artefactos = leer_csv(artifact_route)
    for artefacto in artefactos:
        print(tuple(artefacto[c] for c in CAMPOS_ARTEFACTOS))

def buscar_artefacto():
    artefactos = leer_csv(artifact_route)
    buscar_id = input("Ingrese el ID de artefacto: ")
    for a in artefactos:
        if a["id_artefacto"] == buscar_id:
            print("Datos del artefacto:")
            print(a)
            return
    print("No existe ese artefacto.")

def eliminar_artefacto():
    artefactos = leer_csv(artifact_route)
    id_eliminar = input("ID del artefacto a eliminar: ")
    nuevos = [a for a in artefactos if a["id_artefacto"] != id_eliminar]
    if len(nuevos) < len(artefactos):
        escribir_csv(artifact_route, CAMPOS_ARTEFACTOS, nuevos)
        print("Artefacto eliminado.")
    else:
        print("No existe ese ID.")
