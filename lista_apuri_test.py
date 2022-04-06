import unittest
import lista_apuri
 
class Test_Lista_apuri(unittest.TestCase):
    def testaa_Parillisten_maara(self):
        list = [1,2,3,4]
        tulos = lista_apuri.parillisten_maara(list)
        self.assertEqual(tulos, 2)

    def testaa_Parittomien_maara(self):
        list = [1,2,3,4]
        tulos = lista_apuri.parittomien_maara(list)
        self.assertEqual(tulos, 2)

    def testaa_Negatiivisten_maara(self):
        list = [-1,2,3,4]
        tulos = lista_apuri.negatiivisten_maara(list)
        self.assertEqual(tulos, 1)
