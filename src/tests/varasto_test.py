import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto1 = Varasto(-10)
        self.varasto2 = Varasto(10,-10)        
        self.varasto3 = Varasto(10,20)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
        
    def test_konstruktori_vaara_alkusaldo(self):
        self.assertAlmostEqual(self.varasto2.saldo, 0)
        
    def test_konstruktori_ylitaysi(self):
        self.assertAlmostEqual(self.varasto3.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        
    def test_konstruktori_vaara_tilavuus(self):
        self.assertAlmostEqual(self.varasto1.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)
        
    def test_neg_lisays(self):    
        self.varasto2.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto2.saldo, 0)
        
    def test_liikalisays(self):
        self.varasto2.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto2.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)
        
        saatu_maara1 = self.varasto1.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara1, 0)
        
        saatu_maara3 = self.varasto3.ota_varastosta(12)
        self.assertAlmostEqual(saatu_maara3, 10)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_printoutput(self):
        self.assertEqual(str(self.varasto3), "saldo = 10, vielä tilaa 0")
        