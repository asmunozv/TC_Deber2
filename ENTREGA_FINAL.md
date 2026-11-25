# Estado de entrega final - LOGISTPULSE

Fecha de cierre técnico: 25 de noviembre de 2026. Rama: `finalizacion-deber2`.

## Requisitos cumplidos y evidencia

| Área | Estado | Evidencia |
|---|---|---|
| Pedido | Cumplido | Ocho estados, flujo obligatorio y cancelación desde Reservado con liberación atómica |
| Reserva | Cumplido | Siete estados, incluida Expirada, y consumo solo después de validar/reservar |
| Compra | Cumplido | Siete estados, incluidos En aprobación y Recepción parcial |
| Formalización AFD | Cumplido | Q, Σ, q0, F, δ, determinismo, alcanzabilidad y equivalencia con estado pozo |
| Cadenas | Cumplido | 23 casos documentados con traza, resultado esperado y observado |
| JFLAP visual | Pendiente humano | Seis capturas auténticas; no se fabricaron imágenes |
| Grafo/Dijkstra | Cumplido | 7 vértices, 11 aristas, dos rutas óptimas de 11 m, bloqueos y validaciones |
| FEFO/reposición | Cumplido | Política, desempate, stock insuficiente, posición 23 y sugerencia 27 |
| Diez correos | Cumplido | Fichas, tabla, algoritmos, certificados, reducciones y pruebas |
| Decidibilidad/parada | Cumplido | Documento conceptual e integración en el informe |
| Pruebas | Cumplido | 46 exitosas, 0 fallos; tres módulos ejecutados |
| Sprints | Cumplido con evidencia disponible | Backlog, responsables acordados, commits, retrospectivas y limitaciones |
| Informe | Cumplido | PDF revisado visualmente y fuente LaTeX editable |
| Presentación | Cumplido | 12 diapositivas editables, notas y guion de 9:10 |
| Release | Pendiente de autorización | Se propone `v1.0.0`; no hay tag ni publicación |

## Errores corregidos

- Se añadió `Reservado --x--> Cancelado` en pedido para liberar inventario y cancelar.
- Se añadió `Expirada` a reservas con el evento `v` desde una reserva confirmada.
- Se añadieron `En aprobación` y `Recepción parcial` a compras.
- Se impidieron envíos antes de aprobación y eventos posteriores a estados terminales.
- El test JFLAP ahora valida estados exactos, alfabeto, determinismo, alcanzabilidad, trazas y estado pozo.
- Se actualizó GitHub Actions para Python 3.10, 3.11 y 3.12 y para ejecutar las demostraciones.
- Se corrigió la documentación que declaraba capturas JFLAP incorporadas cuando no existen.
- Se reemplazó la cifra histórica de 44 pruebas por el resultado vigente de 46.
- Se reconstruyó la fuente editable del informe y se creó una presentación que no existía.

## Archivos principales creados o actualizados

- `jflap/pedido.jff`, `jflap/reserva.jff`, `jflap/compra.jff`
- `tests/test_automatas.py`
- `docs/automatas_jflap.md`
- `docs/auditoria_entrega.md`
- `docs/evidencias/resultados_tests.txt`
- `docs/evidencias/jflap/README.md`
- `docs/sprints.md`, `docs/seguimiento_equipo.md`
- `informe/informe_final.tex`
- `informe/LOGISTPULSE_Informe_Final.pdf`
- `presentacion/LOGISTPULSE_Presentacion_Final.pptx`
- `presentacion/guion_exposicion.md`
- `scripts/generar_informe_pdf.py`
- `README.md`, `.gitignore`, `.github/workflows/pruebas.yml`

## Resultados observados

```text
python3 -m unittest discover -s tests -v
Ran 46 tests in 0.012s
OK
```

Las salidas de Dijkstra, FEFO/reposición y los diez correos están en `docs/evidencias/resultados_tests.txt`.

## Estado de JFLAP

Java 21.0.8 está instalado. No se encontró JFLAP instalado en el entorno de finalización. Los `.jff` son XML válidos y pasan el verificador automatizado, pero esto no reemplaza la ejecución visual.

Pasos manuales:

```bash
# Descargar JFLAP 7.1 desde https://www.jflap.org/jflaptmp/
java -jar /ruta/a/JFLAP7.1.jar
```

Abrir cada `.jff`, ejecutar `Input > Multiple Run` con las cadenas de `docs/automatas_jflap.md` y guardar:

```text
docs/evidencias/jflap/pedido_diagrama.png
docs/evidencias/jflap/pedido_multiple_run.png
docs/evidencias/jflap/reserva_diagrama.png
docs/evidencias/jflap/reserva_multiple_run.png
docs/evidencias/jflap/compra_diagrama.png
docs/evidencias/jflap/compra_multiple_run.png
```

Después de revisarlas:

```bash
git add -f docs/evidencias/jflap/*.png
git commit -m "docs(jflap): añadir capturas reales de diagramas y ejecuciones"
```

## Estado del PDF

El PDF final tiene 6 páginas A4 y se revisó página por página. La fuente LaTeX se reconstruyó, pero Tectonic no pudo descargar su paquete base por tiempo de espera del servidor. Para evitar bloquear la entrega, el PDF se generó con el script reproducible de ReportLab:

```bash
python3 scripts/generar_informe_pdf.py
```

## Estado de la presentación

La presentación tiene 12 diapositivas, 4 tablas nativas, diagramas editables y notas en todas las láminas. El validador informó 12 diapositivas, 0 hallazgos de geometría, importación correcta y fuente Arial coherente. Duración del guion: 9:10.

## Estado de Git y pull requests

- Rama local: `finalizacion-deber2`.
- `origin/main` se incorporó y los conflictos se resolvieron conservando evidencia verificable.
- PR #5: limpio y técnicamente fusionable; su contenido válido se incorporó a esta rama.
- PR #4: abierto, con conflicto y cambios ya superados por `main`.
- PR #6: abierto, pero no debe fusionarse tal como está porque declara evidencias JFLAP inexistentes.
- El intento de fusionar #5 desde la cuenta autenticada `kjjjcbs` recibió HTTP 403.
- No se hizo push directo a `main`, tag ni release.

Para que Jeanneth pueda crear y fusionar PRs en el repositorio original, Ariana debe invitar a `@jann1111` como colaboradora y Jeanneth debe aceptar. Después:

```bash
git push -u origin finalizacion-deber2
# Abrir PR finalizacion-deber2 -> main desde GitHub
```

## Actividades que requieren intervención humana

1. Obtener las seis capturas auténticas de JFLAP.
2. Revisar y aprobar visualmente el PDF y la presentación.
3. Conceder/aceptar permiso de colaboradora en GitHub.
4. Crear y fusionar el PR de `finalizacion-deber2`.
5. Cerrar #4 y corregir o cerrar #6 para evitar documentación falsa.
6. Crear `v1.0.0` y el release únicamente después de las verificaciones anteriores.
