# Auditoría de entrega LOGISTPULSE

Fecha de auditoría inicial: 24 de noviembre de 2026. Cierre técnico: 25 de noviembre de 2026. Rama de trabajo: `finalizacion-deber2`.

## Fuentes y alcance

En la auditoría inicial se inspeccionaron los 20 archivos versionados, los ocho commits técnicos disponibles, la configuración de GitHub Actions y el informe PDF aportado por el equipo. Después se incorporaron los commits nuevos de `origin/main` sobre responsables, issues y retrospectivas. El PDF corresponde al informe técnico previo, no al enunciado original del profesor. El archivo del enunciado citado por la documentación (`Deber2_Teoria_Computacion_LOGISTPULSE_USFQ.docx`) no está en el repositorio. Por ello, esta auditoría usa como requisitos primarios la consigna de finalización entregada por el equipo y conserva como datos verificables las figuras, fórmulas y casos ya documentados.

No se encontraron fuente LaTeX, presentación, capturas reales de JFLAP, release ni tag. Tampoco existía `.gitignore`.

## Matriz de correspondencia

| Requisito | Evidencia inicial | Error o riesgo encontrado | Corrección prevista/realizada | Estado |
|---|---|---|---|---|
| Pedido: ocho estados y flujo obligatorio | `jflap/pedido.jff`, `docs/automatas_jflap.md` | No permitía cancelar desde `Reservado` después de liberar inventario | Se añadió transición atómica de liberación/cancelación y se ampliaron cadenas y trazas | Cumplido |
| Reserva: siete estados | `jflap/reserva.jff` | Faltaba `Expirada` y el evento de vencimiento | Se incorporó el estado final y la transición desde `Reservada` | Cumplido |
| Compra: siete estados | `jflap/compra.jff` | Faltaban `En aprobación` y `Recepción parcial` | Se completaron aprobación, recepción directa/parcial y rechazo terminal | Cumplido |
| Validez XML, determinismo y alcanzabilidad | `tests/test_automatas.py` | Solo comprobaba sintaxis básica y palabras; no validaba estados esperados, alcanzabilidad ni trazas | El validador cubre estructura formal, trazas, alcanzabilidad y estado pozo | Cumplido |
| Evidencia real de JFLAP | Documentación de pasos manuales | No existen capturas auténticas | Comprobar Java/JFLAP; no fabricar capturas; dejar protocolo exacto si no hay GUI/JFLAP | Pendiente humano |
| Grafo de planta de 7 vértices | Código, CSV, documento y 12 pruebas | Implementación sólida; diagrama del PDF tenía etiquetas superpuestas | Se creó un diagrama legible en el PDF y la presentación | Cumplido |
| Dijkstra y ruta de 11 m | `src/planta_amr.py` | Dos rutas óptimas ya identificadas correctamente | Suite, salida y complejidad revalidadas | Cumplido |
| FEFO | Código, documento y 9 pruebas FEFO | Política de vencimiento y reserva parcial está explícita | Entradas y resultados revalidados | Cumplido |
| Reposición | Código, documento y 11 pruebas | Prevención secuencial de duplicados correcta; concurrencia declarada como límite | Ejemplo 23/27 y evidencia revalidados | Cumplido |
| Diez correos | `src/correos.py`, fichas, tabla y 10 métodos de prueba | Faltaban registros actuales de ejecución | Se ejecutaron demos/suite y se conservó salida auténtica | Cumplido |
| Decidibilidad y parada | `docs/decidibilidad_parada.md` | Explicación correcta y de extensión breve | Integrar al informe final sin confundir recursos con indecidibilidad | Cumplido |
| Tres sprints e historial | `docs/sprints.md`, historial y seguimiento | El plan no estaba conciliado con commits reales | Se conciliaron commits, responsables, issues y retrospectivas disponibles | Cumplido |
| README y estructura | `README.md` | Indicaba PDF y presentación pendientes | Se actualizaron instalación, ejecución, JFLAP, evidencias y resultados | Cumplido |
| Informe editable y PDF | Solo PDF previo de 18 páginas | No había fuente LaTeX; los autómatas estaban incompletos | Se reconstruyó fuente, se generó PDF y se revisaron sus 6 páginas | Cumplido |
| Presentación 8-10 minutos | No existía | Entregable ausente | Se crearon 12 diapositivas, notas y guion de 9:10 | Cumplido |
| GitHub Actions | `.github/workflows/pruebas.yml` | Solo se activaba en `main`; no probaba demos | Se amplió a tres versiones de Python, rama final y demos | Cumplido |
| Evidencia de pruebas | Referencia remota a 44 pruebas | La cifra histórica quedó obsoleta | Se generó registro auténtico de 46 pruebas, 0 fallos | Cumplido |
| Release | No hay tags | Publicación no autorizada y todavía no procede | Preparar candidato; no crear tag ni publicar sin autorización | Pendiente humano |

## Restricciones de evidencia

- Los diagramas generados por Graphviz o LaTeX se rotularán como diagramas generados, nunca como capturas de JFLAP.
- Solo se marcarán como observadas las salidas producidas en esta rama.
- Las reuniones, revisiones, responsables y retrospectivas no demostrables quedarán como pendientes de confirmación.
- El equipo autorizó intentar gestionar PRs. El merge fue rechazado por GitHub con HTTP 403; no se creó tag ni release.
