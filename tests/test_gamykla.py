"""Gamyklos klases testai."""

import unittest

from src.algoritmai import BurbuluRusiavimas, GreitasisRusiavimas
from src.gamykla import RusiuokliuGamykla


class TestRusiuokliuGamykla(unittest.TestCase):

    def setUp(self):
        self.gamykla = RusiuokliuGamykla()

    def test_sukurti_burbulu(self):
        rusiuoklis = self.gamykla.sukurti("burbulu")
        self.assertIsInstance(rusiuoklis, BurbuluRusiavimas)

    def test_sukurti_greitaji(self):
        rusiuoklis = self.gamykla.sukurti("greitasis")
        self.assertIsInstance(rusiuoklis, GreitasisRusiavimas)

    def test_didziosios_raides(self):
        rusiuoklis = self.gamykla.sukurti("BURBULU")
        self.assertIsInstance(rusiuoklis, BurbuluRusiavimas)

    def test_nezinomas_algoritmas(self):
        with self.assertRaises(ValueError):
            self.gamykla.sukurti("nezinomas")

    def test_galimu_algoritmu_sarasaas(self):
        galimi = self.gamykla.galimi_algoritmai()
        self.assertIn("burbulu", galimi)
        self.assertIn("greitasis", galimi)
        self.assertIn("iterpimo", galimi)


if __name__ == "__main__":
    unittest.main()
