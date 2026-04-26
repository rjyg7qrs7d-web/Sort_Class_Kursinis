"""Klase, kuri sujungia rusiuokli, duomenis ir failu tvarkykle."""

from src.failai import FailuTvarkykle
from src.rusiuoklis import Rusiuoklis


class Programa:
    """Programos pagrindine klase.

    Demonstruoja kompozicijos ir agregacijos principus:

    - KOMPOZICIJA: 'failu_tvarkykle' yra kompozicija - ji sukuriama
      pacioje klaseje (__init__ metode) ir egzistuoja tik kol
      egzistuoja Programa.

    - AGREGACIJA: 'rusiuoklis' yra agregacija - jis perduodamas is
      isores. Net jeigu Programa bus sunaikinta, rusiuoklis liks.
    """

    def __init__(self, rusiuoklis):
        # Agregacija: rusiuoklis ateina is isores.
        self._rusiuoklis = rusiuoklis
        # Kompozicija: failu tvarkykle sukuriama cia pat.
        self._failu_tvarkykle = FailuTvarkykle()
        # Vidinis duomenu sarasaas.
        self._duomenys = []

    def nustatyti_rusiuokli(self, rusiuoklis):
        """Pakeicia rusiavimo algoritma."""
        if not isinstance(rusiuoklis, Rusiuoklis):
            raise TypeError("Rusiuoklis turi paveldeti is Rusiuoklis klases.")
        self._rusiuoklis = rusiuoklis

    def nustatyti_duomenis(self, skaiciai):
        """Nustato duomenis is saraso."""
        # Saugome kopija, kad isorinis sarasaas nepaveiktu vidinio.
        self._duomenys = list(skaiciai)

    def gauti_duomenis(self):
        """Grazina dabartinius duomenis (kopija)."""
        return list(self._duomenys)

    def skaityti_is_failo(self, kelias):
        """Nuskaito duomenis is failo."""
        self._duomenys = self._failu_tvarkykle.skaityti(kelias)

    def rasyti_i_faila(self, kelias, skaiciai):
        """Iraso duotus skaicius i faila."""
        self._failu_tvarkykle.rasyti(kelias, skaiciai)

    def rusiuoti(self):
        """Surusiuoja duomenis ir grazina rezultata.

        Cia veikia polimorfizmas - 'rusiuoti' metodas iskvies tinkama
        algoritma priklausomai nuo to, koks rusiuoklis dabar nustatytas.
        """
        return self._rusiuoklis.rusiuoti(self._duomenys)

    def gauti_rusiuoklio_aprasyma(self):
        """Grazina dabartinio rusiuoklio aprasyma."""
        return self._rusiuoklis.aprasyti()

    def gauti_rusiuoklio_pavadinima(self):
        """Grazina dabartinio rusiuoklio pavadinima."""
        return self._rusiuoklis.pavadinimas
