# Gestión del proyecto y tres sprints

## Criterio de evidencia

El historial disponible contiene ocho commits, todos del 23 de noviembre de 2026 y atribuidos por Git a **Ariana Simone Muñoz Villamar**. Ese dato demuestra autoría técnica de los commits, pero no demuestra por sí solo quién diseñó, revisó o discutió cada parte. No existen actas, pull requests, issues, revisiones aprobadas ni retrospectivas versionadas. Los campos que requieren memoria del equipo quedan pendientes de confirmación y no se inventan.

## Backlog consolidado

| Prioridad | Elemento | Sprint | Criterio de terminado | Estado comprobable |
|---:|---|---:|---|---|
| 1 | Tres AFD y pruebas JFLAP | 1 | Estados completos, XML válido, cadenas y capturas reales | Modelos y tests listos; capturas pendientes |
| 2 | Grafo de planta y Dijkstra | 1-2 | Ruta mínima, bloqueos, complejidad y pruebas | Listo |
| 3 | FEFO y reposición | 2 | Política, fórmula, validaciones y pruebas | Listo |
| 4 | Diez correos y tabla | 3 | Clasificación, verificadores, reducciones y casos | Listo |
| 5 | Decidibilidad y parada | 3 | Explicación conceptual y ejemplo logístico | Listo |
| 6 | Integración y evidencia | 3 | Suite actual, informe, presentación y auditoría | En finalización |
| 7 | Release | 3 | Revisión humana, tag y publicación autorizada | Pendiente |

## Sprint 1: autómatas y grafo

**Objetivo:** modelar los procesos finitos y la topología de planta.

**Evidencia del repositorio:**

- `e98f3b2`: añadió los tres `.jff`, formalización y pruebas iniciales.
- `d18bc7e`: añadió grafo, datos de aristas, Dijkstra y 12 pruebas.
- La rama `finalizacion-deber2` completa `Expirada`, `En aprobación`, `Recepción parcial` y la cancelación desde `Reservado`.

**Resultado comprobable:** los siete u ocho estados requeridos de cada proceso son alcanzables; los archivos son XML compatibles con el esquema básico de JFLAP; la planta tiene siete vértices, once aristas y costo mínimo 11 m.

**Responsable demostrable:** Ariana Muñoz figura como autora Git de los commits iniciales. Responsable de la revisión/finalización: **pendiente de confirmación del equipo**.

**Revisión y retrospectiva:** no hay acta. Pendiente registrar quién revisó los modelos en JFLAP y qué cambio acordó el equipo.

## Sprint 2: Dijkstra, FEFO y reposición

**Objetivo:** implementar los algoritmos logísticos y probar casos normales, límite e inválidos.

**Evidencia del repositorio:**

- `0a72e59`: corrigió la revalidación innecesaria del TSP.
- `74290d1`: incorporó integración continua.
- `42a8234`: añadió FEFO, reposición y sus pruebas.
- `61ef27a`: registró una ejecución histórica de 44 pruebas en GitHub Actions.

**Resultado comprobable:** Dijkstra usa `heapq` y predecesores; FEFO ordena por fecha y código; reposición produce posición 23 y sugerencia 27 en el ejemplo; una segunda evaluación del snapshot actualizado no duplica la orden.

**Responsable demostrable:** Ariana Muñoz figura como autora Git. Colaboradores o revisores: **pendiente de confirmación**.

**Revisión y retrospectiva:** el commit de TSP evidencia una corrección técnica. No existe documentación que permita atribuir una reunión o retrospectiva; queda pendiente añadirla si realmente ocurrió.

## Sprint 3: correos, integración, informe y presentación

**Objetivo:** consolidar teoría de complejidad, documentación, pruebas y entregables de comunicación.

**Evidencia del repositorio:**

- `8895a3c`: añadió los diez casos, solucionadores, verificadores, pruebas, tabla y nota de decidibilidad.
- La rama `finalizacion-deber2` incorpora auditoría, ampliación de AFD, evidencia local, fuente LaTeX, PDF y presentación.

**Resultado comprobable:** las diez fichas distinguen búsqueda y verificación; C1, C2 y C3 incluyen reducción orientada hacia el problema estudiado; P está contenido en NP; los diez problemas son decidibles. La ejecución final y sus cifras se conservan en `docs/evidencias/resultados_tests.txt`.

**Responsables:** Ariana Muñoz es autora Git de la base. La distribución real de informe, presentación, exposición y revisión entre Ariana Muñoz y Jeanneth Cabascango queda **pendiente de confirmación**.

**Revisión y retrospectiva:** pendientes de confirmación: fecha, asistentes, hallazgos y decisiones. No debe completarse retroactivamente con datos inventados.

## Cierre y versión

- Rama preparada: `finalizacion-deber2`.
- Versión propuesta: `v1.0.0`.
- Tags existentes al iniciar la auditoría: ninguno.
- Condiciones antes del release: incorporar capturas reales de JFLAP, confirmar responsables/revisiones, ejecutar la suite en la máquina del equipo, revisar PDF/presentación y obtener autorización de publicación.
- No se crea tag, release, push ni merge desde esta finalización automática.
