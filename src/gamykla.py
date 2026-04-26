"""Factory Method projektavimo sablonas."""

from src.algoritmai import (
    BurbuluRusiavimas,
    GreitasisRusiavimas,
    IterpimoRusiavimas,
)


class RusiuokliuGamykla:
    """Klase, kuri sukuria rusiuokliu objektus pagal pavadinima.

    Tai Factory Method projektavimo sablonas. Vietoj to, kad kode
    butu daug 'if/elif' saku, viskas surinkta vienoje vietoje.
    """

    # Visi galimi algoritmai surasyti zodyne.
    _algoritmai = {
        "burbulu": BurbuluRusiavimas,
        "greitasis": GreitasisRusiavimas,
        "iterpimo": IterpimoRusiavimas,
    }

    @classmethod
    def sukurti(cls, pavadinimas):
        """Sukuria ir grazina rusiuokli pagal pavadinima."""
        raktas = pavadinimas.lower().strip()
        if raktas not in cls._algoritmai:
            galimi = ", ".join(cls._algoritmai.keys())
            raise ValueError(
                f"Nezinomas algoritmas: '{pavadinimas}'. "
                f"Galimi: {galimi}."
            )
        # Sukuriame nauja konkretaus algoritmo objekta.
        klase = cls._algoritmai[raktas]
        return klase()

    @classmethod
    def galimi_algoritmai(cls):
        """Grazina visu galimu algoritmu pavadinimu sarasa."""
        return list(cls._algoritmai.keys())
