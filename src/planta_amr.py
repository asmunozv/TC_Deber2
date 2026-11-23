"""Fase B: rutas AMR, Figura 5 del enunciado USFQ. Pesos en metros."""
from heapq import heappop, heappush
from math import isfinite

ARISTAS_FIGURA = (
    ('R','A',4), ('R','B',2), ('A','B',1), ('A','P',3),
    ('A','E',5), ('B','P',7), ('B','C',3), ('C','P',2),
    ('P','E',2), ('C','E',4), ('E','D',3),
)
NOMBRES = {'R':'Recepción','A':'Pasillo A','B':'Pasillo B',
           'C':'Pasillo C','P':'Picking','E':'Empaque','D':'Despacho'}

def construir_planta(aristas=ARISTAS_FIGURA, nombres=NOMBRES):
    grafo = {v: {} for v in nombres}
    for u,v,peso in aristas:
        if u not in grafo or v not in grafo or u == v:
            raise ValueError('Extremos no registrados o lazo inválido')
        if type(peso) not in (int,float) or not isfinite(peso) or peso < 0:
            raise ValueError('Los pesos deben ser números finitos no negativos')
        if v in grafo[u]:
            raise ValueError('Arista duplicada')
        grafo[u][v] = peso
        grafo[v][u] = peso
    return grafo

def dijkstra_amr(grafo, origen, destino, bloqueadas=()):
    """Ruta y distancia mínima, o None. No atraviesa zonas bloqueadas."""
    if origen not in grafo or destino not in grafo:
        raise ValueError('Origen o destino inexistente')
    bloqueadas = set(bloqueadas)
    if not bloqueadas.issubset(grafo):
        raise ValueError('Zona bloqueada inexistente')
    if origen in bloqueadas or destino in bloqueadas:
        raise ValueError('Origen o destino bloqueado')
    for u, vecinos in grafo.items():
        for v, peso in vecinos.items():
            if v not in grafo or type(peso) not in (int,float) or not isfinite(peso) or peso < 0:
                raise ValueError('Conexión o peso inválido')
            if grafo[v].get(u) != peso:
                raise ValueError('Grafo debe ser no dirigido y simétrico')
    dist = {v: float('inf') for v in grafo}
    prev = {}
    dist[origen] = 0
    cola = [(0, origen)]
    while cola:
        du, u = heappop(cola)
        if du != dist[u]:
            continue
        if u == destino:
            break
        for v, peso in grafo[u].items():
            if v in bloqueadas:
                continue
            alt = du + peso
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heappush(cola, (alt,v))
    if dist[destino] == float('inf'):
        return None
    ruta = [destino]
    while ruta[-1] != origen:
        ruta.append(prev[ruta[-1]])
    return ruta[::-1], dist[destino]

def costo_ruta(grafo, ruta):
    if not ruta or any(v not in grafo for v in ruta):
        raise ValueError('Ruta inválida')
    costo = 0
    for u,v in zip(ruta,ruta[1:]):
        if v not in grafo[u]:
            raise ValueError('Tramo inexistente')
        costo += grafo[u][v]
    return costo

if __name__ == '__main__':
    planta = construir_planta()
    resultado = dijkstra_amr(planta,'R','D')
    print('Ruta mínima R→D:', ' → '.join(resultado[0]), '=', resultado[1], 'm')
    ruta_figura = ['R','B','A','P','E','D']
    print('Ruta resaltada en Figura 5:', ' → '.join(ruta_figura), '=', costo_ruta(planta,ruta_figura), 'm')
    print('Con P bloqueado:', dijkstra_amr(planta,'R','D',{'P'}))
    print('Con A y P bloqueados:', dijkstra_amr(planta,'R','D',{'A','P'}))
