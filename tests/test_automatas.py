"""Auditoría estructural y funcional de los tres DFA JFLAP."""
from collections import deque
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

ESPECIFICACIONES = {
    "pedido": {
        "estados": {"Borrador", "Confirmado", "Reservado", "Preparacion",
                    "Empacado", "Despachado", "Entregado", "Cancelado"},
        "inicial": "Borrador",
        "finales": {"Entregado", "Cancelado"},
        "alfabeto": set("abcdefx"),
        "casos": [
            ("abcdef", True, ["Borrador", "Confirmado", "Reservado", "Preparacion",
                               "Empacado", "Despachado", "Entregado"]),
            ("abx", True, ["Borrador", "Confirmado", "Reservado", "Cancelado"]),
            ("x", True, ["Borrador", "Cancelado"]),
            ("", False, ["Borrador"]),
            ("abcde", False, ["Borrador", "Confirmado", "Reservado", "Preparacion",
                                "Empacado", "Despachado"]),
            ("ae", False, ["Borrador", "Confirmado"]),
            ("abcdefx", False, ["Borrador", "Confirmado", "Reservado", "Preparacion",
                                  "Empacado", "Despachado", "Entregado"]),
        ],
    },
    "reserva": {
        "estados": {"Solicitada", "Validada", "Reservada", "Consumida", "Liberada",
                    "Rechazada", "Expirada"},
        "inicial": "Solicitada",
        "finales": {"Consumida", "Liberada", "Rechazada", "Expirada"},
        "alfabeto": set("abclrv"),
        "casos": [
            ("abc", True, ["Solicitada", "Validada", "Reservada", "Consumida"]),
            ("abl", True, ["Solicitada", "Validada", "Reservada", "Liberada"]),
            ("abv", True, ["Solicitada", "Validada", "Reservada", "Expirada"]),
            ("r", True, ["Solicitada", "Rechazada"]),
            ("", False, ["Solicitada"]),
            ("ac", False, ["Solicitada", "Validada"]),
            ("av", False, ["Solicitada", "Validada"]),
            ("abvc", False, ["Solicitada", "Validada", "Reservada", "Expirada"]),
        ],
    },
    "compra": {
        "estados": {"Borrador", "En aprobacion", "Aprobada", "Enviada",
                    "Recepcion parcial", "Recibida", "Rechazada"},
        "inicial": "Borrador",
        "finales": {"Recibida", "Rechazada"},
        "alfabeto": set("apecrx"),
        "casos": [
            ("apec", True, ["Borrador", "En aprobacion", "Aprobada", "Enviada", "Recibida"]),
            ("aperc", True, ["Borrador", "En aprobacion", "Aprobada", "Enviada",
                               "Recepcion parcial", "Recibida"]),
            ("aperrc", True, ["Borrador", "En aprobacion", "Aprobada", "Enviada",
                                "Recepcion parcial", "Recepcion parcial", "Recibida"]),
            ("ax", True, ["Borrador", "En aprobacion", "Rechazada"]),
            ("", False, ["Borrador"]),
            ("ae", False, ["Borrador", "En aprobacion"]),
            ("ap", False, ["Borrador", "En aprobacion", "Aprobada"]),
            ("xe", False, ["Borrador", "Rechazada"]),
        ],
    },
}


def cargar(nombre):
    ruta = ROOT / "jflap" / f"{nombre}.jff"
    tree = ET.parse(ruta)
    if tree.getroot().tag != "structure" or tree.findtext("./type") != "fa":
        raise ValueError("Estructura JFLAP inválida")
    auto = tree.find("./automaton")
    estados_xml = auto.findall("state")
    ids = {e.get("id") for e in estados_xml}
    nombres = {e.get("id"): e.get("name") for e in estados_xml}
    if None in ids or len(ids) != len(estados_xml) or len(set(nombres.values())) != len(nombres):
        raise ValueError("Identificadores o nombres de estado inválidos")
    iniciales = [e.get("id") for e in estados_xml if e.find("initial") is not None]
    finales = {e.get("id") for e in estados_xml if e.find("final") is not None}
    if len(iniciales) != 1 or not finales or not finales.issubset(ids):
        raise ValueError("Estados inicial/final inválidos")
    delta = {}
    for transicion in auto.findall("transition"):
        origen = transicion.findtext("from")
        destino = transicion.findtext("to")
        simbolo = transicion.findtext("read")
        if origen not in ids or destino not in ids or simbolo is None or len(simbolo) != 1:
            raise ValueError("Transición JFLAP inválida")
        if (origen, simbolo) in delta:
            raise ValueError("Autómata no determinista")
        delta[(origen, simbolo)] = destino
    return {"inicial": iniciales[0], "finales": finales, "delta": delta,
            "nombres": nombres, "estados": ids}


def ejecutar(modelo, palabra):
    actual = modelo["inicial"]
    traza = [modelo["nombres"][actual]]
    for simbolo in palabra:
        siguiente = modelo["delta"].get((actual, simbolo))
        if siguiente is None:
            return False, traza
        actual = siguiente
        traza.append(modelo["nombres"][actual])
    return actual in modelo["finales"], traza


class TestJFLAP(unittest.TestCase):
    def test_definicion_formal_exacta(self):
        for nombre, especificacion in ESPECIFICACIONES.items():
            with self.subTest(automata=nombre):
                modelo = cargar(nombre)
                self.assertEqual(set(modelo["nombres"].values()), especificacion["estados"])
                self.assertEqual(modelo["nombres"][modelo["inicial"]], especificacion["inicial"])
                self.assertEqual({modelo["nombres"][i] for i in modelo["finales"]},
                                 especificacion["finales"])
                self.assertEqual({simbolo for _, simbolo in modelo["delta"]},
                                 especificacion["alfabeto"])

    def test_todos_los_estados_son_alcanzables(self):
        for nombre in ESPECIFICACIONES:
            modelo = cargar(nombre)
            alcanzados = {modelo["inicial"]}
            cola = deque(alcanzados)
            while cola:
                origen = cola.popleft()
                for (u, _), destino in modelo["delta"].items():
                    if u == origen and destino not in alcanzados:
                        alcanzados.add(destino)
                        cola.append(destino)
            with self.subTest(automata=nombre):
                self.assertEqual(alcanzados, modelo["estados"])

    def test_cadenas_y_trazas(self):
        for nombre, especificacion in ESPECIFICACIONES.items():
            modelo = cargar(nombre)
            for entrada, esperado, traza in especificacion["casos"]:
                with self.subTest(automata=nombre, entrada=entrada):
                    observado, traza_observada = ejecutar(modelo, entrada)
                    self.assertEqual(observado, esperado)
                    self.assertEqual(traza_observada, traza)

    def test_dfa_parcial_equivale_a_total_con_pozo(self):
        for nombre, especificacion in ESPECIFICACIONES.items():
            modelo = cargar(nombre)
            faltantes = {(estado, simbolo) for estado in modelo["estados"]
                         for simbolo in especificacion["alfabeto"]
                         if (estado, simbolo) not in modelo["delta"]}
            with self.subTest(automata=nombre):
                self.assertTrue(faltantes)
                total = dict(modelo["delta"])
                total.update({par: "POZO" for par in faltantes})
                total.update({("POZO", simbolo): "POZO"
                              for simbolo in especificacion["alfabeto"]})
                self.assertEqual(len(total),
                                 (len(modelo["estados"]) + 1) * len(especificacion["alfabeto"]))


if __name__ == "__main__":
    unittest.main()
