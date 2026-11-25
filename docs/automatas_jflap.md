# Fase A: autómatas finitos deterministas en JFLAP

## Convención formal

Cada archivo representa un AFD parcial `M=(Q,Σ,δ,q0,F)`. Para cada estado y símbolo hay como máximo una transición, por lo que el modelo es determinista. Una transición omitida produce rechazo inmediato. Formalmente, cada AFD parcial reconoce el mismo lenguaje que el AFD total obtenido al añadir un estado no final `Pozo`, dirigir a él todos los pares `(q,s)` ausentes y añadir `δ(Pozo,s)=Pozo` para todo `s∈Σ`.

Los estados finales representan procesos **cerrados**, no únicamente resultados exitosos. Por eso `Cancelado`, `Rechazada`, `Liberada` y `Expirada` pueden ser finales. Todos los estados de los tres modelos son alcanzables desde el estado inicial. Los archivos usan caracteres sin tilde en nombres de estado para maximizar compatibilidad con JFLAP; la documentación conserva la ortografía española.

## A1. Pedido

- `Q = {Borrador, Confirmado, Reservado, Preparacion, Empacado, Despachado, Entregado, Cancelado}`.
- `Σ = {a,b,c,d,e,f,x}`.
- `q0 = Borrador`.
- `F = {Entregado, Cancelado}`.

| Origen | Símbolo | Destino | Evento operativo |
|---|:---:|---|---|
| Borrador | `a` | Confirmado | Confirmar pedido |
| Confirmado | `b` | Reservado | Reservar inventario |
| Reservado | `c` | Preparación | Iniciar preparación |
| Preparación | `d` | Empacado | Empacar |
| Empacado | `e` | Despachado | Despachar |
| Despachado | `f` | Entregado | Confirmar entrega |
| Borrador | `x` | Cancelado | Cancelar borrador |
| Confirmado | `x` | Cancelado | Cancelar antes de reservar |
| Reservado | `x` | Cancelado | Liberar inventario reservado y cancelar atómicamente |

La transición `Reservado --x--> Cancelado` incorpora la cancelación indicada por el modelo operativo. El evento presupone que la aplicación libera la reserva dentro de la misma operación transaccional. Ninguna secuencia puede llegar a `Despachado` sin pasar por confirmación, reserva, preparación y empaque.

## A2. Reserva de inventario

- `Q = {Solicitada, Validada, Reservada, Consumida, Liberada, Rechazada, Expirada}`.
- `Σ = {a,b,c,l,r,v}`.
- `q0 = Solicitada`.
- `F = {Consumida, Liberada, Rechazada, Expirada}`.

| Origen | Símbolo | Destino | Evento operativo |
|---|:---:|---|---|
| Solicitada | `a` | Validada | Validar disponibilidad |
| Validada | `b` | Reservada | Confirmar reserva |
| Reservada | `c` | Consumida | Consumir unidades reservadas |
| Reservada | `l` | Liberada | Liberar unidades |
| Solicitada | `r` | Rechazada | Rechazar solicitud |
| Validada | `r` | Rechazada | Rechazar tras validación |
| Reservada | `v` | Expirada | Vencer el plazo de una reserva confirmada |

`Expirada` se incorpora como cierre terminal. El vencimiento solo parte de `Reservada`: una solicitud aún no confirmada no inmoviliza stock y, por tanto, no se modela como reserva expirada. No existe transición de `Solicitada` o `Validada` a `Consumida`.

## A3. Orden de compra

- `Q = {Borrador, En aprobacion, Aprobada, Enviada, Recepcion parcial, Recibida, Rechazada}`.
- `Σ = {a,p,e,r,c,x}`.
- `q0 = Borrador`.
- `F = {Recibida, Rechazada}`.

| Origen | Símbolo | Destino | Evento operativo |
|---|:---:|---|---|
| Borrador | `a` | En aprobación | Solicitar aprobación |
| En aprobación | `p` | Aprobada | Aprobar orden |
| Aprobada | `e` | Enviada | Enviar al proveedor |
| Enviada | `r` | Recepción parcial | Registrar recepción parcial |
| Recepción parcial | `r` | Recepción parcial | Registrar otra entrega parcial |
| Enviada | `c` | Recibida | Registrar recepción completa directa |
| Recepción parcial | `c` | Recibida | Completar recepción |
| Borrador | `x` | Rechazada | Rechazar borrador |
| En aprobación | `x` | Rechazada | Rechazar solicitud de aprobación |

La orden no puede enviarse mientras siga en aprobación ni después de ser rechazada. La autorrecepción parcial permite una o más entregas parciales antes del cierre completo.

## Pruebas reproducibles y resultados observados

La secuencia de estados incluye el estado inicial. Si falta una transición, la traza termina en el último estado alcanzado. El 24 de noviembre de 2026, `tests/test_automatas.py` observó todos los resultados siguientes.

