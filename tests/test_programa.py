"""Programos klases testai."""

import unittest

from src.algoritmai import BurbuluRusiavimas, GreitasisRusiavimas
from src.programa import Programa


class TestPrograma(unittest.TestCase):

    def test_pradine_busena(self):
        programa = Programa(BurbuluRusiavimas())
        self.assertEqual(programa.gauti_duomenis(), [])

    def test_rusiavimas(self):
        programa = Programa(BurbuluRusiavimas())
        programa.nustatyti_duomenis([3, 1, 2])
        rezultatas = programa.rusiuoti()
        self.assertEqual(rezultatas, [1, 2, 3])

    def test_keisti_algoritma(self):
        programa = Programa(BurbuluRusiavimas())
        programa.nustatyti_duomenis([5, 2, 4])
        programa.nustatyti_rusiuokli(GreitasisRusiavimas())
        rezultatas = programa.rusiuoti()
        self.assertEqual(rezultatas, [2, 4, 5])

    def test_blogas_rusiuoklio_tipas(self):
        programa = Programa(BurbuluRusiavimas())
        with self.assertRaises(TypeError):
            programa.nustatyti_rusiuokli("ne rusiuoklis")

    def test_duomenu_kopija(self):
        # Tikriname, kad gauti_duomenis grazina kopija.
        programa = Programa(BurbuluRusiavimas())
        programa.nustatyti_duomenis([1, 2, 3])
        gauti = programa.gauti_duomenis()
        gauti.append(99)
        # Vidinis sarasaas neturi pasikeisti.
        self.assertEqual(programa.gauti_duomenis(), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
