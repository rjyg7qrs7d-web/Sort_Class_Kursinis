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
    algoritmai = {
        "burbulu": BurbuluRusiavimas,
        "greitasis": GreitasisRusiavimas,
        "iterpimo": IterpimoRusiavimas,
    }

    def sukurti(self, pavadinimas):
        """Sukuria ir grazina rusiuokli pagal pavadinima."""
        raktas = pavadinimas.lower().strip()
        if raktas not in self.algoritmai:
            galimi = ", ".join(self.algoritmai.keys())
            raise ValueError(
                f"Nezinomas algoritmas: '{pavadinimas}'. "
                f"Galimi: {galimi}."
            )
        # Sukuriame nauja konkretaus algoritmo objekta.
        klase = self.algoritmai[raktas]
        return klase()

    def galimi_algoritmai(self):
        """Grazina visu galimu algoritmu pavadinimu sarasa."""
        return list(self.algoritmai.keys())
