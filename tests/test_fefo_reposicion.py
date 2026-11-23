"""Pruebas reproducibles de FEFO y reposición."""
import copy
import unittest
from src.fefo_reposicion import seleccionar_fefo, sugerir_reposicion, registrar_sugerencias


class TestFEFO(unittest.TestCase):
    def setUp(self):
        self.lotes = [
            {'codigo':'L003','vencimiento':'2026-12-10','disponible':8},
            {'codigo':'L002','vencimiento':'2026-11-25','disponible':5},
            {'codigo':'L001','vencimiento':'2026-11-25','disponible':4},
            {'codigo':'L000','vencimiento':'2026-11-22','disponible':30},
        ]

    def test_fefo_orden_fecha_codigo(self):
        r = seleccionar_fefo(self.lotes, 12, '2026-11-23')
        self.assertEqual(r['estado'], 'OK')
        self.assertEqual(r['plan'], [
            {'codigo':'L001','cantidad':4},
            {'codigo':'L002','cantidad':5},
            {'codigo':'L003','cantidad':3}])

    def test_excluye_vencidos_y_cantidad_cero(self):
        r = seleccionar_fefo([
            {'codigo':'V','vencimiento':'2026-11-22','disponible':100},
            {'codigo':'Z','vencimiento':'2026-11-25','disponible':0},
            {'codigo':'A','vencimiento':'2026-11-25','disponible':1},
        ], 1, '2026-11-23')
        self.assertEqual(r['plan'], [{'codigo':'A','cantidad':1}])

    def test_stock_insuficiente_sin_reserva_parcial(self):
        r = seleccionar_fefo(self.lotes, 25, '2026-11-23')
        self.assertEqual(r['estado'], 'STOCK_INSUFICIENTE')
        self.assertEqual(r['pendiente'], 8)
        self.assertFalse(r['reserva_confirmada'])
        self.assertEqual(sum(item['cantidad'] for item in r['plan']), 17)

    def test_cantidad_cero(self):
        r = seleccionar_fefo(self.lotes, 0, '2026-11-23')
        self.assertEqual((r['estado'],r['plan']), ('OK', []))

    def test_vencimiento_hoy_elegible(self):
        r = seleccionar_fefo([
            {'codigo':'HOY','vencimiento':'2026-11-23','disponible':3}
        ], 3, '2026-11-23')
        self.assertEqual(r['plan'], [{'codigo':'HOY','cantidad':3}])

    def test_no_modifica_entrada(self):
        antes = copy.deepcopy(self.lotes)
        seleccionar_fefo(self.lotes, 12, '2026-11-23')
        self.assertEqual(antes,self.lotes)

    def test_fecha_invalida(self):
        with self.assertRaises(ValueError):
            seleccionar_fefo(self.lotes, 1, '23/11/2026')

    def test_codigo_duplicado(self):
        with self.assertRaises(ValueError):
            seleccionar_fefo(self.lotes + [self.lotes[0]], 1, '2026-11-23')

    def test_negativa(self):
        with self.assertRaises(ValueError):
            seleccionar_fefo(self.lotes, -2, '2026-11-23')


class TestReposicion(unittest.TestCase):
    def setUp(self):
        self.productos = [
            {'sku':'SKU-001','disponible':18,'en_orden':10,
             'reservado':5,'minimo':30,'objetivo':50}
        ]

    def test_ejemplo_enunciado(self):
        self.assertEqual(sugerir_reposicion(self.productos),
                         [{'sku':'SKU-001','posicion':23,'sugerencia':27}])

    def test_no_reponer_por_encima_minimo(self):
        datos = [{**self.productos[0], 'disponible':40}]
        self.assertEqual(sugerir_reposicion(datos)[0]['sugerencia'], 0)

    def test_igual_minimo(self):
        datos = [{**self.productos[0], 'disponible':25}]
        self.assertEqual(sugerir_reposicion(datos)[0]['posicion'], 30)
        self.assertEqual(sugerir_reposicion(datos)[0]['sugerencia'], 20)

    def test_orden_abierta_previa(self):
        datos = [{**self.productos[0], 'en_orden':40}]
        self.assertEqual(sugerir_reposicion(datos)[0]['sugerencia'], 0)

    def test_sin_duplicar_orden(self):
        antes = copy.deepcopy(self.productos)
        nuevo, ordenes = registrar_sugerencias(self.productos)
        self.assertEqual(ordenes, [{'sku':'SKU-001','cantidad':27}])
        self.assertEqual(nuevo[0]['en_orden'], 37)
        self.assertEqual(self.productos, antes)
        siguiente, repetidas = registrar_sugerencias(nuevo)
        self.assertEqual(repetidas, [])
        self.assertEqual(siguiente, nuevo)

    def test_lista_vacia(self):
        self.assertEqual(sugerir_reposicion([]), [])
        self.assertEqual(registrar_sugerencias([]), ([],[]))

    def test_varios_skus(self):
        datos = self.productos + [
            {'sku':'SKU-002','disponible':100,'en_orden':0,
             'reservado':0,'minimo':10,'objetivo':20}]
        r = sugerir_reposicion(datos)
        self.assertEqual([x['sugerencia'] for x in r],[27,0])

    def test_sku_duplicado(self):
        with self.assertRaises(ValueError):
            sugerir_reposicion(self.productos + self.productos)

    def test_entrada_negativa(self):
        with self.assertRaises(ValueError):
            sugerir_reposicion([{**self.productos[0],'en_orden':-1}])

    def test_objetivo_invalido(self):
        with self.assertRaises(ValueError):
            sugerir_reposicion([{**self.productos[0],'objetivo':10}])

    def test_reservado_supera_fisico(self):
        with self.assertRaises(ValueError):
            sugerir_reposicion([{**self.productos[0],'reservado':100}])

if __name__ == '__main__':
    unittest.main()
