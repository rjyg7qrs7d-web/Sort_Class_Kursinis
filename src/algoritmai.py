"""Konkretus rusiavimo algoritmai."""

from src.rusiuoklis import Rusiuoklis


class BurbuluRusiavimas(Rusiuoklis):
    """Burbulu rusiavimas - paprastas, bet letas algoritmas."""

    def __init__(self):
        super().__init__("Burbulu rusiavimas")

    def rusiuoti(self, sarasas):
        # Dirbame su kopija, kad nepakeistume pradinio sarasoso.
        sarasas = list(sarasas)
        n = len(sarasas)
        for i in range(n):
            for j in range(0, n - i - 1):
                if sarasas[j] > sarasas[j + 1]:
                    sarasas[j], sarasas[j + 1] = sarasas[j + 1], sarasas[j]
        return sarasas

    def aprasyti(self):
        return ("Burbulu rusiavimas: gretimi elementai lyginami ir, "
                "jei reikia, sukeiciami vietomis. Sudetingumas: O(n^2).")


class GreitasisRusiavimas(Rusiuoklis):
    """Greitasis rusiavimas (QuickSort) - efektyvus algoritmas."""

    def __init__(self):
        super().__init__("Greitasis rusiavimas")

    def rusiuoti(self, sarasas):
        sarasas = list(sarasas)
        self._rusiuoti_dali(sarasas, 0, len(sarasas) - 1)
        return sarasas

    def _rusiuoti_dali(self, sarasas, pradzia, pabaiga):
        # Privatus metodas (pradedame pabraukimu).
        if pradzia < pabaiga:
            riba = self._padalinti(sarasas, pradzia, pabaiga)
            self._rusiuoti_dali(sarasas, pradzia, riba - 1)
            self._rusiuoti_dali(sarasas, riba + 1, pabaiga)

    def _padalinti(self, sarasas, pradzia, pabaiga):
        atrama = sarasas[pabaiga]
        i = pradzia - 1
        for j in range(pradzia, pabaiga):
            if sarasas[j] <= atrama:
                i += 1
                sarasas[i], sarasas[j] = sarasas[j], sarasas[i]
        sarasas[i + 1], sarasas[pabaiga] = sarasas[pabaiga], sarasas[i + 1]
        return i + 1

    def aprasyti(self):
        return ("Greitasis rusiavimas: pasirenkamas atramos elementas, "
                "sarasaas padalinamas i dvi dalis ir kiekviena dalis "
                "rusiuojama atskirai. Sudetingumas: O(n log n).")


class IterpimoRusiavimas(Rusiuoklis):
    """Iterpimo rusiavimas - tinka mazyciams sarasaams."""

    def __init__(self):
        super().__init__("Iterpimo rusiavimas")

    def rusiuoti(self, sarasas):
        sarasas = list(sarasas)
        for i in range(1, len(sarasas)):
            esamas = sarasas[i]
            j = i - 1
            while j >= 0 and sarasas[j] > esamas:
                sarasas[j + 1] = sarasas[j]
                j -= 1
            sarasas[j + 1] = esamas
        return sarasas

    def aprasyti(self):
        return ("Iterpimo rusiavimas: kiekvienas elementas iterpiamas i "
                "tinkama vieta jau surusiuotoje dalyje. "
                "Sudetingumas: O(n^2).")
