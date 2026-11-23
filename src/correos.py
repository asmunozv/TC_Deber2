"""Diez casos del simulador LOGISTPULSE.
Solucionadores exactos y verificadores separados. Python 3.10+.
"""
from collections import deque
from heapq import heappush, heappop
from itertools import permutations, combinations


def bfs_camino(g, origen, destino):
    if origen not in g or destino not in g:
        raise ValueError("Nodo inexistente")
    q = deque([origen])
    anterior = {origen: None}
    while q:
        u = q.popleft()
        if u == destino:
            ruta = []
            while u is not None:
                ruta.append(u)
                u = anterior[u]
            return ruta[::-1]
        for v in g[u]:
            if v not in g:
                raise ValueError("Arista a nodo inexistente")
            if v not in anterior:
                anterior[v] = u
                q.append(v)
    return None


def dijkstra(g, origen, destino):
    if origen not in g or destino not in g:
        raise ValueError("Nodo inexistente")
    for aristas in g.values():
        for v, w in aristas:
            if v not in g or not isinstance(w, (int, float)) or w < 0:
                raise ValueError("Arista o peso inválido")
    dist = {v: float("inf") for v in g}
    prev = {}
    dist[origen] = 0
    q = [(0, origen)]
    while q:
        d, u = heappop(q)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                prev[v] = u
                heappush(q, (dist[v], v))
    if dist[destino] == float("inf"):
        return None
    camino = [destino]
    while camino[-1] != origen:
        camino.append(prev[camino[-1]])
    return camino[::-1], dist[destino]


def flujo_maximo(g, s, t):
    """Edmonds-Karp para capacidades enteras no negativas.
    Se acumulan capacidades en la red residual, incluso en aristas recíprocas.
    """
    if s not in g or t not in g or s == t:
        raise ValueError("Origen o destino inválido")
    residual = {u: {} for u in g}
    for u, aristas in g.items():
        for v, cap in aristas.items():
            if v not in g or type(cap) is not int or cap < 0:
                raise ValueError("Capacidad o vértice inválido")
            residual[u][v] = residual[u].get(v, 0) + cap
            residual[v].setdefault(u, 0)
    total = 0
    aumentos = []
    while True:
        padre = {s: None}
        cola = deque([s])
        while cola and t not in padre:
            u = cola.popleft()
            for v, cap in residual[u].items():
                if cap > 0 and v not in padre:
                    padre[v] = u
                    cola.append(v)
        if t not in padre:
            return total, aumentos
        cuello = float("inf")
        ruta = [t]
        v = t
        while v != s:
            u = padre[v]
            cuello = min(cuello, residual[u][v])
            ruta.append(u)
            v = u
        ruta.reverse()
        for u, v in zip(ruta, ruta[1:]):
            residual[u][v] -= cuello
            residual[v][u] = residual[v].get(u, 0) + cuello
        total += cuello
        aumentos.append((ruta, cuello))


def validar_matriz(a):
    n = len(a)
    if any(len(fila) != n for fila in a):
        raise ValueError("Matriz no cuadrada")
    if any(type(z) is not int or z not in (0, 1) for fila in a for z in fila):
        raise ValueError("Matriz binaria requerida")


def verificar_isomorfismo(a, b, p):
    validar_matriz(a)
    validar_matriz(b)
    n = len(a)
    return (len(b) == n and len(p) == n
            and all(type(x) is int for x in p)
            and set(p) == set(range(n))
            and all(a[i][j] == b[p[i]][p[j]]
                    for i in range(n) for j in range(n)))


def buscar_isomorfismo(a, b):
    validar_matriz(a)
    validar_matriz(b)
    if len(a) != len(b):
        return None
    return next((p for p in permutations(range(len(a)))
                 if verificar_isomorfismo(a, b, p)), None)


def validar_factor(n, b):
    if type(n) is not int or type(b) is not int or n < 2 or b < 2:
        raise ValueError("N y B deben ser enteros >= 2")


def verificar_factor(n, b, d):
    validar_factor(n, b)
    return type(d) is int and 2 <= d <= b and n % d == 0


def buscar_factor(n, b):
    validar_factor(n, b)
    return next((d for d in range(2, min(n, b) + 1) if n % d == 0), None)


def validar_modular(p, g, h, b):
    if any(type(x) is not int for x in (p, g, h, b)):
        raise ValueError("Parámetros enteros requeridos")
    if p < 2 or b < 0 or not 0 <= g < p or not 0 <= h < p:
        raise ValueError("Parámetros modulares fuera de rango")
    # p primo es una precondición declarada en el enunciado.


def verificar_exponente(p, g, h, b, x):
    validar_modular(p, g, h, b)
    return type(x) is int and 0 <= x <= b and pow(g, x, p) == h


def buscar_exponente(p, g, h, b):
    validar_modular(p, g, h, b)
    valor = 1 % p
    for x in range(b + 1):
        if valor == h:
            return x
        valor = (valor * g) % p
    return None


def verificar_automorfismo(a, p):
    validar_matriz(a)
    n = len(a)
    return (len(p) == n and all(type(x) is int for x in p)
            and set(p) == set(range(n))
            and any(p[i] != i for i in range(n))
            and all(a[i][j] == a[p[i]][p[j]]
                    for i in range(n) for j in range(n)))


