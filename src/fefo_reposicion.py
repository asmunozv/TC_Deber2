"""LOGISTPULSE — Fase C: FEFO y reposición según enunciado USFQ.

Políticas de implementación:
- FEFO: fecha >= hoy significa lote aún elegible durante su día de vencimiento.
- Si el stock no alcanza, se devuelve plan PARCIAL INFORMATIVO, no reserva confirmada.
- Ninguna función FEFO modifica cantidades en el origen.
- La sugerencia de compra no crea órdenes; registrar_sugerencias contabiliza
  cada orden nueva en 'en_orden' para impedir duplicarla en llamadas sucesivas.
"""
from datetime import date


def _entero_no_negativo(valor, campo):
    if type(valor) is not int or valor < 0:
        raise ValueError(f"{campo} debe ser un entero no negativo")


def _fecha(valor, campo):
    if isinstance(valor, date) and not isinstance(valor, __import__('datetime').datetime):
        return valor
    if type(valor) is str:
        try:
            return date.fromisoformat(valor)
        except ValueError:
            pass
    raise ValueError(f"{campo} debe ser fecha ISO YYYY-MM-DD o date")


def seleccionar_fefo(lotes, cantidad_pedida, hoy):
    """Devuelve resultado y plan; no muta lotes ni realiza reserva parcial.

    Lotes: [{'codigo':str,'vencimiento':'YYYY-MM-DD','disponible':int},...]
    Devuelve estado, plan=[{'codigo','cantidad'}], pendiente, solicitado.
    """
    _entero_no_negativo(cantidad_pedida, "cantidad_pedida")
    hoy_fecha = _fecha(hoy, "hoy")
    if not isinstance(lotes, (list, tuple)):
        raise ValueError("lotes debe ser una lista o tupla")

    vistos = set()
    candidatos = []
    for lote in lotes:
        if not isinstance(lote, dict):
            raise ValueError("Cada lote debe ser un diccionario")
        if not {'codigo', 'vencimiento', 'disponible'}.issubset(lote):
            raise ValueError("Lote incompleto")
        codigo = lote['codigo']
        if type(codigo) is not str or not codigo.strip():
            raise ValueError("Código de lote inválido")
        if codigo in vistos:
            raise ValueError("Código de lote duplicado")
        vistos.add(codigo)
        vencimiento = _fecha(lote['vencimiento'], "vencimiento")
        disponible = lote['disponible']
        _entero_no_negativo(disponible, "disponible")
        if vencimiento >= hoy_fecha and disponible > 0:
            candidatos.append((vencimiento, codigo, disponible))

    candidatos.sort(key=lambda item: (item[0], item[1]))
    pendiente = cantidad_pedida
    plan = []
    for _, codigo, disponible in candidatos:
        if pendiente == 0:
            break
        tomar = min(pendiente, disponible)
        plan.append({'codigo': codigo, 'cantidad': tomar})
        pendiente -= tomar

    return {
        'estado': 'OK' if pendiente == 0 else 'STOCK_INSUFICIENTE',
        'solicitado': cantidad_pedida,
        'pendiente': pendiente,
        'plan': plan,
        'reserva_confirmada': pendiente == 0,
    }


def sugerir_reposicion(productos):
    """Recomendación por SKU (sin efectos secundarios); O(P) tiempo.
    Producto: sku, disponible, en_orden, reservado, minimo, objetivo.
    """
    if not isinstance(productos, (list, tuple)):
        raise ValueError("productos debe ser lista o tupla")
    vistos = set()
    sugerencias = []
    for producto in productos:
        if not isinstance(producto, dict) or not {
            'sku', 'disponible', 'en_orden', 'reservado', 'minimo', 'objetivo'
        }.issubset(producto):
            raise ValueError("Producto incompleto")
        sku = producto['sku']
        if type(sku) is not str or not sku.strip() or sku in vistos:
            raise ValueError("SKU inválido o duplicado")
        vistos.add(sku)
        for campo in ('disponible', 'en_orden', 'reservado', 'minimo', 'objetivo'):
            _entero_no_negativo(producto[campo], campo)
        if producto['objetivo'] < producto['minimo']:
            raise ValueError("objetivo debe ser mayor o igual que mínimo")
        if producto['reservado'] > producto['disponible']:
            raise ValueError("reservado supera disponible del inventario físico")

        posicion = producto['disponible'] + producto['en_orden'] - producto['reservado']
        cantidad = max(0, producto['objetivo'] - posicion) if posicion <= producto['minimo'] else 0
        sugerencias.append({'sku': sku, 'posicion': posicion, 'sugerencia': cantidad})
    return sugerencias


def registrar_sugerencias(productos):
    """Simula en memoria el alta de órdenes abiertas una sola vez.

    Recibe snapshot sin mutarlo; devuelve snapshot actualizado y órdenes nuevas.
    En producción debe ejecutarse con transacción/bloqueo por SKU, pues dos
    procesos concurrentes con un snapshot desactualizado podrían duplicar OC.
    """
    sugerencias = sugerir_reposicion(productos)
    por_sku = {fila['sku']: fila for fila in sugerencias}
    actualizado = []
    nuevas_ordenes = []
    for producto in productos:
        copia = dict(producto)
        cant = por_sku[producto['sku']]['sugerencia']
        if cant > 0:
            copia['en_orden'] += cant
            nuevas_ordenes.append({'sku': producto['sku'], 'cantidad': cant})
        actualizado.append(copia)
    return actualizado, nuevas_ordenes


if __name__ == '__main__':
    lotes = [
        {'codigo':'L003', 'vencimiento':'2026-12-10', 'disponible':8},
        {'codigo':'L002', 'vencimiento':'2026-11-25', 'disponible':5},
        {'codigo':'L001', 'vencimiento':'2026-11-25', 'disponible':4},
        {'codigo':'L000', 'vencimiento':'2026-11-22', 'disponible':30},
    ]
    print('FEFO:', seleccionar_fefo(lotes, 12, '2026-11-23'))
    productos = [{'sku':'SKU-001', 'disponible':18, 'en_orden':10,
                 'reservado':5, 'minimo':30, 'objetivo':50}]
    print('Reposición:', sugerir_reposicion(productos))
    nuevo, ordenes = registrar_sugerencias(productos)
    print('Órdenes generadas:', ordenes)
    print('Segunda evaluación (sin duplicados):', registrar_sugerencias(nuevo)[1])
