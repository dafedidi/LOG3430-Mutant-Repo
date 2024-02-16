import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def test_ajouter_25c(self):
        c = CCoinBox()
        c.ajouter_25c()
        self.assertEqual(c.get_monnaie_courante(), 1)
        self.assertEqual(c.get_vente_permise(), True)
        print("test_ajouter_25c() passed")