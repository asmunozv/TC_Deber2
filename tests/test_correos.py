import unittest
from src import correos as c


class TestCorreos(unittest.TestCase):
    def test_p1(self):
        g = {"Durán":["Quito"], "Quito":["Norte"], "Norte":[], "Sur":[]}
        self.assertEqual(c.bfs_camino(g,"Durán","Norte"),["Durán","Quito","Norte"])
        self.assertIsNone(c.bfs_camino(g,"Sur","Norte"))
        self.assertEqual(c.bfs_camino(g,"Durán","Durán"),["Durán"])
        with self.assertRaises(ValueError): c.bfs_camino(g,"NoExiste","Norte")

    def test_p2(self):
        g = {"Quito":[("Latacunga",2),("Ambato",5)],"Latacunga":[("Guayaquil",6)],"Ambato":[("Guayaquil",3)],"Guayaquil":[]}
        self.assertEqual(c.dijkstra(g,"Quito","Guayaquil")[1],8)
        self.assertIsNone(c.dijkstra(g,"Guayaquil","Quito"))
        self.assertEqual(c.dijkstra(g,"Quito","Quito"),(["Quito"],0))
        with self.assertRaises(ValueError): c.dijkstra({"A":[("B",-1)],"B":[]},"A","B")

    def test_p3(self):
        g={"Planta":{"Quito":7,"Guayaquil":5},"Quito":{"Clientes":4,"Guayaquil":2},"Guayaquil":{"Clientes":6},"Clientes":{}}
        flujo, aumentos = c.flujo_maximo(g,"Planta","Clientes")
        self.assertEqual(flujo,10)
        self.assertEqual(sum(x[1] for x in aumentos),10)
        self.assertEqual(c.flujo_maximo({"A":{"B":0},"B":{}},"A","B")[0],0)
        with self.assertRaises(ValueError): c.flujo_maximo({"A":{"B":-1},"B":{}},"A","B")

    def test_n1(self):
        a=[[0,1,0],[1,0,1],[0,1,0]]
        b=[[0,1,1],[1,0,0],[1,0,0]]
        p=c.buscar_isomorfismo(a,b)
        self.assertTrue(c.verificar_isomorfismo(a,b,p))
        self.assertFalse(c.verificar_isomorfismo(a,b,(0,0,2)))
        self.assertIsNone(c.buscar_isomorfismo(a,[[0,1,1],[1,0,1],[1,1,0]]))

    def test_n2(self):
        self.assertEqual(c.buscar_factor(91,10),7)
        self.assertTrue(c.verificar_factor(91,10,7))
        self.assertFalse(c.verificar_factor(91,10,13))
        self.assertIsNone(c.buscar_factor(91,6))
        self.assertEqual(c.buscar_factor(4,2),2)
        with self.assertRaises(ValueError): c.buscar_factor(91,-1)

    def test_n3(self):
        self.assertEqual(c.buscar_exponente(23,5,8,10),6)
        self.assertTrue(c.verificar_exponente(23,5,8,10,6))
        self.assertFalse(c.verificar_exponente(23,5,8,5,6))
        self.assertIsNone(c.buscar_exponente(23,5,8,5))
        self.assertEqual(c.buscar_exponente(23,5,1,0),0)
        with self.assertRaises(ValueError): c.buscar_exponente(23,5,8,-1)

    def test_n4(self):
        tri=[[0,1,1],[1,0,1],[1,1,0]]
        p=c.buscar_automorfismo(tri)
        self.assertTrue(c.verificar_automorfismo(tri,p))
        self.assertTrue(c.verificar_automorfismo(tri,(1,0,2)))
        self.assertFalse(c.verificar_automorfismo(tri,(0,1,2)))
        self.assertIsNone(c.buscar_automorfismo([[0]]))
        with self.assertRaises(ValueError): c.buscar_automorfismo([[0,1],[0,0,1]])

    def test_c1(self):
        f=[[1,-2],[2,3]]
        sol=c.dpll(f,3)
        self.assertTrue(c.verificar_sat(f,3,sol))
        self.assertTrue(c.verificar_sat(f,3,{1:True,2:True,3:False}))
        self.assertIsNone(c.dpll([[1],[-1]],1))
        self.assertEqual(c.dpll([],0),{})
        self.assertFalse(c.verificar_sat(f,3,{1:False,2:True,3:False}))
        with self.assertRaises(ValueError): c.dpll([[4]],3)

    def test_c2(self):
        d=[[0,4,8],[4,0,3],[8,3,0]]
        self.assertEqual(c.buscar_tsp(d,20),((0,1,2,0),15))
        self.assertTrue(c.verificar_tsp(d,20,(0,1,2,0)))
        self.assertIsNone(c.buscar_tsp(d,14))
        self.assertFalse(c.verificar_tsp(d,20,(0,1,1,0)))
        self.assertEqual(c.buscar_tsp([[0,5],[5,0]],10),((0,1,0),10))
        with self.assertRaises(ValueError): c.buscar_tsp([[0,-3],[-3,0]],10)

    def test_c3(self):
        g={"A":["B"],"B":["A","C"],"C":["B"]}
        self.assertEqual(c.buscar_cobertura(g,1),{"B"})
        self.assertTrue(c.verificar_cobertura(g,1,{"B"}))
        self.assertFalse(c.verificar_cobertura(g,1,{"A"}))
        self.assertIsNone(c.buscar_cobertura(g,0))
        self.assertEqual(c.buscar_cobertura({"A":[],"B":[]},0),set())
        with self.assertRaises(ValueError): c.buscar_cobertura({"A":["B"],"B":[]},1)


if __name__ == "__main__":
    unittest.main()
