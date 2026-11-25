# LOGISTPULSE - Deber 2 de Teoría de la Computación

Proyecto académico de la Universidad San Francisco de Quito que aplica autómatas finitos, grafos ponderados, políticas de inventario, decidibilidad y complejidad computacional a procesos logísticos.

## Integrantes confirmadas

- Ariana Muñoz - [@asmunozv](https://github.com/asmunozv)
- Jeanneth Cabascango - [@jann1111](https://github.com/jann1111)

## Objetivos

- Modelar pedidos, reservas y órdenes de compra como AFD compatibles con JFLAP.
- Calcular rutas AMR mínimas mediante Dijkstra.
- Implementar FEFO y la regla de reposición por posición de inventario.
- Analizar diez problemas de P, NP y NP-completitud con algoritmos y verificadores.
- Diferenciar decidibilidad, computabilidad, complejidad y eficiencia práctica.

## Resultados principales

- Los tres AFD incluyen todos los estados requeridos: cancelación desde `Reservado`, reserva `Expirada`, compra `En aprobación` y `Recepción parcial`.
- Dijkstra encuentra costo mínimo **11 m**. Son óptimas `R-B-A-P-E-D` y `R-B-A-E-D`.
- FEFO selecciona `L001:4`, `L002:5`, `L003:3` para la demanda de ejemplo.
- Reposición obtiene posición **23** y sugerencia **27**.
- La ejecución local final reportó **46 pruebas, 46 exitosas, 0 fallos**.

## Estructura

| Ruta | Contenido |
|---|---|
| [`jflap/`](jflap/) | Tres autómatas `.jff` |
| [`src/`](src/) | Dijkstra, FEFO/reposición y diez casos |
| [`tests/`](tests/) | Pruebas unitarias reproducibles |
| [`docs/`](docs/) | Formalización, fichas, sprints, auditoría y evidencias |
| [`informe/`](informe/) | Fuente LaTeX y PDF técnico final |
| [`presentacion/`](presentacion/) | Presentación editable y guion de 9:10 |
| [`scripts/`](scripts/) | Generador reproducible del PDF |

## Requisitos e instalación

- Python 3.9 o superior. No hay dependencias externas para ejecutar código y pruebas.
- Java para JFLAP. El entorno de finalización usó Java 21.
- JFLAP 7.1 para las capturas manuales: [descarga oficial](https://www.jflap.org/jflaptmp/).
- Para regenerar el PDF sin LaTeX: `reportlab`. La fuente editable también está disponible en [`informe/informe_final.tex`](informe/informe_final.tex).

```bash
git clone https://github.com/asmunozv/TC_Deber2.git
cd TC_Deber2
python3 -m unittest discover -s tests -v
```

## Ejecución

```bash
python3 -m src.planta_amr
python3 -m src.fefo_reposicion
python3 -m src.correos
```

La salida observada completa se conserva en [`docs/evidencias/resultados_tests.txt`](docs/evidencias/resultados_tests.txt).

## Autómatas y JFLAP

La definición formal, las transiciones, 23 cadenas de prueba y sus trazas están en [`docs/automatas_jflap.md`](docs/automatas_jflap.md). Los modelos son AFD parciales equivalentes a AFD totales con un estado pozo no final.

```bash
java -jar /ruta/a/JFLAP7.1.jar
```

Después de abrir cada `.jff`, usar `Input > Multiple Run` con las cadenas documentadas. Las seis capturas auténticas deben guardarse en `docs/evidencias/jflap/`. No se incluyeron imágenes simuladas; el protocolo exacto está en [`docs/evidencias/jflap/README.md`](docs/evidencias/jflap/README.md).

## Documentación técnica

- [Autómatas JFLAP](docs/automatas_jflap.md)
- [Grafo de planta y Dijkstra](docs/planta_amr.md)
- [FEFO y reposición](docs/fefo_reposicion.md)
- [Diez fichas](docs/fichas_correos.md) y [tabla comparativa](docs/tabla_resumen.md)
- [Decidibilidad y problema de la parada](docs/decidibilidad_parada.md)
- [Auditoría de requisitos](docs/auditoria_entrega.md)
- [Gestión de sprints](docs/sprints.md) y [seguimiento del equipo](docs/seguimiento_equipo.md)

## Informe y presentación

- PDF final: [`informe/LOGISTPULSE_Informe_Final.pdf`](informe/LOGISTPULSE_Informe_Final.pdf)
- Fuente editable: [`informe/informe_final.tex`](informe/informe_final.tex)
- Presentación editable: [`presentacion/LOGISTPULSE_Presentacion_Final.pptx`](presentacion/LOGISTPULSE_Presentacion_Final.pptx)
- Guion oral: [`presentacion/guion_exposicion.md`](presentacion/guion_exposicion.md)

La presentación tiene 12 diapositivas, tablas y diagramas editables, notas del expositor y una duración sugerida de 9 minutos 10 segundos.

## Integración continua

GitHub Actions ejecuta pruebas y demostraciones en Python 3.10, 3.11 y 3.12 para `main`, `finalizacion-deber2` y pull requests.

## Estado de versión

La versión propuesta es `v1.0.0`, pero no se ha creado tag ni release. Antes de publicarla deben incorporarse las seis capturas reales de JFLAP, revisar PDF/presentación y contar con permisos de la propietaria para fusionar el PR. El detalle final está en [`ENTREGA_FINAL.md`](ENTREGA_FINAL.md).
