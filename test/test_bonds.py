from unittest import TestCase

from fda.bonds import bond_price, bond_ytm, bond_convexity, bond_mod_duration

class TestBonds(TestCase):

    def test_bond_price(self):
        ytm = bond_ytm(95.0428, 100, 1.5, 5.75, 2)
        price = bond_price(100, 1.5, ytm, 5.75, 2)
        self.assertAlmostEqual(price, 95.04279)
