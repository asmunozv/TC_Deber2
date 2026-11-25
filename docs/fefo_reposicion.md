# Fase C · Selección FEFO y reposición (LOGISTPULSE)

**Fuente:** Deber 2 USFQ, `Deber2_Teoria_Computacion_LOGISTPULSE_USFQ.docx`, página 5, «Fase C · Selección FEFO y regla de reposición». Las fórmulas y reglas de prioridad se mantienen como constan en el documento; las políticas operativas adicionales aparecen claramente señaladas.

## 1. Selección FEFO

**Objetivo:** elaborar un plan de reserva que consuma primero los lotes elegibles que vencen antes (*First Expired, First Out*).

**Entrada:** colección de `L` lotes (`codigo`, `vencimiento`, `disponible`), fecha de referencia y cantidad pedida.

**Salida:** `estado`, `plan` de lotes/cantidades, `pendiente` y `reserva_confirmada`.

**Reglas exigidas por el enunciado:**
1. Excluir lotes vencidos y lotes con disponible = 0.
2. Ordenar por (fecha_vencimiento ascendente, código_lote ascendente).
3. Recorrer por ese orden y tomar `min(cantidad_pendiente, disponible)`.
4. Informar stock insuficiente y plan parcial si no alcanza.

**Política adicional elegida por el equipo (el enunciado pide explicitar una):** **rechazar la reserva completa** si el stock es insuficiente, aunque se devuelva un plan parcial *informativo*. No se disminuye stock ni se comprometen unidades durante el cálculo. La confirmación real de una reserva completa deberá realizarse en una transacción atómica, verificando nuevamente disponibilidades para evitar carreras concurrentes.

**Supuesto del ejemplo:** un lote con `vencimiento == hoy` sigue siendo utilizable durante esa fecha; se excluyen lotes con fecha **anterior**. En operación real, la regla debe adecuarse a restricciones sanitarias y horarios de caducidad.

### Pseudocódigo

```text
FEFO(lotes, cantidad_pedida, hoy)
    validar fecha, cantidad, códigos únicos, cantidades no negativas
    candidatos = []
    para cada lote:
        si lote.fecha_vencimiento >= hoy Y lote.disponible > 0:
            agregar lote a candidatos
    ordenar candidatos por (fecha_vencimiento, código_lote)
    pendiente = cantidad_pedida
    plan = []
    para cada lote en candidatos:
        si pendiente = 0: salir
        tomar = min(pendiente, lote.disponible)
        agregar (lote.codigo, tomar) al plan
        pendiente = pendiente - tomar
    si pendiente = 0:
        devolver OK, plan, pendiente=0, reserva_confirmada=verdadero
    si no:
        devolver STOCK_INSUFICIENTE, plan_informativo, pendiente,
                 reserva_confirmada=falso
```

### Ejemplo reproducible

Fecha de referencia: **2026-11-23**, demanda: **12**.

| Lote | Vence | Disponible | Elegible |
|---|---|---:|---|
| L003 | 2026-12-10 | 8 | Sí |
| L002 | 2026-11-25 | 5 | Sí |
| L001 | 2026-11-25 | 4 | Sí |
| L000 | 2026-11-22 | 30 | No: vencido |

Salida: `L001:4`, `L002:5`, `L003:3`; pendiente **0**, `OK`. El empate de vencimiento L001/L002 se resuelve por código. Si la demanda fuera 25, solo habría 17 disponibles, el plan sería informativo, el faltante 8 y **no** se confirmaría reserva.

### Complejidad, terminación y exactitud

- `L` = número de lotes.
- **Tiempo:** O(L log L) en peor caso (filtrar O(L), ordenar O(L log L), recorrer O(L)).
- **Espacio auxiliar:** O(L) para los candidatos y el plan. No incluye lotes de entrada.
- **Terminación:** recorridos acotados por el número finito de lotes; ordenación finita.
- **Exactitud:** selecciona respetando prioridad de vencimiento/código, sin heurísticas.

## 2. Reposición: punto de pedido

**Regla literal del enunciado** por producto/SKU:

```text
posición = disponible_en_bodega + cantidad_en_órdenes_abiertas − cantidad_reservada
si posición <= mínimo:
    sugerencia = max(0, objetivo − posición)
si no:
    sugerencia = 0
```

**Entrada:** `P` productos con `sku`, `disponible`, `en_orden`, `reservado`, `minimo`, `objetivo`.

**Salida:** por SKU, posición y cantidad a sugerir; opcionalmente copia del catálogo tras registrar nuevas órdenes.