| DFA | Cadena | Traza observada | Esperado/observado | Justificación |
|---|---|---|---|---|
| Pedido | `abcdef` | Borrador, Confirmado, Reservado, Preparación, Empacado, Despachado, Entregado | Acepta/Acepta | Flujo completo obligatorio |
| Pedido | `abx` | Borrador, Confirmado, Reservado, Cancelado | Acepta/Acepta | Libera inventario y cancela |
| Pedido | `x` | Borrador, Cancelado | Acepta/Acepta | Cancelación temprana |
| Pedido | cadena vacía | Borrador | Rechaza/Rechaza | Borrador no es final |
| Pedido | `abcde` | termina en Despachado | Rechaza/Rechaza | Falta confirmar entrega |
| Pedido | `ae` | Borrador, Confirmado | Rechaza/Rechaza | Salto ilegal a despacho |
| Pedido | `abcdefx` | termina en Entregado | Rechaza/Rechaza | No hay eventos después de un cierre |
| Reserva | `abc` | Solicitada, Validada, Reservada, Consumida | Acepta/Acepta | Consumo confirmado |
| Reserva | `abl` | Solicitada, Validada, Reservada, Liberada | Acepta/Acepta | Liberación válida |
| Reserva | `abv` | Solicitada, Validada, Reservada, Expirada | Acepta/Acepta | Vencimiento del plazo |
| Reserva | `r` | Solicitada, Rechazada | Acepta/Acepta | Rechazo temprano |
| Reserva | cadena vacía | Solicitada | Rechaza/Rechaza | Proceso incompleto |
| Reserva | `ac` | termina en Validada | Rechaza/Rechaza | No consume sin reservar |
| Reserva | `av` | termina en Validada | Rechaza/Rechaza | Una validación no confirmada no expira como reserva |
| Reserva | `abvc` | termina en Expirada | Rechaza/Rechaza | Estado terminal sin consumo posterior |
| Compra | `apec` | Borrador, En aprobación, Aprobada, Enviada, Recibida | Acepta/Acepta | Recepción completa directa |
| Compra | `aperc` | Borrador, En aprobación, Aprobada, Enviada, Recepción parcial, Recibida | Acepta/Acepta | Una recepción parcial |
| Compra | `aperrc` | añade dos visitas a Recepción parcial | Acepta/Acepta | Varias entregas parciales |
| Compra | `ax` | Borrador, En aprobación, Rechazada | Acepta/Acepta | Rechazo durante aprobación |
| Compra | cadena vacía | Borrador | Rechaza/Rechaza | Borrador no es final |
| Compra | `ae` | termina en En aprobación | Rechaza/Rechaza | Falta aprobación |
| Compra | `ap` | termina en Aprobada | Rechaza/Rechaza | Proceso aún abierto |
| Compra | `xe` | termina en Rechazada | Rechaza/Rechaza | Una orden rechazada no se envía |

La prueba automatizada también comprueba XML válido, tipo `fa`, un único estado inicial, finales existentes, símbolos de un carácter, ausencia de transiciones duplicadas y alcanzabilidad de cada estado.

## Ejecución manual en JFLAP

Java 21 está instalado en el entorno de desarrollo, pero no se encontró una instalación de JFLAP ni una interfaz gráfica autorizada para producir capturas. Por tanto, `docs/evidencias/jflap/` contiene instrucciones y queda pendiente de seis capturas auténticas. No se generaron imágenes que imiten JFLAP.

1. Descargar JFLAP desde su sitio oficial y abrir el archivo `.jar` con `java -jar JFLAP7.1.jar` (ajustar el nombre a la versión descargada).
2. Abrir `jflap/pedido.jff`; capturar el diagrama como `docs/evidencias/jflap/pedido_diagrama.png`.
3. En `Input > Multiple Run`, ingresar `abcdef`, `abx`, `x`, `abcde`, `ae` y `abcdefx`; capturar el resultado como `pedido_multiple_run.png`.
4. Abrir `jflap/reserva.jff`; capturar `reserva_diagrama.png`. En Multiple Run ingresar `abc`, `abl`, `abv`, `r`, `ac`, `av` y `abvc`; capturar `reserva_multiple_run.png`.
5. Abrir `jflap/compra.jff`; capturar `compra_diagrama.png`. En Multiple Run ingresar `apec`, `aperc`, `aperrc`, `ax`, `ae`, `ap` y `xe`; capturar `compra_multiple_run.png`.
6. Ejecutar además la cadena vacía con `Input > Step by State` o el mecanismo equivalente de la versión instalada y confirmar que el estado inicial no es final.

La verificación automatizada se ejecuta con:

```bash
python3 -m unittest tests.test_automatas -v
```
