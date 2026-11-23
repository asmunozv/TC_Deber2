# Diez fichas de análisis — Fase D

**Marco común:** problemas de decisión sobre instancias finitas codificadas como grafos, matrices o números binarios. Los diez son decidibles y computables: los algoritmos descritos terminan. **Algoritmos exactos**, no aproximaciones o heurísticas. Se documentan casos normales, límite e inválidos en `tests/test_correos.py`.

## P1 — ¿Puede llegar el envío a la zona Norte? (Daniela Paredes)
- **Entrada:** red dirigida de rutas activas G=(V,E); origen Durán y destino Norte.
- **Salida/restricciones:** respuesta Sí/No; solo conexiones habilitadas y vértices registrados.
- **Clase/evidencia:** P, BFS en listas de adyacencia.
- **Decidibilidad/computabilidad:** BFS visita cada vértice a lo sumo una vez; cuando encuentra Norte responde Sí, al agotar cola responde No.
- **Algoritmo:** BFS, exacto. **Tiempo** O(V+E), **espacio** O(V).
- **Instancia:** Durán→Quito→Norte; respuesta Sí. Pruebas: alcanzable, inalcanzable, mismo origen/destino, dato inválido.
- **Código:** `bfs_camino` en `src/correos.py`.

## P2 — Ruta mínima entre centros de distribución (Marco Cedeño)
- **Entrada:** grafo ponderado dirigido, tiempos no negativos; Quito como origen y Guayaquil como destino.
- **Salida/restricciones:** menor costo y predecesores para reconstruir camino; optimización, con versión de decisión «¿costo ≤ T?».
- **Clase/evidencia:** P por Dijkstra con pesos ≥0.
- **Decidibilidad/computabilidad:** número finito de nodos/aristas y mejoras; la cola se agota y entrega distancias.
- **Algoritmo:** Dijkstra exacto, **tiempo** O((V+E) log V), **espacio auxiliar** O(V+E) en implementación con inserciones repetidas en heap.
- **Instancia:** Quito→Latacunga→Guayaquil (2+6=8) y Quito→Ambato→Guayaquil (5+3=8); ambas óptimas.
- **Código/pruebas:** `dijkstra`; camino, empate, destino inalcanzable, origen igual a destino, negativo inválido.

## P3 — Máximo de camiones hacia clientes (Luis Vaca)
- **Entrada:** red dirigida con capacidades enteras no negativas, Planta como fuente y Clientes como sumidero.
- **Salida/restricciones:** flujo máximo; conservación en nodos intermedios; versión de decisión «¿flujo ≥ K?».
- **Clase/evidencia:** P por Edmonds–Karp.
- **Decidibilidad/computabilidad:** BFS de caminos aumentantes sobre red residual; a lo sumo O(VE) aumentos; termina.
- **Algoritmo:** Edmonds–Karp exacto. **Tiempo** O(VE²), **espacio** O(V+E).
- **Instancia:** rutas aumentantes con flujos 4, 5, 1 → **10 camiones/día**. Corte de entrada Clientes 4+6=10 prueba optimalidad.
- **Código/pruebas:** `flujo_maximo`; normal, cero, sin ruta, negativa inválida.

## N1 — Comparar topologías equivalentes (Elena Ruiz)
- **Entrada:** matrices de adyacencia binarias A y B.
- **Salida/restricciones:** decisión de isomorfismo: biyección entre vértices que preserve aristas y no aristas.
- **Clase/evidencia:** pertenece a NP: certificado p de tamaño polinómico.
- **Certificado:** p=(1,0,2), que transforma la red camino de tres nodos en la misma estructura con centros reetiquetados.
- **Verificador:** confirmar p es permutación y que A[i][j]=B[p[i]][p[j]] para todos i,j; O(n²) tiempo y O(n) auxiliar.
- **Decidibilidad/computabilidad:** enumeración finita de permutaciones hasta éxito o agotamiento.
- **Algoritmo:** exhaustivo exacto; tiempo O(n!n²); espacio auxiliar O(n).
- **Pruebas:** isomorfos, no isomorfos, identidad, certificado repetido y matriz inválida.
- **No se demuestra NP-completitud ni exclusión de P.**

