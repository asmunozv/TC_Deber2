# Evidencia JFLAP pendiente

Este directorio no contiene capturas generadas o simuladas. Java 21 está disponible, pero JFLAP y una sesión gráfica no estaban instalados durante la finalización automatizada.

Descarga oficial recomendada: [JFLAP 7.1](https://www.jflap.org/jflaptmp/). El sitio oficial recomienda la versión 7.1 y distribuye un archivo `.jar`.

Ejecutar:

```bash
java -jar /ruta/a/JFLAP7.1.jar
```

Seguir las cadenas y pasos de `docs/automatas_jflap.md` y guardar exactamente:

- `pedido_diagrama.png`
- `pedido_multiple_run.png`
- `reserva_diagrama.png`
- `reserva_multiple_run.png`
- `compra_diagrama.png`
- `compra_multiple_run.png`

Antes de incluirlas en Git, comprobar que cada imagen muestra la ventana real de JFLAP y que los resultados coinciden con la tabla documentada. Como `.gitignore` evita incorporarlas accidentalmente, usar `git add -f docs/evidencias/jflap/*.png` después de la revisión humana.
