"""Genera el informe final PDF cuando la distribución LaTeX no está disponible."""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, Flowable, ListFlowable, ListItem,
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "informe" / "LOGISTPULSE_Informe_Final.pdf"
AZUL = colors.HexColor("#153B5B")
VERDE = colors.HexColor("#1B7F79")
GRIS = colors.HexColor("#F2F5F7")
ROJO = colors.HexColor("#9B2C2C")


class AutomataDiagram(Flowable):
    def __init__(self, states, transitions, finals, width=16.5 * cm, height=4.2 * cm):
        super().__init__()
        self.width, self.height = width, height
        self.states, self.transitions, self.finals = states, transitions, set(finals)

    def draw(self):
        c = self.canv
        n = len(self.states)
        radius = 16
        gap = (self.width - 50) / max(1, n - 1)
        y = self.height / 2
        pos = {name: (25 + i * gap, y) for i, name in enumerate(self.states)}
        c.setStrokeColor(AZUL)
        c.setFillColor(colors.white)
        c.setLineWidth(1.2)
        # Arrows first, so state circles remain clean.
        for src, label, dst in self.transitions:
            x1, y1 = pos[src]
            x2, y2 = pos[dst]
            if src == dst:
                c.arc(x1 - 20, y1 + 4, x1 + 20, y1 + 44, 20, 300)
                c.setFont("Helvetica-Bold", 7)
                c.drawCentredString(x1, y1 + 47, label)
                continue
            direction = 1 if x2 >= x1 else -1
            start, end = x1 + direction * radius, x2 - direction * radius
            c.line(start, y1, end, y2)
            c.setFillColor(AZUL)
            c.saveState()
            c.translate(end, y2)
            if direction < 0:
                c.rotate(180)
            c.line(0, 0, -5, 3)
            c.line(0, 0, -5, -3)
            c.restoreState()
            c.setFont("Helvetica-Bold", 7)
            c.drawCentredString((x1 + x2) / 2, y + 7, label)
        for name, (x, yy) in pos.items():
            c.setFillColor(colors.white)
            c.setStrokeColor(VERDE if name in self.finals else AZUL)
            c.circle(x, yy, radius, fill=1, stroke=1)
            if name in self.finals:
                c.circle(x, yy, radius - 3, fill=0, stroke=1)
            c.setFillColor(colors.black)
            c.setFont("Helvetica", 6.5)
            c.drawCentredString(x, yy - 2, name[:14])
        first_x, _ = pos[self.states[0]]
        c.setStrokeColor(AZUL)
        c.line(0, y, first_x - radius, y)
        c.line(first_x - radius, y, first_x - radius - 5, y + 3)
        c.line(first_x - radius, y, first_x - radius - 5, y - 3)


class GraphDiagram(Flowable):
    def __init__(self, width=16 * cm, height=7.5 * cm):
        super().__init__()
        self.width, self.height = width, height

    def draw(self):
        c = self.canv
        coords = {"R": (25, 105), "A": (135, 175), "B": (135, 45),
                  "C": (250, 25), "P": (275, 145), "E": (390, 105), "D": (505, 105)}
        edges = [("R", "A", 4), ("R", "B", 2), ("A", "B", 1), ("A", "P", 3),
                 ("A", "E", 5), ("B", "P", 7), ("B", "C", 3), ("C", "P", 2),
                 ("P", "E", 2), ("C", "E", 4), ("E", "D", 3)]
        route = {frozenset(x) for x in [("R", "B"), ("B", "A"), ("A", "P"),
                                        ("P", "E"), ("E", "D")]}
        for u, v, w in edges:
            x1, y1 = coords[u]; x2, y2 = coords[v]
            c.setStrokeColor(VERDE if frozenset((u, v)) in route else colors.HexColor("#78909C"))
            c.setLineWidth(2.5 if frozenset((u, v)) in route else 1.2)
            c.line(x1, y1, x2, y2)
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            c.setFillColor(colors.white); c.rect(mx - 7, my - 6, 14, 12, fill=1, stroke=0)
            c.setFillColor(colors.black); c.setFont("Helvetica-Bold", 8); c.drawCentredString(mx, my - 3, str(w))
        for label, (x, y) in coords.items():
            c.setFillColor(colors.white); c.setStrokeColor(AZUL); c.setLineWidth(1.6)
            c.circle(x, y, 14, fill=1, stroke=1)
            c.setFillColor(AZUL); c.setFont("Helvetica-Bold", 9); c.drawCentredString(x, y - 3, label)
        c.setFillColor(VERDE); c.setFont("Helvetica-Bold", 9)
        c.drawString(25, 202, "Ruta destacada: R-B-A-P-E-D = 11 m")


