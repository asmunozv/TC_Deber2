# Seguimiento del equipo — LOGISTPULSE

Este documento reúne el seguimiento de revisiones y retrospectivas. Las retrospectivas que aparecen abajo son **borradores de redacción propuestos** a partir de las actividades del proyecto. Ariana y Jeanneth deben leerlos, corregirlos y confirmar que reflejan sus experiencias antes de considerarlos definitivos.

Integrantes:
- Ariana Muñoz — @asmunozv
- Jeanneth — @jann1111

## 1. Registro de revisiones cruzadas

Registrar una fila después de que la revisión se haya realizado.

| Fecha real | Persona revisora | Trabajo revisado | Observación / comprobación | Corrección acordada | Estado |
|---|---|---|---|---|---|
| Por completar | Jeanneth | Autómatas JFLAP de Ariana | Por completar | Por completar | Pendiente |
| Por completar | Ariana | Grafo AMR y Dijkstra | Por completar | Por completar | Pendiente |
| Por completar | Jeanneth | FEFO y reposición | Por completar | Por completar | Pendiente |
| Por completar | Ariana | Informe y clasificación P/NP | Por completar | Por completar | Pendiente |

La tabla propone qué revisar; no afirma que esas revisiones ya hayan ocurrido. Si la revisión se hace mediante Pull Request, añadir el enlace del PR en la observación.

## 2. Retrospectiva del Sprint 1 — Modelado formal

> **Borrador propuesto para validar con ambas integrantes.** Editar cualquier punto que no represente lo que realmente ocurrió.

- **Fecha real de conversación:** Por completar.
- **Participantes:** Ariana y Jeanneth (confirmar asistencia).
- **Qué salió bien:** La separación del proceso logístico en autómatas de pedidos, reservas y compras ayudó a representar cada flujo por partes. También fue útil definir secuencias aceptadas y rechazadas para comprobar el comportamiento de los modelos.
- **Qué dificultades hubo:** La parte más delicada fue decidir qué estados y transiciones correspondían a cada evento y evitar aceptar secuencias que no respetaran el orden del proceso. También fue necesario revisar la representación en JFLAP y la correspondencia entre el grafo de planta y sus pesos.
- **Qué mejorar en el siguiente sprint:** Antes de implementar, dejar acordados los símbolos, estados, transiciones y casos de prueba. Hacer una revisión cruzada de los modelos y registrar cualquier corrección en el mismo documento.
- **Acuerdos propuestos:** Usar una lista breve de casos normales y casos inválidos para revisar cada entregable antes de integrarlo. Responsable y fecha objetivo: por confirmar por el equipo.

## 3. Retrospectiva del Sprint 2 — Algoritmos logísticos

> **Borrador propuesto para validar con ambas integrantes.** Editar cualquier punto que no represente lo que realmente ocurrió.

- **Fecha real de conversación:** Por completar.
- **Participantes:** Ariana y Jeanneth (confirmar asistencia).
- **Qué salió bien:** Trabajar Dijkstra, FEFO y reposición como componentes separados facilitó entender qué resultado debía producir cada algoritmo. Las pruebas ayudaron a comprobar la ruta de menor costo, el orden de selección por vencimiento y el cálculo de la posición de inventario.
- **Qué dificultades hubo:** Fue importante prestar atención a los casos límite: lotes vencidos o sin stock, fechas iguales, stock insuficiente y posiciones de inventario exactamente en el mínimo. También se debía distinguir entre sugerir una reposición y modificar realmente el inventario.
- **Qué mejorar en el siguiente sprint:** Probar explícitamente los límites y documentar junto a cada algoritmo su entrada, salida y complejidad. Revisar que el código, las pruebas y la explicación del informe utilicen las mismas reglas.
- **Acuerdos propuestos:** Ejecutar la suite completa después de cada cambio importante y anotar los resultados y errores encontrados. Responsable y fecha objetivo: por confirmar por el equipo.

## 4. Retrospectiva del Sprint 3 — Complejidad, integración y entrega

> **Borrador propuesto para validar con ambas integrantes.** Editar cualquier punto que no represente lo que realmente ocurrió.

- **Fecha real de conversación:** Por completar.
- **Participantes:** Ariana y Jeanneth (confirmar asistencia).
- **Qué salió bien:** Organizar los diez problemas por categorías P, NP y NP-completo permitió estructurar el análisis teórico. La integración de los algoritmos, pruebas y documentación en el repositorio facilitó revisar el proyecto como un solo entregable.
- **Qué dificultades hubo:** La justificación de cada clasificación requirió cuidado, especialmente para diferenciar un problema que está en NP de uno que además es NP-completo. También fue necesario mantener consistentes el código, los resultados de las pruebas, el informe y la presentación.
- **Qué mejorar en futuros trabajos:** Distribuir las revisiones con anticipación, reservar tiempo específico para corregir el informe y comprobar todos los archivos de entrega antes de publicar la versión final. Mantener una lista de verificación compartida desde el inicio.
- **Acuerdos propuestos:** Antes de cerrar el proyecto, comprobar que el PDF y la presentación estén actualizados, ejecutar las pruebas finales y verificar que las evidencias estén incluidas. Responsable y fecha objetivo: por confirmar por el equipo.

## 5. Lista de control del release final

Marcar únicamente cuando exista evidencia:

- [ ] Informe PDF final revisado.
- [ ] Presentación final revisada.
- [ ] Capturas JFLAP incorporadas y legibles.
- [ ] Suite completa ejecutada después de los últimos cambios.
- [ ] Revisiones cruzadas registradas.
- [ ] Ariana y Jeanneth validaron y ajustaron las tres retrospectivas.
- [ ] Etiqueta Git `v1.0.0` creada.
- [ ] GitHub Release `LOGISTPULSE v1.0.0` publicado.

**Nota:** estos textos son propuestas de redacción, no testimonios ni acuerdos confirmados. Para cerrar las retrospectivas, ambas integrantes deben validarlos y completar la fecha real de conversación, confirmar quiénes participaron y modificar lo que no coincida con su experiencia. Una planificación asigna responsabilidades; un issue registra seguimiento; una revisión o retrospectiva solo se considera realizada cuando se documenta lo que efectivamente ocurrió.
