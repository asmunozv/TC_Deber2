# Gestión del proyecto y tres sprints

## Equipo y criterio de evidencia

- **Ariana Muñoz** — [@asmunozv](https://github.com/asmunozv).
- **Jeanneth Cabascango** — [@jann1111](https://github.com/jann1111).

El historial atribuye a Ariana los ocho commits técnicos iniciales. Los commits posteriores de `main` registran la planificación, los issues y retrospectivas aprobadas por el equipo en [seguimiento_equipo.md](seguimiento_equipo.md). La contribución confirmada en esos registros indica que Ariana desarrolló los autómatas; las demás asignaciones expresan responsabilidad de revisión o cierre y no se usan para atribuir código retrospectivamente.

## Responsabilidades acordadas

| Integrante | Responsabilidad principal | Apoyo |
|---|---|---|
| Ariana | Autómatas JFLAP, integración técnica y clasificación de los diez casos | Pruebas, informe y preparación del release |
| Jeanneth | Revisión de grafo/Dijkstra, FEFO/reposición y resultados | Revisión del informe y presentación |

## Backlog consolidado

| Prioridad | Elemento | Sprint | Criterio de terminado | Estado comprobable |
|---:|---|---:|---|---|
| 1 | Tres AFD y pruebas JFLAP | 1 | Estados completos, XML válido, cadenas y capturas reales | Modelos y tests listos; capturas pendientes |
| 2 | Grafo de planta y Dijkstra | 1-2 | Ruta mínima, bloqueos, complejidad y pruebas | Listo |
| 3 | FEFO y reposición | 2 | Política, fórmula, validaciones y pruebas | Listo |
| 4 | Diez correos y tabla | 3 | Clasificación, verificadores, reducciones y casos | Listo |
| 5 | Decidibilidad y parada | 3 | Explicación y ejemplo logístico | Listo |
| 6 | Integración y evidencia | 3 | Suite actual, informe, presentación y auditoría | En finalización |
| 7 | Release | 3 | Revisión humana, tag y publicación autorizada | Pendiente |

## Sprint 1: autómatas y grafo

**Objetivo:** modelar los procesos finitos y la topología de planta.

- `e98f3b2`: añadió los tres `.jff`, formalización y pruebas iniciales.
- `d18bc7e`: añadió grafo, datos de aristas, Dijkstra y 12 pruebas.
- La rama `finalizacion-deber2` completa `Expirada`, `En aprobación`, `Recepción parcial` y la cancelación desde `Reservado`.
- Resultado: los estados requeridos son alcanzables; la planta tiene siete vértices, once aristas y costo mínimo 11 m.
- Revisión acordada: Jeanneth revisa modelos y resultados; el detalle fechado se conserva en `seguimiento_equipo.md`.

**Observación de cierre:** las pruebas automatizadas están completas. Las seis capturas reales de JFLAP todavía no están en el repositorio y no se declaran incorporadas.

## Sprint 2: Dijkstra, FEFO y reposición

**Objetivo:** implementar los algoritmos logísticos y probar casos normales, límite e inválidos.

- `0a72e59`: corrigió la revalidación innecesaria del TSP.
- `74290d1`: incorporó integración continua.
- `42a8234`: añadió FEFO, reposición y sus pruebas.
- `61ef27a`: registró una ejecución histórica de 44 pruebas.
- Resultado: Dijkstra usa cola de prioridad y predecesores; FEFO ordena por fecha y código; reposición obtiene posición 23 y sugerencia 27 sin duplicación secuencial.

La cifra actual se toma de `docs/evidencias/resultados_tests.txt`, no del resultado histórico.

## Sprint 3: correos, integración, informe y presentación

**Objetivo:** consolidar teoría, documentación, pruebas y entregables de comunicación.

- `8895a3c`: añadió los diez casos, solucionadores, verificadores, pruebas, tabla y nota de decidibilidad.
- Los commits `bf3f5a4` a `899db2a` incorporaron responsables, issues y retrospectivas en `main`.
- La rama `finalizacion-deber2` incorpora auditoría, AFD ampliados, evidencia local, fuente LaTeX, PDF y presentación.
- Resultado: las fichas distinguen búsqueda y verificación; C1, C2 y C3 incluyen reducciones; P está contenido en NP; los diez problemas son decidibles.

## Issues de seguimiento

- [Sprint 1](https://github.com/asmunozv/TC_Deber2/issues/2): asignado a Ariana; Jeanneth figura como revisora.
- [Sprint 2](https://github.com/asmunozv/TC_Deber2/issues/3): Jeanneth es responsable de revisión, pero GitHub no permitió asignarla técnicamente.
- [Sprint 3](https://github.com/asmunozv/TC_Deber2/issues/1): asignado a Ariana; Jeanneth figura como revisora.

GitHub rechazó asignaciones y pushes desde la cuenta autenticada de Jeanneth porque no tiene permisos de escritura en el repositorio de Ariana. Ariana debe invitar a `@jann1111` como colaboradora y Jeanneth debe aceptar la invitación para aprobar, fusionar o asignar desde esa cuenta.

## Cierre y versión

- Rama preparada: `finalizacion-deber2`.
- Versión propuesta: `v1.0.0`.
- Tags existentes al iniciar la auditoría: ninguno.
- Condiciones: incorporar capturas reales de JFLAP, ejecutar suite final, revisar PDF/presentación y obtener autorización de publicación.
- Un release no se considera terminado mientras falten esas condiciones.
