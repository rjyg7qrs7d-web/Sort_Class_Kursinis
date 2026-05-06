"""Pagrindinis programos paleidimo failas."""

from src.gamykla import RusiuokliuGamykla
from src.programa import Programa


def parodyti_meniu():
    """Atspausdina meniu su pasirinkimais."""
    print()
    print("=" * 50)
    print(" Rusiavimo algoritmu programa")
    print("=" * 50)
    print(" 1. Skaityti skaicius is failo")
    print(" 2. Ivesti skaicius ranka")
    print(" 3. Parodyti dabartinius duomenis")
    print(" 4. Pasirinkti rusiavimo algoritma")
    print(" 5. Surusiuoti")
    print(" 6. Irasyti rezultata i faila")
    print(" 7. Parodyti algoritmo aprasyma")
    print(" 0. Iseiti")
    print("=" * 50)


def skaityti_is_failo(programa):
    """Nuskaito skaicius is vartotojo nurodyto failo."""
    kelias = input("Failo kelias (.txt arba .csv): ").strip()
    try:
        programa.skaityti_is_failo(kelias)
        skaicius = len(programa.gauti_duomenis())
        print(f"Nuskaityta {skaicius} skaiciu.")
    except (FileNotFoundError, ValueError) as klaida:
        print(f"Klaida: {klaida}")


def ivesti_ranka(programa):
    """Leidzia vartotojui ivesti skaicius ranka."""
    tekstas = input("Iveskite skaicius, atskirtus tarpais: ").strip()
    try:
        skaiciai = [int(x) for x in tekstas.split()]
        programa.nustatyti_duomenis(skaiciai)
        print(f"Iraseta {len(skaiciai)} skaiciu.")
    except ValueError:
        print("Klaida: ivedete ne skaicius.")


def parodyti_duomenis(programa):
    """Parodo dabartinius duomenis."""
    duomenys = programa.gauti_duomenis()
    if not duomenys:
        print("Duomenu nera.")
    else:
        print(f"Duomenys ({len(duomenys)}): {duomenys}")


def pasirinkti_algoritma(programa):
    """Leidzia vartotojui pasirinkti rusiavimo algoritma."""
    gamykla = RusiuokliuGamykla()
    galimi = gamykla.galimi_algoritmai()
    print("Galimi algoritmai:")
    for i, vardas in enumerate(galimi, 1):
        print(f"  {i}. {vardas}")
    pasirinkimas = input("Iveskite pavadinima: ").strip()
    try:
        rusiuoklis = gamykla.sukurti(pasirinkimas)
        programa.nustatyti_rusiuokli(rusiuoklis)
        print(f"Pasirinktas: {rusiuoklis.pavadinimas}")
    except ValueError as klaida:
        print(f"Klaida: {klaida}")


def surusiuoti(programa):
    """Surusiuoja duomenis ir parodo rezultata."""
    if not programa.gauti_duomenis():
        print("Pirma ikelkite duomenis.")
        return
    rezultatas = programa.rusiuoti()
    print(f"Algoritmas: {programa.gauti_rusiuoklio_pavadinima()}")
    print(f"Rezultatas: {rezultatas}")


def irasyti_i_faila(programa):
    """Irasyti rezultata i faila."""
    duomenys = programa.gauti_duomenis()
    if not duomenys:
        print("Duomenu nera.")
        return
    rezultatas = programa.rusiuoti()
    kelias = input("Failo kelias (.txt arba .csv): ").strip()
    try:
        programa.rasyti_i_faila(kelias, rezultatas)
        print(f"Rezultatas irasytas i {kelias}")
    except ValueError as klaida:
        print(f"Klaida: {klaida}")


def parodyti_aprasyma(programa):
    """Parodo dabartinio algoritmo aprasyma."""
    print(programa.gauti_rusiuoklio_aprasyma())


def main():
    """Pagrindine programos funkcija."""
    # Pradzioje nustatome numatytaji algoritma.
    gamykla = RusiuokliuGamykla()
    pradinis_rusiuoklis = gamykla.sukurti("greitasis")
    programa = Programa(pradinis_rusiuoklis)

    # Visi galimi veiksmai surasyti zodyne.
    veiksmai = {
        "1": skaityti_is_failo,
        "2": ivesti_ranka,
        "3": parodyti_duomenis,
        "4": pasirinkti_algoritma,
        "5": surusiuoti,
        "6": irasyti_i_faila,
        "7": parodyti_aprasyma,
    }

    while True:
        parodyti_meniu()
        pasirinkimas = input("Pasirinkite veiksma: ").strip()
        if pasirinkimas == "0":
            print("Iki!")
            break
        veiksmas = veiksmai.get(pasirinkimas)
        if veiksmas is None:
            print("Neteisingas pasirinkimas.")
        else:
            veiksmas(programa)


if __name__ == "__main__":
    main()
