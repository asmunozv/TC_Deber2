# Seguimiento del equipo — LOGISTPULSE

Este documento reúne el seguimiento de revisiones y las retrospectivas de los tres sprints. **Las retrospectivas están redactadas y aprobadas por Ariana y Jeanneth.**

Integrantes:
- Ariana Muñoz — @asmunozv
- Jeanneth — @jann1111

## 1. Tabla principal de avance

| Sprint | Retrospectiva | Estado | Fecha |
|---|---|---|---|
| Sprint 1 — Modelado formal | Retrospectiva completa | **Aprobada por ambas integrantes** | 22/11/2026 |
| Sprint 2 — Algoritmos logísticos | Retrospectiva completa | **Aprobada por ambas integrantes** | 23/11/2026 |
| Sprint 3 — Complejidad e integración | Retrospectiva completa | **Aprobada por ambas integrantes** | 24/11/2026  |

## 2. Registro de revisiones cruzadas

| Fecha | Persona revisora | Trabajo revisado | Observación / comprobación | Corrección acordada | Estado |
|---|---|---|---|---|---|
| 23/11/2026  | Jeanneth | Autómatas JFLAP de Ariana | Revisión de estados, transiciones y secuencias | Ajustes según las observaciones de revisión | Registro de revisión |
| 23/11/2026  | Ariana | Grafo AMR y Dijkstra | Revisión de nodos, aristas, pesos y ruta | Ajustes según las observaciones de revisión | Registro de revisión |
| 23/11/2026  | Jeanneth | FEFO y reposición | Revisión de reglas, límites y resultados | Ajustes según las observaciones de revisión | Registro de revisión |
| 24/11/2026  | Ariana | Informe y clasificación P/NP | Revisión de consistencia y justificaciones | Ajustes según las observaciones de revisión | Registro de revisión |

## 3. Retrospectiva del Sprint 1 — Modelado formal

**Estado:** Aprobada por Ariana y Jeanneth.

- **Fecha de retrospectiva:** 22/11/2026 
- **Participantes:** Ariana Muñoz y Jeanneth.
- **Qué salió bien:** La separación del proceso logístico en autómatas de pedidos, reservas y compras ayudó a representar cada flujo por partes. También fue útil definir secuencias aceptadas y rechazadas para comprobar el comportamiento de los modelos.
- **Qué dificultades hubo:** La parte más delicada fue decidir qué estados y transiciones correspondían a cada evento y evitar aceptar secuencias que no respetaran el orden del proceso. También fue necesario revisar la representación en JFLAP y la correspondencia entre el grafo de planta y sus pesos.
- **Qué mejorar:** Para facilitar el trabajo, conviene acordar desde el inicio los símbolos, estados, transiciones y casos de prueba. También es importante realizar revisiones cruzadas de los modelos y registrar las correcciones en la documentación.
- **Acuerdos del equipo:** Se acordó utilizar una lista de casos normales e inválidos para comprobar cada entregable antes de integrarlo y mantener la documentación sincronizada con los modelos.

## 4. Retrospectiva del Sprint 2 — Algoritmos logísticos

**Estado:** Aprobada por Ariana y Jeanneth.

- **Fecha de retrospectiva:** 23/11/2026 
- **Participantes:** Ariana Muñoz y Jeanneth.
- **Qué salió bien:** Trabajar Dijkstra, FEFO y reposición como componentes separados facilitó entender qué resultado debía producir cada algoritmo. Las pruebas ayudaron a comprobar la ruta de menor costo, el orden de selección por vencimiento y el cálculo de la posición de inventario.
- **Qué dificultades hubo:** Fue importante prestar atención a los casos límite: lotes vencidos o sin stock, fechas iguales, stock insuficiente y posiciones de inventario exactamente en el mínimo. También se debía distinguir entre sugerir una reposición y modificar realmente el inventario.
- **Qué mejorar:** Es conveniente probar explícitamente los límites y documentar junto a cada algoritmo su entrada, salida y complejidad. También se debe mantener la consistencia entre el código, las pruebas y la explicación del informe.
- **Acuerdos del equipo:** Se acordó ejecutar la suite completa después de los cambios importantes y registrar los resultados para facilitar la detección y corrección de errores.

## 5. Retrospectiva del Sprint 3 — Complejidad, integración y entrega

**Estado:** Aprobada por Ariana y Jeanneth.

- **Fecha de retrospectiva:** 24/11/2026 
- **Participantes:** Ariana Muñoz y Jeanneth.
- **Qué salió bien:** Organizar los diez problemas por categorías P, NP y NP-completo permitió estructurar el análisis teórico. La integración de los algoritmos, pruebas y documentación en el repositorio facilitó revisar el proyecto como un solo entregable.
- **Qué dificultades hubo:** La justificación de cada clasificación requirió cuidado, especialmente para diferenciar un problema que está en NP de uno que además es NP-completo. También fue necesario mantener consistentes el código, los resultados de las pruebas, el informe y la presentación.
- **Qué mejorar:** En futuros trabajos es importante distribuir las revisiones con anticipación, reservar tiempo específico para corregir el informe y comprobar los archivos de entrega antes de publicar la versión final. Una lista de verificación compartida desde el inicio facilita este proceso.
- **Acuerdos del equipo:** Se acordó comprobar la actualización del PDF y la presentación, ejecutar las pruebas finales y verificar que las evidencias estén incorporadas antes de cerrar una entrega.

## 6. Lista de control del release final

- [ ] Informe PDF final revisado.
- [ ] Presentación final revisada.
- [ ] Capturas JFLAP incorporadas y legibles.
- [ ] Suite completa ejecutada después de los últimos cambios.
- [ ] Revisiones cruzadas registradas.
- [x] Retrospectivas de los tres sprints redactadas y aprobadas por Ariana y Jeanneth.
- [ ] Fechas de las tres retrospectivas incorporadas.
- [ ] Etiqueta Git `v1.0.0` creada.
- [ ] GitHub Release `LOGISTPULSE v1.0.0` publicado.
