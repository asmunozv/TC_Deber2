# Guion de exposición LOGISTPULSE

Duración sugerida total: **9 minutos 10 segundos**. El texto ampliado también está guardado en las notas del expositor del archivo `.pptx`.

| Diapositiva | Tiempo | Guion breve |
|---:|---:|---|
| 1. Portada | 0:30 | Presentar el propósito: conectar modelos formales, algoritmos logísticos y límites computacionales. |
| 2. Contexto y objetivo | 0:40 | Enumerar los cinco entregables y distinguir evidencia automatizada de capturas reales de JFLAP. |
| 3. Autómata de pedidos | 0:50 | Recorrer el flujo obligatorio. Explicar que cancelar desde Reservado libera inventario y cierra el proceso. |
| 4. Reservas y compras | 0:55 | Mostrar Expirada, En aprobación y Recepción parcial. Recalcar que no se consume ni se envía antes de confirmar. |
| 5. Grafo y ruta AMR | 0:50 | Explicar pesos no negativos, Dijkstra y las dos rutas óptimas de 11 m. |
| 6. FEFO | 0:45 | Aplicar el orden fecha/código y explicar el plan parcial informativo. |
| 7. Reposición | 0:40 | Resolver posición 23 y sugerencia 27. Diferenciar sugerir de crear una orden. |
| 8. Diez correos | 0:55 | Explicar P ⊆ NP y la prueba adicional de NP-hardness para NP-completo. Aclarar C1, C2 y C3. |
| 9. Búsqueda frente a verificación | 0:45 | Comparar búsqueda factorial de TSP con verificación polinómica de un tour certificado. |
| 10. Decidibilidad y parada | 0:50 | Contrastar un algoritmo exponencial que sí termina con la inexistencia de un decisor universal para la parada. |
| 11. Implementación y pruebas | 0:45 | Resumir 46 pruebas, tres versiones de Python y la limitación de evidencia visual. |
| 12. Conclusiones | 0:45 | Cerrar con los cuatro hallazgos y las acciones pendientes antes del release. |

## Preguntas previsibles

- **¿Por qué Cancelado es final?** Porque representa un proceso cerrado, no una entrega exitosa.
- **¿Por qué el AFD es parcial?** Las transiciones omitidas rechazan; es equivalente a añadir un estado pozo no final.
- **¿Por qué hay dos rutas de 11 m?** El grafo contiene un empate; cualquiera de las dos es óptima.
- **¿NP significa “no polinómico”?** No. NP describe verificación polinómica; no se sabe si P=NP.
- **¿La instancia C1 demuestra NP-completitud?** No. Esa instancia es 2-CNF; la NP-completitud corresponde a 3-SAT general.
- **¿Qué falta para cerrar la entrega?** Seis capturas reales de JFLAP, revisión humana, permisos de GitHub y autorización del release.
