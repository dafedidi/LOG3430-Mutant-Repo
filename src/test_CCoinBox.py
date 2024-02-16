import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):

    def test_pass(self):
        pass

    def test_monnaie(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        coinBox.ajouter_25c()
        self.assertEqual(coinBox.get_vente_permise(), True)

    def test_monnaie_Negative(self):
        coinBox = CCoinBox()
        coinBox.ajouter_25c()
        self.assertEqual(self.monnaie_courante, 1)