def make_styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle("TitleX", parent=s["Title"], fontName="Helvetica-Bold", fontSize=26,
                         leading=31, textColor=AZUL, alignment=TA_CENTER, spaceAfter=16))
    s.add(ParagraphStyle("SubTitleX", parent=s["Normal"], fontName="Helvetica", fontSize=15,
                         leading=20, textColor=VERDE, alignment=TA_CENTER, spaceAfter=18))
    s.add(ParagraphStyle("H1X", parent=s["Heading1"], fontName="Helvetica-Bold", fontSize=16,
                         leading=19, textColor=AZUL, spaceBefore=11, spaceAfter=7))
    s.add(ParagraphStyle("H2X", parent=s["Heading2"], fontName="Helvetica-Bold", fontSize=12,
                         leading=15, textColor=VERDE, spaceBefore=8, spaceAfter=5))
    s.add(ParagraphStyle("BodyX", parent=s["BodyText"], fontName="Helvetica", fontSize=9.2,
                         leading=13.2, spaceAfter=6, alignment=4))
    s.add(ParagraphStyle("SmallX", parent=s["BodyText"], fontName="Helvetica", fontSize=7.8,
                         leading=10, spaceAfter=3))
    s.add(ParagraphStyle("Callout", parent=s["BodyText"], fontName="Helvetica-Bold", fontSize=9,
                         leading=13, borderColor=VERDE, borderWidth=1, borderPadding=8,
                         backColor=GRIS, spaceBefore=8, spaceAfter=8))
    s.add(ParagraphStyle("CodeX", parent=s["Code"], fontName="Courier", fontSize=8,
                         leading=11, backColor=GRIS, borderPadding=6, spaceAfter=8))
    return s


def para(text, style):
    return Paragraph(text, style)


