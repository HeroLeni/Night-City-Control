def contar_elementos_recursivo(lista, contador=0):
    if not lista:
        return contador
    return contar_elementos_recursivo(lista[1:], contador + 1)

def mostrar_tuplas_lista(lista):
    return tuple(tuple(elemento.values()) for elemento in lista)

def mostrar_estadisticas_visitantes(*args, **kwargs):
    visitantes = args[0]  
    total = len(visitantes)
    especies = set()
    estados = {'Activo': 0, 'Retirado': 0}
    for visitante in visitantes:
        especies.add(visitante['Especie'])
        estado = visitante['Estado']
        if estado in estados:
            estados[estado] += 1
    extra = kwargs.get('extra', '')
    estadisticas = {
        'Total': total,
        'Especies': especies,
        'Activos': estados['Activo'],
        'Retirados': estados['Retirado'],
        'Extra': extra
    }
    return estadisticas

def filtrar_por_kwargs(lista, **kwargs):
    resultado = []
    for elemento in lista:
        coincide = all(elemento.get(k) == v for k, v in kwargs.items())
        if coincide:
            resultado.append(elemento)
    return resultado
