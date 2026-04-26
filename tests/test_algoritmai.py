"""Algoritmu testai."""

import unittest

from src.algoritmai import (
    BurbuluRusiavimas,
    GreitasisRusiavimas,
    IterpimoRusiavimas,
)
from src.rusiuoklis import Rusiuoklis


class TestBurbuluRusiavimas(unittest.TestCase):

    def setUp(self):
        self.rusiuoklis = BurbuluRusiavimas()

    def test_tuscias_sarasaas(self):
        self.assertEqual(self.rusiuoklis.rusiuoti([]), [])

    def test_vienas_elementas(self):
        self.assertEqual(self.rusiuoklis.rusiuoti([5]), [5])

    def test_jau_surusiuotas(self):
        self.assertEqual(self.rusiuoklis.rusiuoti([1, 2, 3]), [1, 2, 3])

    def test_atvirksciai_surusiuotas(self):
        self.assertEqual(self.rusiuoklis.rusiuoti([5, 4, 3]), [3, 4, 5])

    def test_su_pasikartojimais(self):
        self.assertEqual(
            self.rusiuoklis.rusiuoti([3, 1, 2, 3, 1]),
            [1, 1, 2, 3, 3]
        )

    def test_neigiami_skaiciai(self):
        self.assertEqual(
            self.rusiuoklis.rusiuoti([-2, 5, -1, 0]),
            [-2, -1, 0, 5]
        )

    def test_pradinis_sarasaas_nepakeicimas(self):
        # Tikriname, kad pradinio saraso nepakeitiama.
        pradinis = [3, 1, 2]
        kopija = list(pradinis)
        self.rusiuoklis.rusiuoti(pradinis)
        self.assertEqual(pradinis, kopija)


class TestGreitasisRusiavimas(unittest.TestCase):

    def setUp(self):
        self.rusiuoklis = GreitasisRusiavimas()

    def test_tuscias(self):
        self.assertEqual(self.rusiuoklis.rusiuoti([]), [])

    def test_paprastas(self):
        self.assertEqual(
            self.rusiuoklis.rusiuoti([4, 2, 7, 1, 3]),
            [1, 2, 3, 4, 7]
        )

    def test_neigiami(self):
        self.assertEqual(
            self.rusiuoklis.rusiuoti([-3, 0, 5, -1]),
            [-3, -1, 0, 5]
        )


class TestIterpimoRusiavimas(unittest.TestCase):

    def setUp(self):
        self.rusiuoklis = IterpimoRusiavimas()

    def test_paprastas(self):
        self.assertEqual(
            self.rusiuoklis.rusiuoti([5, 2, 8, 1]),
            [1, 2, 5, 8]
        )

    def test_su_pasikartojimais(self):
        self.assertEqual(
            self.rusiuoklis.rusiuoti([2, 1, 2, 1]),
            [1, 1, 2, 2]
        )


class TestAbstrakciaiKlasei(unittest.TestCase):

    def test_negalima_sukurti_abstrakcios(self):
        # Tikriname, kad abstrakcios klases negalima sukurti tiesiogiai.
        with self.assertRaises(TypeError):
            Rusiuoklis("bandymas")

    def test_pavadinimas(self):
        rusiuoklis = BurbuluRusiavimas()
        self.assertEqual(rusiuoklis.pavadinimas, "Burbulu rusiavimas")

    def test_aprasymas_skiriasi(self):
        # Polimorfizmo testas - kiekvienas algoritmas turi savo aprasyma.
        a = BurbuluRusiavimas().aprasyti()
        b = GreitasisRusiavimas().aprasyti()
        self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main()
