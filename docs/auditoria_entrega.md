# Auditoría de entrega LOGISTPULSE

Fecha de auditoría: 24 de noviembre de 2026. Rama de trabajo: `finalizacion-deber2`.

## Fuentes y alcance

Se inspeccionaron los 20 archivos versionados, los ocho commits disponibles, la configuración de GitHub Actions y el informe PDF aportado por el equipo. El PDF corresponde al informe técnico actual, no al enunciado original del profesor. El archivo del enunciado citado por la documentación (`Deber2_Teoria_Computacion_LOGISTPULSE_USFQ.docx`) no está en el repositorio. Por ello, esta auditoría usa como requisitos primarios la consigna de finalización entregada por el equipo y conserva como datos verificables las figuras, fórmulas y casos ya documentados.

No se encontraron fuente LaTeX, presentación, capturas reales de JFLAP, release ni tag. Tampoco existía `.gitignore`.

## Matriz de correspondencia

| Requisito | Evidencia inicial | Error o riesgo encontrado | Corrección prevista/realizada | Estado |
|---|---|---|---|---|
| Pedido: ocho estados y flujo obligatorio | `jflap/pedido.jff`, `docs/automatas_jflap.md` | No permitía cancelar desde `Reservado` después de liberar inventario | Añadir transición atómica de liberación y cancelación; ampliar cadenas y trazas | En corrección |
| Reserva: siete estados | `jflap/reserva.jff` | Faltaba `Expirada` y el evento de vencimiento | Incorporar estado final y transición desde `Reservada` | En corrección |
| Compra: siete estados | `jflap/compra.jff` | Faltaban `En aprobación` y `Recepción parcial` | Completar aprobación, recepción directa/parcial y rechazo terminal | En corrección |
| Validez XML, determinismo y alcanzabilidad | `tests/test_automatas.py` | Solo comprobaba sintaxis básica y palabras; no validaba estados esperados, alcanzabilidad ni trazas | Reforzar validador y casos de cadena vacía, procesos incompletos y eventos tras estados terminales | En corrección |
| Evidencia real de JFLAP | Documentación de pasos manuales | No existen capturas auténticas | Comprobar Java/JFLAP; no fabricar capturas; dejar protocolo exacto si no hay GUI/JFLAP | Pendiente humano |
| Grafo de planta de 7 vértices | Código, CSV, documento y 12 pruebas | Implementación sólida; diagrama del PDF tiene etiquetas superpuestas | Mantener algoritmo y generar diagrama legible identificado como generado | En corrección |
| Dijkstra y ruta de 11 m | `src/planta_amr.py` | Dos rutas óptimas ya identificadas correctamente | Revalidar suite, salida y complejidad | Cumplido, por revalidar |
| FEFO | Código, documento y 9 pruebas FEFO | Política de vencimiento y reserva parcial está explícita | Revalidar entradas y resultados observados | Cumplido, por revalidar |
| Reposición | Código, documento y 11 pruebas | Prevención secuencial de duplicados correcta; concurrencia declarada como límite | Revalidar ejemplo 23/27 y evidencia | Cumplido, por revalidar |
| Diez correos | `src/correos.py`, fichas, tabla y 10 métodos de prueba | Contenido amplio; faltan registros actuales de ejecución | Ejecutar demos/suite y conservar salida auténtica | En corrección |
| Decidibilidad y parada | `docs/decidibilidad_parada.md` | Explicación correcta y de extensión breve | Integrar al informe final sin confundir recursos con indecidibilidad | Cumplido |
| Tres sprints e historial | `docs/sprints.md`, ocho commits | Plan no conciliado con commits reales; responsables/reuniones sin confirmar | Documentar solo evidencia comprobable y marcar datos del equipo pendientes | En corrección |
| README y estructura | `README.md` | Desactualizado: indica PDF y presentación pendientes; enlaces poco visibles | Actualizar instalación, ejecución, JFLAP, evidencias y resultados | En corrección |
| Informe editable y PDF | Solo PDF actual de 18 páginas | No hay fuente LaTeX; los autómatas del PDF están incompletos | Reconstruir fuente editable, compilar y revisar visualmente | En corrección |
| Presentación 8-10 minutos | No existe | Entregable ausente | Crear 12 diapositivas con notas/guion y tiempos | En corrección |
| GitHub Actions | `.github/workflows/pruebas.yml` | Solo se activa en `main`; no prueba demos ni versiones adicionales | Mantener suite reproducible y ampliar ramas/disparadores si procede | En corrección |
| Evidencia de pruebas | Referencia remota a 44 pruebas | Cifra histórica; cambiará al ampliar la suite | Generar `docs/evidencias/resultados_tests.txt` con resultados actuales | En corrección |
| Release | No hay tags | Publicación no autorizada y todavía no procede | Preparar candidato; no crear tag ni publicar sin autorización | Pendiente humano |

## Restricciones de evidencia

- Los diagramas generados por Graphviz o LaTeX se rotularán como diagramas generados, nunca como capturas de JFLAP.
- Solo se marcarán como observadas las salidas producidas en esta rama.
- Las reuniones, revisiones, responsables y retrospectivas no demostrables quedarán como pendientes de confirmación.
- No se hará `push`, merge a `main`, tag ni release sin autorización expresa.
