# LOGISTPULSE — planificación y asignación de tres sprints

Equipo:
- **Ariana Muñoz** — GitHub: [@asmunozv](https://github.com/asmunozv)
- **Jeanneth** — GitHub: [@jaan](https://github.com/jaan)

Esta planificación distribuye las tareas de seguimiento y cierre entre las dos integrantes. No se usa para atribuir retrospectivamente código o reuniones que no estén comprobados. La contribución confirmada por el equipo es que **Ariana desarrolló los autómatas**. Las demás asignaciones indican quién queda responsable de revisar, validar, integrar o completar cada entregable.

## Responsabilidades generales

| Integrante | Responsabilidad principal | Responsabilidad de apoyo |
|---|---|---|
| Ariana (@asmunozv) | Autómatas JFLAP; integración técnica; clasificación de los diez casos P/NP/NP-completos | Ejecutar pruebas, consolidar el informe y preparar el release |
| Jeanneth (@jaan) | Revisión del grafo AMR/Dijkstra y de FEFO/reposición; validación de resultados | Revisión cruzada del informe y apoyo en la presentación |

## Sprint 1 — Modelado formal y validación del modelo

**Objetivo:** dejar comprobables los modelos de pedidos, reservas y compras, y validar el grafo de desplazamiento AMR.

| Tarea | Responsable | Apoyo / revisión | Estado |
|---|---|---|---|
| Construcción de los tres autómatas JFLAP (.jff) y definición formal | Ariana | Jeanneth revisa estados, transiciones y secuencias | Autómatas desarrollados por Ariana; revisión cruzada por registrar |
| Comprobación de las secuencias válidas e inválidas y capturas de JFLAP | Ariana | Jeanneth verifica que las salidas coincidan con la documentación | Pendiente de registrar evidencia de revisión |
| Validación de nodos, aristas, pesos y ruta AMR de Dijkstra | Jeanneth | Ariana atiende observaciones e integra correcciones | Pendiente de revisión documentada |

**Criterio de cierre:** tres modelos consistentes, secuencias válidas e inválidas verificadas, ruta AMR comprobada y observaciones de revisión registradas.

## Sprint 2 — Algoritmos logísticos y pruebas

**Objetivo:** comprobar la lógica de rutas, selección FEFO y reposición, incluyendo los casos límite.

| Tarea | Responsable | Apoyo / revisión | Estado |
|---|---|---|---|
| Revisión de Dijkstra, ruta óptima y complejidad | Jeanneth | Ariana integra correcciones si hacen falta | Pendiente de revisión documentada |
| Revisión de FEFO: vencimiento, desempate por código y stock insuficiente | Jeanneth | Ariana ejecuta pruebas y corrige discrepancias | Código y pruebas existen; revisión cruzada por registrar |
| Revisión de la fórmula de reposición y sus límites | Jeanneth | Ariana verifica resultados y pruebas automatizadas | Código y pruebas existen; revisión cruzada por registrar |
| Ejecución de la suite completa y conservación del resultado | Ariana | Jeanneth comprueba que el resultado sea reproducible | GitHub Actions registra una ejecución exitosa de 44 pruebas; repetir al cerrar cambios |

**Criterio de cierre:** revisión de los tres algoritmos, resultados reproducibles y observaciones/correcciones registradas.

## Sprint 3 — Complejidad, integración y entrega

**Objetivo:** consolidar los diez casos, el informe, la presentación y la versión final del repositorio.

| Tarea | Responsable | Apoyo / revisión | Estado |
|---|---|---|---|
| Consolidación de los diez casos P, NP y NP-completos y sus verificadores | Ariana | Jeanneth revisa la clasificación y los certificados | Documentación y código existentes; revisión por registrar |
| Revisión final del informe, capturas y consistencia entre texto y repositorio | Jeanneth | Ariana aplica correcciones | Pendiente |
| Preparación y comprobación de la presentación de 8–10 minutos | Jeanneth | Ariana revisa contenido técnico | Pendiente |
| Ejecutar pruebas finales, etiquetar y publicar `v1.0.0` | Ariana | Jeanneth da conformidad a la revisión final | Pendiente |

**Criterio de cierre:** informe y presentación revisados, pruebas finales satisfactorias, etiqueta `v1.0.0` y GitHub Release publicado.

## Evidencias de seguimiento

- Las tareas se registran como asignaciones de responsabilidad, no como prueba automática de que ya fueron ejecutadas.
- Las revisiones cruzadas deben quedar registradas con fecha real, persona revisora, alcance, observaciones y resultado en [seguimiento_equipo.md](seguimiento_equipo.md).
- Las retrospectivas de cada sprint se completan con aportes reales de las integrantes y fecha en que se realicen. No se reconstruyen reuniones inexistentes.
- Las tareas se pueden seguir en los issues de GitHub titulados Sprint 1, Sprint 2 y Sprint 3.

## Referencias de implementación

- Autómatas: `jflap/` y `docs/automatas_jflap.md`.
- Grafo AMR: `src/planta_amr.py`, `tests/test_planta_amr.py` y `docs/planta_amr.md`.
- FEFO/reposición: `src/fefo_reposicion.py`, `tests/test_fefo_reposicion.py` y `docs/fefo_reposicion.md`.
- Casos P/NP: `src/correos.py`, `tests/test_correos.py`, `docs/fichas_correos.md` y `docs/tabla_resumen.md`.
- Decidibilidad: `docs/decidibilidad_parada.md`.


## Issues de seguimiento en GitHub

- [Sprint 1 — Modelado formal y validación](https://github.com/asmunozv/TC_Deber2/issues/2) — asignado a Ariana; Jeanneth figura como responsable de revisión.
- [Sprint 2 — Algoritmos logísticos y pruebas](https://github.com/asmunozv/TC_Deber2/issues/3) — Jeanneth es la responsable de revisión indicada en el issue; quedó sin asignación técnica de GitHub porque el repositorio no permite asignar actualmente a `@jaan`.
- [Sprint 3 — Complejidad, integración y release final](https://github.com/asmunozv/TC_Deber2/issues/1) — asignado a Ariana; Jeanneth figura como revisora.

**Nota de permisos:** GitHub rechazó asignar issues a `@jaan` porque ese usuario no aparece como asignable en este repositorio. Para que Jeanneth pueda recibir asignaciones formales desde GitHub, la propietaria del repositorio debe invitar a `jaan` como colaboradora y ella debe aceptar la invitación. Mientras tanto, su responsabilidad queda descrita en este plan y en los issues, pero no como assignee técnico.
