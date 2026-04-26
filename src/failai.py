"""Failu skaitymas ir rasymas."""

import csv
import os


class FailuTvarkykle:
    """Klase, kuri skaito ir raso skaicius is/i .txt arba .csv failus."""

    def skaityti(self, kelias):
        """Nuskaito skaicius is failo ir grazina sarasa.

        Palaikomi formatai: .txt (skaiciai atskirti tarpais)
        ir .csv (skaiciai atskirti kableliais).
        """
        if not os.path.isfile(kelias):
            raise FileNotFoundError(f"Failas nerastas: {kelias}")

        # Nustatome failo formata pagal pletini.
        pletinys = os.path.splitext(kelias)[1].lower()
        skaiciai = []

        if pletinys == ".txt":
            with open(kelias, "r", encoding="utf-8") as f:
                tekstas = f.read()
                for zodis in tekstas.split():
                    skaiciai.append(int(zodis))

        elif pletinys == ".csv":
            with open(kelias, "r", encoding="utf-8") as f:
                skaitytojas = csv.reader(f)
                for eilute in skaitytojas:
                    for reiksme in eilute:
                        reiksme = reiksme.strip()
                        if reiksme:
                            skaiciai.append(int(reiksme))
        else:
            raise ValueError(
                f"Nepalaikomas failo formatas: '{pletinys}'. "
                f"Galima naudoti: .txt arba .csv."
            )

        return skaiciai

    def rasyti(self, kelias, skaiciai):
        """Iraso skaicius i .txt arba .csv faila."""
        pletinys = os.path.splitext(kelias)[1].lower()

        if pletinys == ".txt":
            with open(kelias, "w", encoding="utf-8") as f:
                for skaicius in skaiciai:
                    f.write(f"{skaicius}\n")

        elif pletinys == ".csv":
            with open(kelias, "w", encoding="utf-8", newline="") as f:
                rasytojas = csv.writer(f)
                rasytojas.writerow(skaiciai)
        else:
            raise ValueError(
                f"Nepalaikomas failo formatas: '{pletinys}'. "
                f"Galima naudoti: .txt arba .csv."
            )