### Pseudocódigo

```text
SUGERIR_REPOSICION(productos)
    validar SKU único, cantidades enteras no negativas,
            objetivo >= mínimo, reservado <= disponible
    resultado = []
    para cada SKU:
        posicion = disponible + en_orden - reservado
        si posicion <= minimo:
            sugerencia = max(0, objetivo - posicion)
        si no:
            sugerencia = 0
        agregar (SKU, posicion, sugerencia) a resultado
    devolver resultado

REGISTRAR_SUGERENCIAS(productos)
    calcular sugerencias desde el estado actualizado
    para cada sugerencia positiva:
        agregar cantidad a la cantidad en órdenes abiertas
        registrar orden nueva
    devolver copia actualizada y órdenes generadas
```

### Ejemplo exacto del documento

| Disponible | En orden | Reservado | Mínimo | Objetivo | Posición | Sugerencia |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 10 | 5 | 30 | 50 | **23** | **27** |

**No duplicación:** `sugerir_reposicion` es una función pura; consultar dos veces no crea ninguna orden. `registrar_sugerencias` devuelve un **nuevo snapshot** y registra las 27 unidades en `en_orden` (pasa de 10 a 37). La siguiente evaluación obtiene posición **50**, superior al mínimo, y devuelve sugerencia **0**. **En producción** se necesita transacción por SKU, bloqueo o clave idempotente para impedir dos órdenes simultáneas a partir de un estado anterior; este ejemplo en memoria **no** garantiza seguridad entre procesos concurrentes.

### Complejidad, terminación y exactitud

- `P` = número de productos.
- **Tiempo:** O(P) para sugerir y para registrar en memoria, asumiendo operaciones aritméticas y de diccionario de costo constante.
- **Espacio:** O(1) adicional por SKU procesado; O(P) si se devuelve la lista de sugerencias o un snapshot de salida, como hace esta implementación.
- **Terminación:** se itera una vez sobre una colección finita de P productos.
- **Exactitud:** se aplica literalmente la fórmula del enunciado sin heurísticas.

## 3. Validación, política de datos y reproducibilidad

**Implementación:** `src/fefo_reposicion.py`. **Pruebas:** `tests/test_fefo_reposicion.py`. No requiere paquetes externos.

```bash
python3 -m src.fefo_reposicion
python3 -m unittest discover -s tests -v
```

**Resultados esperados de la demostración (código de ejemplo):**
```text
FEFO: {'estado': 'OK', 'solicitado': 12, 'pendiente': 0, 'plan': [{'codigo': 'L001', 'cantidad': 4}, {'codigo': 'L002', 'cantidad': 5}, {'codigo': 'L003', 'cantidad': 3}], 'reserva_confirmada': True}
Reposición: [{'sku': 'SKU-001', 'posicion': 23, 'sugerencia': 27}]
Órdenes generadas: [{'sku': 'SKU-001', 'cantidad': 27}]
Segunda evaluación (sin duplicados): []
```

**Cobertura de pruebas:** FEFO: normal con desempate, vencido, disponible 0, insuficiente, demanda 0, vencimiento hoy, sin mutaciones, fecha inválida, lote duplicado, demanda negativa. Reposición: ejemplo del enunciado, inventario superior al mínimo, posición igual al mínimo, órdenes abiertas, registro idempotente secuencial, lista vacía, varios SKU, duplicados y datos inválidos.

**Evidencia observada:** GitHub Actions ejecutó `python -m unittest discover -s tests -v` en el commit `42a82346135e79b2220e2161efce607f2b3109bb` y reportó **44 tests, OK**; incluye las 20 pruebas nuevas de Fase C y los tests de fases anteriores. Registro: https://github.com/asmunozv/TC_Deber2/actions/runs/45272516718 . Las salidas impresas en el bloque anterior son las previstas por los datos de ejemplo y no se incluyeron como captura de la ejecución del comando demostrativo. Los datos inventados L001/L002/L003 se utilizan solo para demostración; la fórmula 18+10−5 y sugerencia 27 sí procede literalmente del enunciado.

## 4. Cumplimiento de la rúbrica

Se desarrolla pseudocódigo para FEFO y reposición, restricciones operativas, elección de política ante falta de stock, prevención de duplicación, condiciones de terminación, Big-O temporal y espacial y código ejecutable con pruebas de casos normales, límite e inválidos. Corresponde al criterio «FEFO y reposición» de **1,5 puntos**, sujeto a evaluación del docente.
