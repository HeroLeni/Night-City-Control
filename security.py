from storage import leer_csv, escribir_csv, agregar_fila_csv

security_route = "csv/security.csv"
CAMPOS_SEGURIDAD = [
    "id_reporte",
    "tipo_reporte",
    "hora_suceso",
    "involucrados"
]

def obtener_nuevo_id_reporte():
    reportes = leer_csv(security_route)
    if not reportes:
        return "S001"
    ids = [int(r['id_reporte'][1:]) for r in reportes if r['id_reporte'].startswith('S')]
    max_id = max(ids) if ids else 0
    return f"S{str(max_id + 1).zfill(3)}"

def registrar_reporte_seguridad():
    id_nuevo = obtener_nuevo_id_reporte()
    print(f"ID de reporte asignado: {id_nuevo}")
    datos = {
        "id_reporte": id_nuevo,
        "tipo_reporte": input("Tipo de reporte: "),
        "hora_suceso": input("Hora del suceso (HH:MM): "),
        "involucrados": input("Involucrados (separados por coma): ")
    }
    agregar_fila_csv(security_route, CAMPOS_SEGURIDAD, datos)
    print("Reporte de seguridad registrado.")

def listar_reportes():
    reportes = leer_csv(security_route)
    for reporte in reportes:
        print(tuple(reporte[c] for c in CAMPOS_SEGURIDAD))

def buscar_reporte():
    reportes = leer_csv(security_route)
    buscar_id = input("Ingrese el ID de reporte de seguridad: ")
    for r in reportes:
        if r["id_reporte"] == buscar_id:
            print("Datos del reporte:")
            print(r)
            return
    print("No existe ese reporte.")

def eliminar_reporte():
    reportes = leer_csv(security_route)
    id_eliminar = input("ID del reporte a eliminar: ")
    nuevos = [r for r in reportes if r["id_reporte"] != id_eliminar]
    if len(nuevos) < len(reportes):
        escribir_csv(security_route, CAMPOS_SEGURIDAD, nuevos)
        print("Reporte eliminado.")
    else:
        print("No existe ese ID.")
