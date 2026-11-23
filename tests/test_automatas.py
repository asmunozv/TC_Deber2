"""Valida sintaxis JFLAP y doce secuencias exigidas por la rúbrica."""
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PRUEBAS = {
    "pedido": [("abcdef", True), ("ax", True), ("e", False), ("ae", False), ("a", False)],
    "reserva": [("abc", True), ("abl", True), ("c", False), ("ac", False)],
    "compra": [("aer", True), ("ax", True), ("xe", False), ("e", False)],
}

def cargar(nombre):
    tree = ET.parse(ROOT / "jflap" / (nombre + ".jff"))
    assert tree.findtext("./type") == "fa"
    auto = tree.find("./automaton")
    estados = auto.findall("state")
    ids = {e.get("id") for e in estados}
    inicial = [e.get("id") for e in estados if e.find("initial") is not None]
    finales = {e.get("id") for e in estados if e.find("final") is not None}
    if len(inicial) != 1 or not finales or not finales.issubset(ids):
        raise ValueError("Estados inicial/final inválidos")
    delta = {}
    for t in auto.findall("transition"):
        orig, dest = t.findtext("from"), t.findtext("to")
        sim = t.findtext("read")
        if orig not in ids or dest not in ids or sim is None or len(sim) != 1:
            raise ValueError("Transición JFLAP inválida")
        if (orig, sim) in delta:
            raise ValueError("No determinista")
        delta[(orig, sim)] = dest
    return inicial[0], finales, delta

def acepta(modelo, palabra):
    actual, finales, delta = modelo
    for simbolo in palabra:
        actual = delta.get((actual, simbolo))
        if actual is None:
            return False
    return actual in finales

class TestJFLAP(unittest.TestCase):
    def test_docean_pruebas_y_transiciones(self):
        for nombre, casos in PRUEBAS.items():
            modelo = cargar(nombre)
            for entrada, esperado in casos:
                with self.subTest(automata=nombre, entrada=entrada):
                    self.assertEqual(acepta(modelo, entrada), esperado)

    def test_sin_transiciones_epsilon(self):
        for nombre in PRUEBAS:
            _, _, delta = cargar(nombre)
            self.assertTrue(all(len(sim) == 1 for _, sim in delta))

if __name__ == "__main__":
    unittest.main()