def buscar_automorfismo(a):
    validar_matriz(a)
    return next((p for p in permutations(range(len(a)))
                 if verificar_automorfismo(a, p)), None)


def validar_cnf(clausulas, n):
    if type(n) is not int or n < 0 or not isinstance(clausulas, list):
        raise ValueError("Fórmula inválida")
    for c in clausulas:
        if (not isinstance(c, (list, tuple)) or not 1 <= len(c) <= 3
            or any(type(l) is not int or l == 0 or abs(l) > n for l in c)):
            raise ValueError("Cláusula inválida")


def verificar_sat(clausulas, n, asignacion):
    validar_cnf(clausulas, n)
    if not isinstance(asignacion, dict) or set(asignacion) != set(range(1, n + 1)):
        return False
    if any(type(v) is not bool for v in asignacion.values()):
        return False
    return all(any(asignacion[abs(l)] == (l > 0) for l in c) for c in clausulas)


def dpll(clausulas, n):
    validar_cnf(clausulas, n)
    def resolver(a):
        while True:
            unitaria = None
            for c in clausulas:
                pendiente = []
                satisfecha = False
                for lit in c:
                    v = abs(lit)
                    if v not in a:
                        pendiente.append(lit)
                    elif a[v] == (lit > 0):
                        satisfecha = True
                        break
                if satisfecha:
                    continue
                if not pendiente:
                    return None
                if len(pendiente) == 1:
                    unitaria = pendiente[0]
                    break
            if unitaria is None:
                break
            a[abs(unitaria)] = (unitaria > 0)
        if len(a) == n:
            return a
        v = next(i for i in range(1, n + 1) if i not in a)
        for valor in (True, False):
            b = dict(a)
            b[v] = valor
            salida = resolver(b)
            if salida is not None:
                return salida
        return None
    return resolver({})


def validar_distancias(d, limite):
    if type(limite) not in (int, float) or limite < 0:
        raise ValueError("Límite inválido")
    n = len(d)
    if n < 2 or any(len(f) != n for f in d):
        raise ValueError("Matriz de distancias inválida")
    for fila in d:
        for val in fila:
            if val is not None and (type(val) not in (int, float) or val < 0):
                raise ValueError("Distancia inválida")


def verificar_tsp(d, limite, ruta):
    validar_distancias(d, limite)
    n = len(d)
    if ruta is None or len(ruta) != n + 1:
        return False
    if any(type(v) is not int for v in ruta):
        return False
    if ruta[0] != 0 or ruta[-1] != 0 or set(ruta[:-1]) != set(range(n)):
        return False
    costo = 0
    for u, v in zip(ruta, ruta[1:]):
        if d[u][v] is None:
            return False
        costo += d[u][v]
    return costo <= limite


def buscar_tsp(d, limite):
    validar_distancias(d, limite)
    n = len(d)
    for p in permutations(range(1, n)):
        ruta = (0,) + p + (0,)
        if verificar_tsp(d, limite, ruta):
            return ruta, sum(d[u][v] for u, v in zip(ruta, ruta[1:]))
    return None


def validar_cobertura(g, k):
    if not isinstance(g, dict) or type(k) is not int or k < 0:
        raise ValueError("Grafo o k inválido")
    for u, vecinos in g.items():
        if not isinstance(vecinos, (list, tuple, set)):
            raise ValueError("Lista de vecinos inválida")
        for v in vecinos:
            if v not in g or u == v or u not in g[v]:
                raise ValueError("Grafo no dirigido simple requerido")


def verificar_cobertura(g, k, s):
    validar_cobertura(g, k)
    return (isinstance(s, (set, frozenset)) and len(s) <= k
            and s.issubset(g)
            and all(u in s or v in s for u in g for v in g[u]))


def buscar_cobertura(g, k):
    validar_cobertura(g, k)
    vertices = list(g)
    for tam in range(min(k, len(vertices)) + 1):
        for grupo in combinations(vertices, tam):
            s = set(grupo)
            if verificar_cobertura(g, k, s):
                return s
    return None


if __name__ == "__main__":
    p1 = {"Durán": ["Quito", "Guayaquil"], "Quito": ["Norte"], "Guayaquil": ["Sur"], "Norte": [], "Sur": []}
    p2 = {"Quito": [("Latacunga", 2), ("Ambato", 5)], "Latacunga": [("Guayaquil", 6)], "Ambato": [("Guayaquil", 3)], "Guayaquil": []}
    p3 = {"Planta": {"Quito": 7, "Guayaquil": 5}, "Quito": {"Clientes": 4, "Guayaquil": 2}, "Guayaquil": {"Clientes": 6}, "Clientes": {}}
    a = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    b = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]
    tri = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    d = [[0, 4, 8], [4, 0, 3], [8, 3, 0]]
    g = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
    print("P1", bfs_camino(p1, "Durán", "Norte"))
    print("P2", dijkstra(p2, "Quito", "Guayaquil"))
    print("P3", flujo_maximo(p3, "Planta", "Clientes")[0])
    print("N1", buscar_isomorfismo(a, b))
    print("N2", buscar_factor(91, 10))
    print("N3", buscar_exponente(23, 5, 8, 10))
    print("N4", buscar_automorfismo(tri))
    print("C1", dpll([[1, -2], [2, 3]], 3))
    print("C2", buscar_tsp(d, 20))
    print("C3", buscar_cobertura(g, 1))