## N2 — ¿Tiene N un factor en este intervalo? (Andrés Molina)
- **Entrada:** enteros N≥2 y B≥2 en binario.
- **Salida/restricciones:** ¿existe divisor entero d con 2≤d≤B y N mod d=0?
- **Clase/evidencia:** pertenece a NP.
- **Certificado/verificador:** d=7 para N=91, B=10; validar intervalo y residuo con aritmética polinómica O(L²) escolar, L=bits máximos.
- **Decidibilidad/computabilidad:** búsqueda finita desde 2 hasta min(N,B); termina.
- **Algoritmo:** división exhaustiva exacta; tiempo O(B·M(L)) (cota superior), O(BL²) escolar; espacio O(L).
- **Instancia:** 91 mod 7 = 0; respuesta Sí.
- **Pruebas:** divisor válido, primo sin divisor acotado, límite inferior y negativo inválido.
- **No se afirma NP-completitud.** La búsqueda directa no representa el mejor algoritmo teórico conocido.

## N3 — ¿Existe exponente x que produzca h? (Paola León)
- **Entrada:** p primo, 0≤g,h<p, B≥0 en binario.
- **Salida/restricciones:** ¿existe x entero 0≤x≤B con g^x ≡ h (mod p)?
- **Clase/evidencia:** pertenece a NP.
- **Certificado/verificador:** x=6; 5^6 mod 23=8. Verificar intervalo y exponenciación modular rápida; O((b+1)k²) escolar, k bits de p y b bits del límite.
- **Decidibilidad/computabilidad:** probar a lo sumo B+1 exponentes; siempre termina.
- **Algoritmo:** residuos sucesivos exactos; tiempo O(B·M(k)), espacio O(k+b).
- **Instancia:** p=23, g=5, h=8, B=10; respuesta Sí.
- **Pruebas:** éxito, límite 5 sin éxito, exponente cero, negativo y certificado fuera de rango.
- **Nota:** primalidad de p es precondición del expediente, no se certifica por este programa.

## N4 — ¿La topología tiene una simetría? (Santiago Jaramillo)
- **Entrada:** matriz de adyacencia de grafo simple.
- **Salida/restricciones:** ¿existe automorfismo no idéntico que preserve adyacencias?
- **Clase/evidencia:** pertenece a NP.
- **Certificado/verificador:** p=(1,0,2), biyección no identidad; A[i][j]=A[p[i]][p[j]]; O(n²).
- **Decidibilidad/computabilidad:** búsqueda exhaustiva finita.
- **Algoritmo:** permutaciones exactas, O(n!n²) tiempo; O(n) espacio auxiliar.
- **Instancia:** triángulo; Sí. El programa puede encontrar (0,2,1) primero; ambas son válidas.
- **Pruebas:** triángulo, identidad rechazada, un solo nodo, matriz inválida.
- **No se afirma NP-completitud.**

