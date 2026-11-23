# LOGISTPULSE — Deber 2 de Teoría de la Computación

Universidad San Francisco de Quito · Teoría de la Computación.

Este repositorio documenta la **Fase D: diez correos de P, NP y NP-completitud** con código Python y pruebas, y registra los demás entregables requeridos por el enunciado.

## Estado real del trabajo
- ✅ Diez fichas y tabla resumen: `docs/fichas_correos.md` y `docs/tabla_resumen.md`.
- ✅ Algoritmos y verificadores: `src/correos.py`.
- ✅ Pruebas automatizadas: `tests/test_correos.py`.
- ✅ Nota teórica sobre la parada: `docs/decidibilidad_parada.md`.
- ✅ Backlog de tres sprints **propuesto**, no retrospectiva de sprints ya ejecutados: `docs/sprints.md`.
- ✅ Tres modelos JFLAP (.jff), sus diagramas Mermaid, definiciones formales y 12 secuencias documentadas: `docs/automatas_jflap.md`.
- ⏳ Capturas de las doce ejecuciones en la aplicación JFLAP: **pendiente de obtener manualmente**.
- ⏳ Grafo de planta AMR, rutas; pseudocódigo y pruebas FEFO/reposición: **pendiente**.
- ⏳ Informe PDF consolidado, presentación y release final: **pendiente**.

## Ejecución
Requiere Python 3.10+; no hay dependencias externas.

```bash
python -m unittest discover -s tests -v
python -m src.correos
```

Los casos del simulador son *instancias de demostración*. Las afirmaciones de complejidad se refieren a problemas generales, no a que las instancias pequeñas sean difíciles. En el correo C1, el ejemplo tiene cláusulas de **2-CNF** (resoluble en P), mientras que la NP-completitud corresponde a **3-SAT general**. Todos los problemas analizados son decidibles.

## Organización
- `docs/fichas_correos.md`: diez fichas formales y reducciones de C1, C2, C3.
- `docs/tabla_resumen.md`: comparación de clase, tiempo/espacio, decidibilidad y estrategia.
- `src/correos.py`: diez solucionadores y verificadores separados.
- `tests/test_correos.py`: pruebas normales, negativas, límite e inválidas.
- `docs/sprints.md`: backlog y planificación.
- `docs/decidibilidad_parada.md`: distinción entre decidibilidad, computabilidad y eficiencia.

Para reproducibilidad, los resultados impresos por `python -m src.correos` son los datos de ejemplo. No se ha completado todavía la fase de simulación JFLAP.

## Referencias
Enunciado USFQ «Deber 2 Teoría de la Computación — LOGISTPULSE» y simulador educativo local «LOGISTPULSE · Laboratorio P, NP y NP-completo».
## Fase A · JFLAP

Abrir `jflap/pedido.jff`, `jflap/reserva.jff` o `jflap/compra.jff` en JFLAP 7.x. Las entradas son símbolos de una sola letra: consulta `docs/automatas_jflap.md` para su significado y las **12 secuencias**. El conjunto de tests `tests/test_automatas.py` valida los XML y las secuencias con Python, pero la evidencia visual de **Input → Multiple Run** en JFLAP se debe añadir después.
