# Tabla resumen — diez correos LOGISTPULSE

Todas las entradas son finitas; las diez versiones de decisión son **decidibles y computables**. Las etiquetas P, NP y NP-completo expresan niveles distintos de evidencia: P ⊆ NP, y NP-completo ⊆ NP. **NP** en N1–N4 no excluye pertenencia a P.

| Caso | Versión | Evidencia/clase | Solución exacta | Tiempo de búsqueda | Espacio auxiliar | Certificado/verificación | Resultado |
|---|---|---|---|---|---|---|---|
| P1 Alcanzabilidad | Decisión | P | BFS | O(V+E) | O(V) | Camino; O(V+E) | Durán→Quito→Norte |
| P2 Ruta mínima | Optimización / decisión con umbral | P | Dijkstra (pesos ≥0) | O((V+E) log V) | O(V+E) | Ruta; O(V+E) | mínimo 8, dos rutas |
| P3 Flujo máximo | Optimización / decisión con umbral | P | Edmonds–Karp | O(VE²) | O(V+E) | Flujo y corte; polinómico | 10 camiones/día |
| N1 Isomorfismo | Decisión | NP | Permutaciones | O(n! n²) | O(n) | Biyección; O(n²) | (1,0,2) |
| N2 Divisor en [2,B] | Decisión | NP | División exhaustiva | O(B M(L)) | O(L) | d; O(L²) escolar | 7 divide 91 |
| N3 Log discreto acotado | Decisión | NP | Residuos sucesivos | O(B M(k)) | O(k+b) | x; O((b+1)k²) escolar | x=6 |
| N4 Automorfismo | Decisión | NP | Permutaciones | O(n! n²) | O(n) | Permutación no trivial; O(n²) | Sí, triángulo |
| C1 3-SAT | Decisión | NP-completo | DPLL | Exponencial (cota de implementación O(2^n n(m+1))) | O(n²) | Asignación; O(n+m) | SAT |
| C2 TSP de decisión | Decisión | NP-completo | Permutaciones | O(n! n) | O(n) | Tour; O(n), prevalidado | 15 ≤ 20 |
| C3 Vertex Cover | Decisión | NP-completo | Subconjuntos | O(2^V(V+E)) | O(V) | Cobertura; O(V+E) | {B}, k=1 |

**Notación:** V=vertices, E=aristas, n=variables o vértices según caso, m=cláusulas, B=límite numérico, L=bits máximos para N2, k=bits del módulo para N3 y b=bits de B para N3. M(s) es costo de multiplicación/división modular con s bits; aritmética escolar O(s²). Todas las cotas auxiliares excluyen datos de entrada.

**Precisión C1:** la fórmula concreta `(x1 ∨ ¬x2) ∧ (x2 ∨ x3)` pertenece a la subfamilia 2-CNF, resoluble en P. La afirmación NP-completa corresponde a 3-SAT **general** (cláusulas de a lo sumo tres literales, con instancias difíciles de tres literales).

**Precisión C2:** se solicita un *ciclo* hamiltoniano, no solo una ruta abierta, porque hay regreso a Planta.