def table(data, widths, header=True, font=7.4):
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    commands = [
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), font),
        ("LEADING", (0, 0), (-1, -1), font + 2.2),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#AAB7C4")),
        ("ROWBACKGROUNDS", (0, 1 if header else 0), (-1, -1), [colors.white, GRIS]),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    if header:
        commands += [("BACKGROUND", (0, 0), (-1, 0), AZUL),
                     ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                     ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")]
    t.setStyle(TableStyle(commands))
    return t


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    styles = make_styles()
    body, small = styles["BodyX"], styles["SmallX"]
    story = []

    story += [Spacer(1, 2.2 * cm), para("LOGISTPULSE", styles["TitleX"]),
              para("Decisiones, algoritmos y límites computacionales", styles["SubTitleX"]),
              Spacer(1, 0.6 * cm), para("Deber 2 - Informe técnico final", styles["H1X"]),
              Spacer(1, 0.8 * cm), para("Ariana Muñoz y Jeanneth Cabascango", styles["SubTitleX"]),
              para("Universidad San Francisco de Quito<br/>25 de noviembre de 2026", styles["SubTitleX"]),
              Spacer(1, 1.0 * cm), para("Repositorio: github.com/asmunozv/TC_Deber2<br/>Rama: finalizacion-deber2", styles["Callout"]),
              Spacer(1, 0.6 * cm), para("Los archivos y pruebas JFLAP se verificaron. Las seis capturas auténticas de la aplicación siguen pendientes; este informe no las sustituye con imágenes fabricadas.", styles["Callout"]), PageBreak()]

    story += [para("1. Resumen y objetivos", styles["H1X"]),
              para("LOGISTPULSE integra autómatas finitos, rutas ponderadas, políticas de inventario y teoría de complejidad. Se completaron tres AFD, Dijkstra para una planta de siete zonas, FEFO, la regla de reposición y diez expedientes computacionales. La implementación usa Python 3.10+ y una suite de 46 pruebas.", body),
              para("El objetivo es demostrar corrección, terminación, complejidad y límites computacionales sin confundir una instancia pequeña con la complejidad del problema general.", body),
              para("2. Autómatas de procesos logísticos", styles["H1X"]),
              para("Cada modelo es un AFD parcial M=(Q, Σ, δ, q0, F). Una transición omitida rechaza la cadena. Su AFD total equivalente añade un estado no final Pozo, dirige allí todos los pares ausentes y mantiene δ(Pozo,s)=Pozo para todo símbolo.", body),
              para("2.1 Pedido", styles["H2X"]),
              para("Q={Borrador, Confirmado, Reservado, Preparación, Empacado, Despachado, Entregado, Cancelado}; Σ={a,b,c,d,e,f,x}; q0=Borrador; F={Entregado, Cancelado}.", body),
              AutomataDiagram(["Borrador", "Confirmado", "Reservado", "Preparación", "Empacado", "Despachado", "Entregado"],
                              [("Borrador", "a", "Confirmado"), ("Confirmado", "b", "Reservado"),
                               ("Reservado", "c", "Preparación"), ("Preparación", "d", "Empacado"),
                               ("Empacado", "e", "Despachado"), ("Despachado", "f", "Entregado")], ["Entregado"]),
              para("La transición Reservado -x-> Cancelado libera el inventario y cancela como una operación atómica. También se permite cancelar desde Borrador y Confirmado. El despacho solo se alcanza después de reserva, preparación y empaque.", body),
              para("2.2 Reserva de inventario", styles["H2X"]),
              para("Q={Solicitada, Validada, Reservada, Consumida, Liberada, Rechazada, Expirada}; Σ={a,b,c,l,r,v}; q0=Solicitada; F={Consumida, Liberada, Rechazada, Expirada}. Expirada cierra una reserva confirmada cuyo plazo venció. No se consume desde Solicitada o Validada.", body),
              para("2.3 Orden de compra", styles["H2X"]),
              para("Q={Borrador, En aprobación, Aprobada, Enviada, Recepción parcial, Recibida, Rechazada}; Σ={a,p,e,r,c,x}; q0=Borrador; F={Recibida, Rechazada}. El evento r registra una o más recepciones parciales; c completa la recepción. Una orden no se envía sin aprobación ni después de ser rechazada.", body), PageBreak()]

    tests = [["AFD", "Cadena", "Resultado", "Justificación"],
             ["Pedido", "abcdef", "Acepta", "Flujo completo hasta Entregado"],
             ["Pedido", "abx", "Acepta", "Libera inventario y cancela desde Reservado"],
             ["Pedido", "vacía", "Rechaza", "Borrador no es final"],
             ["Pedido", "ae", "Rechaza", "Salto ilegal a despacho"],
             ["Pedido", "abcdefx", "Rechaza", "Sin eventos después del cierre"],
             ["Reserva", "abc / abl / abv", "Acepta", "Consumo, liberación o expiración"],
             ["Reserva", "ac / av", "Rechaza", "Falta confirmar la reserva"],
             ["Reserva", "abvc", "Rechaza", "Expirada es terminal"],
             ["Compra", "apec", "Acepta", "Recepción completa directa"],
             ["Compra", "aperc / aperrc", "Acepta", "Una o varias recepciones parciales"],
             ["Compra", "ae / xe", "Rechaza", "Sin aprobación / rechazo terminal"]]
    story += [para("2.4 Cadenas de validación", styles["H2X"]), table(tests, [2.1*cm, 2.4*cm, 2.0*cm, 9.6*cm], font=7.8),
              Spacer(1, 6), para("Las pruebas observaron los resultados esperados, validaron XML, determinismo, estados finales, alcanzabilidad y equivalencia con estado pozo. JFLAP 7.1 requiere ejecución manual mediante Input > Multiple Run; las capturas auténticas siguen pendientes.", body),
              para("3. Grafo ponderado y ruta AMR", styles["H1X"]),
              para("La planta es un grafo no dirigido con V={R,A,B,C,P,E,D}, once aristas y pesos no negativos en metros.", body), GraphDiagram(),
              para("Dijkstra usa distancias, predecesores y una cola de prioridad. La ruta destacada R-B-A-P-E-D cuesta 2+1+3+2+3=11 m. También es óptima R-B-A-E-D=11 m. La complejidad es O((V+E) log V) tiempo y O(V+E) espacio. Las pruebas cubren bloqueos, inalcanzabilidad, origen=destino, pesos inválidos y asimetría.", body), PageBreak()]

    story += [para("4. FEFO y reposición", styles["H1X"]),
              para("FEFO excluye lotes vencidos o sin stock, ordena por (fecha de vencimiento, código) y toma min(pendiente, disponible). Un lote que vence hoy es elegible. Ante stock insuficiente, devuelve un plan parcial informativo sin confirmar ni modificar la reserva. Tiempo O(L log L), espacio O(L).", body),
              table([["Lote", "Vence", "Disponible", "Selección para demanda 12"],
                     ["L000", "2026-11-22", "30", "Excluido: vencido"],
                     ["L001", "2026-11-25", "4", "4"],
                     ["L002", "2026-11-25", "5", "5"],
                     ["L003", "2026-12-10", "8", "3"]], [3.0*cm, 4.0*cm, 3.3*cm, 5.8*cm], font=8.2),
              Spacer(1, 8), para("Posición = disponible + en orden - reservado. Si posición <= mínimo, sugerencia=max(0, objetivo-posición). Con 18, 10, 5, 30 y 50, la posición es 23 y la sugerencia 27. Registrar 27 en órdenes abiertas lleva la posición a 50 y evita una segunda sugerencia secuencial. En producción se requiere una transacción o clave idempotente. Tiempo O(P).", body),
              para("5. Diez correos y complejidad", styles["H1X"]),
              para("P está contenido en NP. Para afirmar NP-completitud se justifican pertenencia a NP y NP-hardness. Los diez problemas sobre entradas finitas son decidibles y computables.", body)]
    cases = [["ID", "Problema", "Clase", "Búsqueda exacta", "Evidencia"],
             ["P1", "Alcanzabilidad", "P", "BFS O(V+E)", "Camino"],
             ["P2", "Ruta mínima", "P", "Dijkstra", "Ruta y peso"],
             ["P3", "Flujo máximo", "P", "Edmonds-Karp", "Flujo/corte"],
             ["N1", "Isomorfismo", "NP", "Permutaciones", "Bijección O(n²)"],
             ["N2", "Divisor acotado", "NP", "Hasta B", "d divide N"],
             ["N3", "Log discreto acotado", "NP", "Hasta B", "Exponente x"],
             ["N4", "Automorfismo", "NP", "Permutaciones", "Bijección no identidad"],
             ["C1", "3-SAT", "NP-completo", "DPLL", "SAT <=p 3-SAT"],
             ["C2", "TSP decisión", "NP-completo", "Tours", "HC <=p TSP"],
             ["C3", "Vertex Cover", "NP-completo", "Subconjuntos", "IS <=p VC"]]
    story += [table(cases, [1.0*cm, 4.0*cm, 2.7*cm, 4.0*cm, 4.5*cm], font=7.5),
              Spacer(1, 8), para("La instancia C1 tiene cláusulas de dos literales y pertenece a 2-SAT, resoluble en P; la NP-completitud corresponde a 3-SAT general. C2 es decisión con umbral, no optimización. C3 cubre corredores por sus extremos y por eso corresponde a Vertex Cover, no a Dominating Set.", body), PageBreak()]

    story += [para("6. Decidibilidad y problema de la parada", styles["H1X"]),
              para("Decidibilidad exige un algoritmo que termine para toda entrada válida y responda Sí o No. Computabilidad pregunta si existe un procedimiento efectivo que calcule una función. Complejidad mide tiempo y memoria en función del tamaño de entrada. Eficiencia práctica depende además del tamaño real y los recursos disponibles.", body),
              para("Vertex Cover es decidible enumerando 2^|V| subconjuntos, pero puede resultar impracticable. El problema general de la parada es distinto: no existe un decisor universal correcto para todo programa y toda entrada. No se trata de falta de tiempo o memoria.", body),
              para("7. Implementación y pruebas reproducibles", styles["H1X"]),
              para("La suite ejecutada el 25 de noviembre de 2026 contiene 46 métodos de prueba y terminó con OK. Se ejecutaron los tres módulos solicitados. La evidencia está en docs/evidencias/resultados_tests.txt.", body),
              para("python3 -m unittest discover -s tests -v<br/>python3 -m src.planta_amr<br/>python3 -m src.fefo_reposicion<br/>python3 -m src.correos", styles["CodeX"]),
              para("GitHub Actions ejecuta pruebas y demostraciones en Python 3.10, 3.11 y 3.12.", body),
              para("8. Gestión del proyecto", styles["H1X"]),
              para("El historial original contiene ocho commits técnicos atribuidos a Ariana. Main agregó planificación, issues y retrospectivas. La rama de finalización concilia esa evidencia, completa los AFD y prepara informe y presentación. GitHub rechazó el push de la cuenta autenticada de Jeanneth con 403; Ariana debe otorgarle permisos para fusionar PRs en el repositorio original.", body),
              para("Los sprints se organizan en: 1) autómatas y grafo, 2) Dijkstra, FEFO y reposición, 3) correos, integración, informe, presentación y release. Se propone v1.0.0, pero no se declara publicado.", body),
              para("9. Correspondencia con la rúbrica", styles["H1X"])]
    rubric = [["Criterio", "Puntos", "Evidencia / estado"],
              ["Autómatas y secuencias", "2,0", "JFF completos y pruebas; capturas pendientes"],
              ["Grafo y rutas", "1,5", "Dijkstra y dos óptimos de 11 m"],
              ["FEFO y reposición", "1,5", "Política, fórmula 23/27 y pruebas"],
              ["Decidibilidad y complejidad", "1,5", "Diez fichas, reducciones y parada"],
              ["Implementación y pruebas", "1,5", "46 pruebas y tres demos"],
              ["Gestión y versiones", "1,0", "Historial, sprints y versión propuesta"],
              ["Comunicación", "1,0", "Informe y presentación con guion"]]
    story += [table(rubric, [5.0*cm, 2.0*cm, 9.2*cm], font=8.1),
              para("10. Conclusiones", styles["H1X"]),
              para("Los procesos quedaron modelados sin saltos ilegales. El grafo confirma rutas óptimas de 11 m. FEFO y reposición distinguen cálculo de confirmación transaccional. Los diez casos muestran por qué buscar puede ser costoso aunque verificar sea polinómico. La suite respalda la implementación, pero no reemplaza las capturas reales de JFLAP ni la autorización de un release.", body),
              para("Referencias", styles["H1X"]),
              para("1. Equipo LOGISTPULSE. Informe previo del Deber 2, 2026.<br/>2. JFLAP 7.1: https://www.jflap.org/jflaptmp/<br/>3. Cormen et al., Introduction to Algorithms.<br/>4. Sipser, Introduction to the Theory of Computation.", small),
              para("Anexo: estado final y cierre manual", styles["H1X"]),
              para("Modelos: jflap/. Código: src/. Pruebas: tests/. Documentación: docs/. Fuente editable: informe/informe_final.tex. El PDF se genera de forma reproducible con scripts/generar_informe_pdf.py.", body),
              para("Evidencias JFLAP pendientes", styles["H2X"]),
              table([["Proceso", "Captura del diagrama", "Captura de Multiple Run"],
                     ["Pedido", "pedido_diagrama.png", "pedido_multiple_run.png"],
                     ["Reserva", "reserva_diagrama.png", "reserva_multiple_run.png"],
                     ["Compra", "compra_diagrama.png", "compra_multiple_run.png"]],
                    [3.0*cm, 6.5*cm, 6.5*cm], font=8.2),
              Spacer(1, 8), para("Abrir JFLAP 7.1 con java -jar JFLAP7.1.jar, cargar cada archivo .jff y ejecutar las cadenas documentadas en docs/automatas_jflap.md. Guardar únicamente capturas reales dentro de docs/evidencias/jflap/.", body),
              para("Estado de GitHub", styles["H2X"]),
              para("El PR #5 es técnicamente fusionable y sus fechas se incorporaron a esta rama, pero el intento de merge al repositorio original recibió HTTP 403. Los PR #4 y #6 no deben fusionarse sin corrección: #4 tiene conflicto y #6 afirma evidencia JFLAP ausente. Ariana debe conceder acceso o fusionar el PR de finalización desde su cuenta.", body),
              para("Cierre requerido", styles["H2X"]),
              para("1. Incorporar las seis capturas auténticas. 2. Revisar el PDF y la presentación. 3. Ejecutar la suite en la máquina del equipo. 4. Fusionar el PR autorizado. 5. Crear v1.0.0 y el release solo después de esas verificaciones.", body)]

    doc = BaseDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=2*cm, leftMargin=2*cm,
                          topMargin=2.0*cm, bottomMargin=1.8*cm,
                          title="LOGISTPULSE - Informe técnico final",
                          author="Ariana Muñoz y Jeanneth Cabascango")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")

    def page(canvas, document):
        canvas.saveState()
        if document.page > 1:
            canvas.setStrokeColor(colors.HexColor("#D3DCE3")); canvas.line(2*cm, A4[1]-1.4*cm, A4[0]-2*cm, A4[1]-1.4*cm)
            canvas.setFont("Helvetica-Bold", 8); canvas.setFillColor(AZUL); canvas.drawString(2*cm, A4[1]-1.1*cm, "LOGISTPULSE")
            canvas.setFont("Helvetica", 8); canvas.setFillColor(colors.HexColor("#607D8B")); canvas.drawRightString(A4[0]-2*cm, A4[1]-1.1*cm, "Teoría de la Computación")
        canvas.setFont("Helvetica", 8); canvas.setFillColor(colors.HexColor("#607D8B")); canvas.drawCentredString(A4[0]/2, 0.9*cm, str(document.page))
        canvas.restoreState()

    doc.addPageTemplates(PageTemplate(id="main", frames=frame, onPage=page))
    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    build()
