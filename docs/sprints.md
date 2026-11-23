# Plan de tres sprints semanales — propuesta, no ejecución reportada

El enunciado exige backlog, responsables, revisión, retrospectiva y release. Esta es una **planificación inicial**; no se atribuyen tareas ejecutadas ni responsables individuales sin confirmación del equipo.

| Sprint | Objetivo | Tareas de backlog | Evidencia esperada |
|---|---|---|---|
| 1 | Modelado formal | Autómatas pedidos, reservas y OC; Q, Σ, q0, F, δ; .jff, 2 secuencias válidas y 2 inválidas por autómata; grafo AMR | Diagramas, JFLAP y grafo documentado |
| 2 | Algoritmos logísticos | Dijkstra o BFS AMR, FEFO por fecha y código, reposición con posición de inventario; análisis Big-O y pruebas | Código, pseudocódigo, salidas reproducibles |
| 3 | Complejidad e integración | Diez correos, tabla resumen, certificado/verificador, nota parada, revisión, PDF, presentación, release | Informe y presentación; tag final |

## Roles a asignar por el equipo
- Coordinación, backlog y revisión de sprint.
- Formalización de autómatas y grafo.
- Algoritmos, pseudocódigo y complejidades.
- Implementación, pruebas e integración.

## Checklist final
- [ ] Registrar integrantes y responsables reales.
- [x] Tres modelos JFLAP y tabla formal con 4 secuencias por autómata; validador automatizado incluido.
- [ ] Capturas de las 12 ejecuciones en JFLAP y evidencia de revisión.
- [x] Grafo ponderado de la Figura 5, ruta AMR, reconstrucción Dijkstra y pruebas locales.
- [x] FEFO, reposición, pseudocódigo, reglas de validación y pruebas escritas.
- [ ] Ejecutar y conservar evidencia observada de las pruebas FEFO/reposición en el entorno del equipo.
- [x] Análisis escrito de 10 casos y tabla.
- [x] Código de referencia y pruebas automatizadas de los casos.
- [x] Nota sobre decidibilidad y parada.
- [ ] Ejecutar y guardar salidas observadas del equipo.
- [ ] Revisiones, retrospectivas y commits de los 3 sprints.
- [ ] PDF y presentación (8–10 min).
- [ ] Publicar release final luego de validación.

**No marcar como completado** un sprint o release hasta tener evidencias reales de trabajo y revisión.
