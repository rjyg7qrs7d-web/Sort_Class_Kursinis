"""Failu tvarkykles testai."""

import os
import tempfile
import unittest

from src.failai import FailuTvarkykle


class TestFailuTvarkykle(unittest.TestCase):

    def setUp(self):
        # Sukuriame laikinaja direktorija testams.
        self.tvarkykle = FailuTvarkykle()
        self.aplankas = tempfile.mkdtemp()

    def tearDown(self):
        # Po testu istriname visus failus.
        for failas in os.listdir(self.aplankas):
            os.remove(os.path.join(self.aplankas, failas))
        os.rmdir(self.aplankas)

    def test_skaityti_txt(self):
        kelias = os.path.join(self.aplankas, "test.txt")
        with open(kelias, "w") as f:
            f.write("1 2 3 4 5")
        rezultatas = self.tvarkykle.skaityti(kelias)
        self.assertEqual(rezultatas, [1, 2, 3, 4, 5])

    def test_skaityti_csv(self):
        kelias = os.path.join(self.aplankas, "test.csv")
        with open(kelias, "w") as f:
            f.write("10,20,30")
        rezultatas = self.tvarkykle.skaityti(kelias)
        self.assertEqual(rezultatas, [10, 20, 30])

    def test_rasyti_ir_skaityti_txt(self):
        kelias = os.path.join(self.aplankas, "test.txt")
        self.tvarkykle.rasyti(kelias, [5, 3, 1])
        rezultatas = self.tvarkykle.skaityti(kelias)
        self.assertEqual(rezultatas, [5, 3, 1])

    def test_rasyti_ir_skaityti_csv(self):
        kelias = os.path.join(self.aplankas, "test.csv")
        self.tvarkykle.rasyti(kelias, [7, 8, 9])
        rezultatas = self.tvarkykle.skaityti(kelias)
        self.assertEqual(rezultatas, [7, 8, 9])

    def test_failas_nerastas(self):
        with self.assertRaises(FileNotFoundError):
            self.tvarkykle.skaityti("/nieko/nera.txt")

    def test_blogas_pletinys(self):
        kelias = os.path.join(self.aplankas, "test.json")
        with open(kelias, "w") as f:
            f.write("[1,2,3]")
        with self.assertRaises(ValueError):
            self.tvarkykle.skaityti(kelias)


if __name__ == "__main__":
    unittest.main()
