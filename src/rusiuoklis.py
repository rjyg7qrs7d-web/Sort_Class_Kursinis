"""Abstrakti rusiuoklio klase."""

from abc import ABC, abstractmethod


class Rusiuoklis(ABC):
    """Bendra visu rusiavimo algoritmu klase.

    Si klase yra abstrakti - jos negalima sukurti tiesiogiai. Visi
    konkretus algoritmai (BurbuluRusiavimas, GreitasisRusiavimas)
    turi paveldeti is sios klases ir aprasyti metoda 'rusiuoti'.
    """

    def __init__(self, pavadinimas):
        # Pavadinimas saugomas su pabraukimu - tai inkapsuliacija.
        # Is isores ji galima skaityti tik per savybe (property).
        self._pavadinimas = pavadinimas

    @property
    def pavadinimas(self):
        """Grazina algoritmo pavadinima."""
        return self._pavadinimas

    @abstractmethod
    def rusiuoti(self, sarasas):
        """Surusiuoja sarasa didejimo tvarka ir grazina nauja sarasa.

        Sis metodas yra abstraktus - kiekvienas paveldetojas privalo ji
        aprasyti savo budu.
        """
        pass

    def aprasyti(self):
        """Grazina trumpa algoritmo aprasyma.

        Sis metodas yra polimorfinis - paveldetojai gali ji perrasyti.
        """
        return f"{self._pavadinimas}: bendras rusiavimo algoritmas."
