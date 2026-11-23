"""Pruebas normales, límites e inválidas para la fase B."""
import unittest
from src.planta_amr import construir_planta, dijkstra_amr, costo_ruta, ARISTAS_FIGURA

class TestPlantaAMR(unittest.TestCase):
    def setUp(self):
        self.g = construir_planta()

    def test_grafo_identico_figura(self):
        self.assertEqual(len(self.g),7)
        self.assertEqual(sum(map(len,self.g.values()))//2,len(ARISTAS_FIGURA))
        self.assertEqual(self.g['R']['B'],2)
        self.assertEqual(self.g['B']['A'],1)
        self.assertEqual(self.g['P']['E'],2)
        self.assertEqual(self.g['E']['D'],3)

    def test_ruta_minima(self):
        ruta,costo=dijkstra_amr(self.g,'R','D')
        self.assertEqual(costo,11)
        self.assertEqual(costo_ruta(self.g,ruta),11)
        self.assertEqual((ruta[0],ruta[-1]),('R','D'))

    def test_ruta_resaltada_enunciado(self):
        self.assertEqual(costo_ruta(self.g,['R','B','A','P','E','D']),11)

    def test_empate_dos_rutas(self):
        self.assertEqual(costo_ruta(self.g,['R','B','A','E','D']),11)

    def test_origen_igual_destino(self):
        self.assertEqual(dijkstra_amr(self.g,'R','R'),(['R'],0))

    def test_zona_bloqueada(self):
        ruta,costo=dijkstra_amr(self.g,'R','D',{'P'})
        self.assertNotIn('P',ruta)
        self.assertEqual(costo,11)

    def test_inaccesible(self):
        self.assertIsNone(dijkstra_amr(self.g,'R','D',{'A','B'}))

    def test_origen_inexistente(self):
        with self.assertRaisesRegex(ValueError,'inexistente'):
            dijkstra_amr(self.g,'X','D')

    def test_destino_bloqueado(self):
        with self.assertRaisesRegex(ValueError,'bloqueado'):
            dijkstra_amr(self.g,'R','D',{'D'})

    def test_peso_negativo(self):
        with self.assertRaisesRegex(ValueError,'no negativos'):
            construir_planta([('R','B',-1)])

    def test_grafo_asimetrico(self):
        with self.assertRaisesRegex(ValueError,'simétrico'):
            dijkstra_amr({'R':{'D':1},'D':{}},'R','D')

    def test_arista_duplicada(self):
        with self.assertRaisesRegex(ValueError,'duplicada'):
            construir_planta([('R','B',2),('B','R',2)])

if __name__ == '__main__':
    unittest.main()