## C1 — ¿Hay una asignación que cumpla todas las reglas? (Mónica Ruiz)
- **Entrada:** n variables booleanas, m cláusulas de máximo tres literales (3-CNF).
- **Salida/restricciones:** ¿existe asignación que satisfaga todas las cláusulas?
- **Clase:** 3-SAT general es NP-completo.
- **Certificado/verificador (NP):** asignación x1=True, x2=True, x3=False para las cláusulas del expediente; evaluar cada literal y todas las cláusulas en O(n+m), con O(n) espacio.
- **NP-hard / reducción:** SAT ≤p 3-SAT. Para cláusulas extensas se introducen variables auxiliares y se encadenan cláusulas con hasta 3 literales, preservando satisfacibilidad. Por ejemplo (a∨b∨c∨d) equivale en satisfacibilidad a (a∨b∨y)∧(¬y∨c∨d). La transformación completa de una fórmula es de tamaño polinómico, y SAT es NP-completo por Cook–Levin.
- **Decidibilidad/computabilidad:** a lo sumo 2^n asignaciones; DPLL termina.
- **Algoritmo:** DPLL exacto con propagación unitaria y retroceso; peor caso exponencial; cota de esta implementación O(2^n·n·(m+1)), espacio O(n²).
- **Instancia:** (x1∨¬x2)∧(x2∨x3) es satisfacible.
- **Advertencia:** la instancia concreta es 2-CNF y pertenece a 2-SAT, que está en P; **no** es una prueba de dureza por sí misma.
- **Pruebas:** SAT, UNSAT, asignación incorrecta, fórmula vacía, literales inválidos.

## C2 — ¿Existe una ruta hamiltoniana dentro del presupuesto? (Jorge Tapia)
- **Entrada:** matriz de distancias no negativas y umbral L.
- **Salida/restricciones:** ¿existe tour que empieza en Planta, visita todos los centros exactamente una vez y vuelve al origen, con costo ≤L? Es **ciclo**, no ruta abierta.
- **Clase:** TSP de decisión es NP-completo.
- **Certificado/verificador (NP):** (0,1,2,0), comprobar inicio/regreso, permutación, existencia de aristas y sumar n costos; O(n) después de prevalidar datos (O(n²) con validación completa).
- **NP-hard / reducción:** Ciclo Hamiltoniano ≤p TSP decisión. Sobre mismos vértices construir grafo completo con distancia 1 si la arista existe en el original y 2 si no; límite L=n. Hay tour con costo ≤n si y solo si existe ciclo hamiltoniano. Matriz construida en O(n²).
- **Decidibilidad/computabilidad:** como máximo (n-1)! órdenes con origen fijo.
- **Algoritmo:** enumeración exacta, tiempo O(n! n); espacio O(n).
- **Instancia:** Planta→Quito→Guayaquil→Planta cuesta 4+3+8=15≤20.
- **Pruebas:** tour válido, presupuesto 14 no válido, 15 exacto, centro repetido, conexión inexistente, peso negativo.

## C3 — ¿Bastan k almacenes para cubrir todas las zonas? (Carla Núñez)
- **Entrada:** grafo no dirigido G=(V,E), entero k≥0.
- **Salida/restricciones:** ¿existe S⊆V con |S|≤k tal que cada arista tiene un extremo seleccionado? Corresponde a **Vertex Cover** (cubrir corredores), no Dominating Set.
- **Clase:** NP-completo.
- **Certificado/verificador (NP):** S={B} para A—B—C, k=1; comprobar cardinalidad y cada arista en O(V+E), espacio O(V).
- **NP-hard / reducción:** Independent Set ≤p Vertex Cover. Dado (G,t), crear (G,k=|V|-t). I es independiente de tamaño ≥t si y solo si V\I es vertex cover de tamaño ≤k. Transformación polinómica.
- **Decidibilidad/computabilidad:** 2^V subconjuntos finitos.
- **Algoritmo:** enumeración de combinaciones hasta tamaño k, exacta; O(2^V(V+E)) tiempo, O(V) espacio auxiliar, excluido grafo.
- **Instancia:** seleccionar B cubre A—B y B—C.
- **Pruebas:** {B} válido, {A} incorrecto, k=0, grafo sin aristas, triángulo, grafo no simétrico.

## Cierre
P ⊆ NP, mientras que NP-completo implica pertenencia a NP y NP-hardness. Que un problema sea decidible no garantiza que su búsqueda exhaustiva sea viable en la práctica. La evidencia de salidas reproducibles está en `tests/test_correos.py`; los resultados deben contrastarse con una ejecución real antes de anexarse como observados.
