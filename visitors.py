from storage import leer_csv, escribir_csv, agregar_fila_csv, visitors_route

CAMPOS_VISITANTES = [
    "id_visitante",
    "nombre_visitante",
    "tipo_visitante",
    "edad_visitante",
    "peso_visitante",
    "planeta_visitante",
    "estado_visitante"
]

def obtener_nuevo_id():
    visitantes = leer_csv(visitors_route)
    if not visitantes:
        return "V001"
    ids = [int(v['id_visitante'][1:]) for v in visitantes if v['id_visitante'].startswith('V')]
    max_id = max(ids) if ids else 0
    return f"V{str(max_id + 1).zfill(3)}"

def registrar_visitante():
    id_nuevo = obtener_nuevo_id()
    print(f"ID asignado: {id_nuevo}")
    datos = {
        "id_visitante": id_nuevo,
        "nombre_visitante": input("Ingresa el nombre del visitante: "),
        "tipo_visitante": input("Ingresa el tipo de visitante: "),
        "edad_visitante": input("Ingresa la edad del visitante: "),
        "peso_visitante": input("Ingresa el peso del visitante: "),
        "planeta_visitante": input("Ingresa el planeta del visitante: "),
        "estado_visitante": input("Estado: Activo / Retirado: ")
    }
    agregar_fila_csv(visitors_route, CAMPOS_VISITANTES, datos)
    print("Visitante registrado exitosamente.")

def listar_visitantes():
    visitantes = leer_csv(visitors_route)
    for visitante in visitantes:
        print(tuple(visitante[c] for c in CAMPOS_VISITANTES))

def buscar_visitante():
    visitantes = leer_csv(visitors_route)
    buscar_id = input("Ingrese el ID a buscar: ")
    for visitante in visitantes:
        if visitante["id_visitante"] == buscar_id:
            print("Datos del visitante:")
            print(visitante)
            return
    print("No está registrado el visitante.")

def modificar_visitante():
    visitantes = leer_csv(visitors_route)
    id_modificar = input("ID del visitante a modificar: ")
    for visitante in visitantes:
        if visitante["id_visitante"] == id_modificar:
            print("Datos actuales:", visitante)
            for campo in CAMPOS_VISITANTES[1:]:
                nuevo = input(f"Nuevo valor para {campo} (Actual: {visitante[campo]}): ")
                if nuevo:
                    visitante[campo] = nuevo
            escribir_csv(visitors_route, CAMPOS_VISITANTES, visitantes)
            print("Visitante modificado.")
            return
    print("No existe ese ID.")

def eliminar_visitante():
    visitantes = leer_csv(visitors_route)
    id_eliminar = input("ID del visitante a eliminar: ")
    nuevos = [v for v in visitantes if v["id_visitante"] != id_eliminar]
    if len(nuevos) < len(visitantes):
        escribir_csv(visitors_route, CAMPOS_VISITANTES, nuevos)
        print("Visitante eliminado.")
    else:
        print("No existe ese ID.")
        print("este visitante no esta registrado")