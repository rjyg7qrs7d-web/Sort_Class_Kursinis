# Rusiavimo algoritmu programa

OOP kursinis darbas. Tema: Sort Class and Strategies.

## Turinys

1. [Įvadas](#1-ivadas)
2. [Analizė](#2-analize)
3. [Rezultatai ir išvados](#3-rezultatai-ir-isvados)

---

## 1. Įvadas

### 1.1 Kas tai per programa?

Programa rūšiuoja sveikuosius skaičius naudodama tris algoritmus:
burbulų rūšiavimą, greitąjį rūšiavimą ir įterpimo rūšiavimą. Visi
algoritmai paveldi iš bendros abstrakčios klasės `Rusiuoklis`. Tai
leidžia juos keisti vienas kitu nepakeičiant kitos kodo dalies.

Programa moka:
- Nuskaityti skaičius iš `.txt` arba `.csv` failo.
- Įrašyti rezultatą į failą.
- Vartotojui leisti pasirinkti algoritmą per meniu.

### 1.2 Kaip paleisti programą?

Reikalingas Python 3.10 arba naujesnis. Papildomų bibliotekų diegti
nereikia.

```bash
git clone https://github.com/rjyg7qrs7d-web/Sort_Class_Kursinis.git
cd Sort_Class_Kursinis
python3 main.py
```

Testai paleidžiami komanda:

```bash
python -m unittest discover -s tests
```

### 1.3 Kaip naudotis programa?

Paleidus programą, pasirodo meniu:

```
==================================================
 Rusiavimo algoritmu programa
==================================================
 1. Skaityti skaicius is failo
 2. Ivesti skaicius ranka
 3. Parodyti dabartinius duomenis
 4. Pasirinkti rusiavimo algoritma
 5. Surusiuoti
 6. Irasyti rezultata i faila
 7. Parodyti algoritmo aprasyma
 0. Iseiti
==================================================
```

Įprasta darbo eiga:

1. Įkelti skaičius (1 arba 2 punktas).
2. Pasirinkti algoritmą (4 punktas).
3. Surūšiuoti (5 punktas).
4. Įrašyti rezultatą į failą (6 punktas).

---

## 2. Analizė

### 2.1 Projekto struktūra

```
sort_coursework/
├── main.py                 # programos paleidimo failas
├── src/
│   ├── rusiuoklis.py       # abstrakti klase Rusiuoklis
│   ├── algoritmai.py       # konkretus algoritmai
│   ├── gamykla.py          # Factory Method sablonas
│   ├── programa.py         # Programos klase (kompozicija)
│   └── failai.py           # failu skaitymas ir rasymas
├── tests/
│   ├── test_algoritmai.py
│   ├── test_gamykla.py
│   ├── test_failai.py
│   └── test_programa.py
└── duomenys/
    ├── skaiciai.txt
    └── skaiciai.csv
```

### 2.2 Keturi OOP ramsčiai

#### 2.2.1 Abstrakcija

Abstrakcija — paslepiame realizacijos detales ir paliekame tik tai, ko
reikia naudotojui. Programoje yra abstrakti klasė `Rusiuoklis`, kuri
nurodo, **ką** rūšiuoklis turi mokėti, bet nesako **kaip** tai daryti:

```python
# src/rusiuoklis.py
from abc import ABC, abstractmethod


class Rusiuoklis(ABC):
    def __init__(self, pavadinimas):
        self._pavadinimas = pavadinimas

    @abstractmethod
    def rusiuoti(self, sarasas):
        pass
```

Kadangi klasė paveldi iš `ABC`, o metodas `rusiuoti` pažymėtas
`@abstractmethod`, tiesiogiai sukurti `Rusiuoklis()` objekto neįmanoma.
Tai patikrina testas:

```python
def test_negalima_sukurti_abstrakcios(self):
    with self.assertRaises(TypeError):
        Rusiuoklis("bandymas")
```

#### 2.2.2 Inkapsuliacija

Inkapsuliacija — vidinių duomenų apsauga nuo tiesioginio keitimo iš
išorės. Klasės atributas `_pavadinimas` prasideda pabraukimu (Python
sutartinis žymėjimas „nelieskite iš išorės"). Į jį galima patekti tik
per savybę (property), kuri leidžia tik skaityti:

```python
# src/rusiuoklis.py
@property
def pavadinimas(self):
    return self._pavadinimas
```

Klasė `Programa` papildomai grąžina sąrašo **kopiją**, kad išorinis
sąrašas nepaveiktų vidinio:

```python
# src/programa.py
def gauti_duomenis(self):
    return list(self._duomenys)
```

Tai patikrina testas:

```python
def test_duomenu_kopija(self):
    programa = Programa(BurbuluRusiavimas())
    programa.nustatyti_duomenis([1, 2, 3])
    gauti = programa.gauti_duomenis()
    gauti.append(99)
    self.assertEqual(programa.gauti_duomenis(), [1, 2, 3])
```

#### 2.2.3 Paveldėjimas

Paveldėjimas leidžia naujai klasei gauti tėvinės klasės savybes ir
pridėti savo elgesį. Visi trys algoritmai paveldi iš `Rusiuoklis` ir
aprašo tik savo rūšiavimo logiką:

```python
# src/algoritmai.py
class BurbuluRusiavimas(Rusiuoklis):
    def __init__(self):
        super().__init__("Burbulu rusiavimas")

    def rusiuoti(self, sarasas):
        sarasas = list(sarasas)
        n = len(sarasas)
        for i in range(n):
            for j in range(0, n - i - 1):
                if sarasas[j] > sarasas[j + 1]:
                    sarasas[j], sarasas[j + 1] = (
                        sarasas[j + 1], sarasas[j]
                    )
        return sarasas
```

Visos trys klasės paveldi tą pačią `pavadinimas` savybę ir gauna
bendrą interfeisą. Be paveldėjimo tą patį kodą reikėtų rašyti tris
kartus.

#### 2.2.4 Polimorfizmas

Polimorfizmas — tas pats metodo iškvietimas elgiasi skirtingai
priklausomai nuo objekto tipo. Kiekvienas algoritmas turi savo
`aprasyti()` versiją:

```python
class BurbuluRusiavimas(Rusiuoklis):
    def aprasyti(self):
        return ("Burbulu rusiavimas: gretimi elementai lyginami ir, "
                "jei reikia, sukeiciami vietomis. Sudetingumas: O(n^2).")


class GreitasisRusiavimas(Rusiuoklis):
    def aprasyti(self):
        return ("Greitasis rusiavimas: pasirenkamas atramos elementas, "
                "sarasaas padalinamas i dvi dalis ir kiekviena dalis "
                "rusiuojama atskirai. Sudetingumas: O(n log n).")
```

`Programa` klasė nežino, koks konkretus algoritmas yra naudojamas. Ji
tik kviečia `self._rusiuoklis.rusiuoti(...)`, o Python pati parenka
tinkamą metodą:

```python
def rusiuoti(self):
    return self._rusiuoklis.rusiuoti(self._duomenys)
```

### 2.3 Projektavimo šablonas — Factory Method

**Pasirinktas šablonas:** Factory Method.

**Kodėl jis tinka.** Programoje reikia kurti skirtingo tipo
rūšiuoklių objektus. Be šablono kiekvienoje vietoje, kur reikia naujo
rūšiuoklio, atsirastų pasikartojantis `if/elif` blokas:

```python
# Be Factory:
if pavadinimas == "burbulu":
    rusiuoklis = BurbuluRusiavimas()
elif pavadinimas == "greitasis":
    rusiuoklis = GreitasisRusiavimas()
```

Pridedant naują algoritmą tektų atnaujinti visas tokias vietas.
`RusiuokliuGamykla` viską sutelkia į vieną klasę:

```python
# src/gamykla.py
class RusiuokliuGamykla:
    _algoritmai = {
        "burbulu": BurbuluRusiavimas,
        "greitasis": GreitasisRusiavimas,
        "iterpimo": IterpimoRusiavimas,
    }

    @classmethod
    def sukurti(cls, pavadinimas):
        raktas = pavadinimas.lower().strip()
        if raktas not in cls._algoritmai:
            galimi = ", ".join(cls._algoritmai.keys())
            raise ValueError(
                f"Nezinomas algoritmas: '{pavadinimas}'. "
                f"Galimi: {galimi}."
            )
        klase = cls._algoritmai[raktas]
        return klase()
```

**Kodėl būtent Factory Method, o ne kitas šablonas?**

- **Singleton** netiktų — kiekvieną kartą reikia naujo rūšiuoklio
  objekto.
- **Builder** skirtas sudėtingiems objektams su daug parametrų. Mūsų
  rūšiuokliai paprasti.
- **Abstract Factory** tiktų, jei reikėtų kurti kelias susijusias
  objektų šeimas. Mes turime tik vieną šeimą (rūšiuokliai).

### 2.4 Kompozicija ir agregacija

Skirtumas:

- **Kompozicija** — konteineris pats sukuria ir valdo dalį. Be
  konteinerio dalis neegzistuoja.
- **Agregacija** — konteineris naudoja dalį, bet jos neturi.
  Sunaikinus konteinerį dalis lieka.

Abu principai yra `Programa` klasėje:

```python
# src/programa.py
class Programa:
    def __init__(self, rusiuoklis):
        # Agregacija: rusiuoklis ateina is isores.
        self._rusiuoklis = rusiuoklis
        # Kompozicija: failu tvarkykle sukuriama cia pat.
        self._failu_tvarkykle = FailuTvarkykle()
        self._duomenys = []
```

`_failu_tvarkykle` yra **kompozicija** — ji sukuriama `__init__`
metode, niekur kitur nesidalinama. Sunaikinus `Programa` objektą, ji
išnyks kartu.

`_rusiuoklis` yra **agregacija** — perduodama iš išorės, gali būti
pakeista bet kada metodu `nustatyti_rusiuokli`:

```python
def nustatyti_rusiuokli(self, rusiuoklis):
    if not isinstance(rusiuoklis, Rusiuoklis):
        raise TypeError("Rusiuoklis turi paveldeti is Rusiuoklis klases.")
    self._rusiuoklis = rusiuoklis
```

### 2.5 Failų skaitymas ir rašymas

Klasė `FailuTvarkykle` palaiko du formatus — `.txt` (skaičiai
atskirti tarpais) ir `.csv` (skaičiai atskirti kableliais):

```python
# src/failai.py
def skaityti(self, kelias):
    if not os.path.isfile(kelias):
        raise FileNotFoundError(f"Failas nerastas: {kelias}")

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
            f"Nepalaikomas failo formatas: '{pletinys}'."
        )

    return skaiciai
```

Klaidas (failas nerastas, blogas plėtinys) `main.py` pagauna ir
parodo žinutę vartotojui:

```python
try:
    programa.skaityti_is_failo(kelias)
except (FileNotFoundError, ValueError) as klaida:
    print(f"Klaida: {klaida}")
```

### 2.6 Vienetiniai testai

Programa padengta 31 testu, parašytu su `unittest`:

| Failas               | Ką tikrina                                |
|----------------------|-------------------------------------------|
| `test_algoritmai.py` | Visus tris algoritmus + abstrakčią klasę |
| `test_gamykla.py`    | Gamyklos kūrimą ir klaidų apdorojimą     |
| `test_failai.py`     | TXT ir CSV skaitymą bei rašymą           |
| `test_programa.py`   | Programos klasę ir algoritmų keitimą     |

Visi testai praeina:

```
$ python -m unittest discover -s tests
...............................
----------------------------------------------------------------------
Ran 31 tests in 0.006s

OK
```

### 2.7 Kodo stilius

Kodas atitinka PEP 8 reikalavimus:

- 4 tarpų įtraukos.
- Eilutės iki 79 simbolių.
- `snake_case` kintamiesiems ir funkcijoms, `CamelCase` klasėms.

---

## 3. Rezultatai ir išvados

### 3.1 Rezultatai

- Sukurta trijų algoritmų sistema, kurioje algoritmai laisvai
  keičiami vienas kitu per `Programa` arba `RusiuokliuGamykla`.
- Visi 31 testai praeina greičiau nei per 0,01 sekundės.
- Didžiausias iššūkis buvo suprasti skirtumą tarp kompozicijos ir
  agregacijos. Tai pavyko išspręsti aiškiai apibrėžiant, kuriuos
  objektus klasė `Programa` sukuria pati (kompozicija — `FailuTvarkykle`),
  o kuriuos gauna iš išorės (agregacija — `Rusiuoklis`).
- Antrasis iššūkis buvo PEP 8 reikalavimas, kad eilutė neviršytų 79
  simbolių — kai kuriose vietose teko skaidyti tekstą į kelias
  eilutes.

### 3.2 Išvados

Darbas atitinka visus kursinio reikalavimus:

- Pademonstruoti visi keturi OOP ramsčiai (abstrakcija, inkapsuliacija,
  paveldėjimas, polimorfizmas).
- Pritaikytas Factory Method projektavimo šablonas.
- Naudoti kompozicijos ir agregacijos principai.
- Įgyvendintas duomenų skaitymas ir rašymas iš `.txt` ir `.csv` failų.
- Pagrindinė funkcionalumo dalis padengta vienetiniais testais.
- Kodas atitinka PEP 8 stiliaus reikalavimus.

Programa atskleidžia OOP privalumą — naują algoritmą galima pridėti
nepakeičiant esamos kodo struktūros: užtenka sukurti naują `Rusiuoklis`
palikuonį ir pridėti vieną įrašą `RusiuokliuGamykla` žodyne.

### 3.3 Galimi plėtiniai

- Pridėti daugiau algoritmų (pvz., `MergeSort`, `HeapSort`).
- Leisti rūšiuoti ne tik sveikuosius skaičius, bet ir tekstinius
  duomenis ar realiuosius skaičius.
- Sukurti grafinę vartotojo sąsają vietoj komandinės eilutės meniu.

---

## 4. Šaltiniai

- [PEP 8 — Python kodo stiliaus gidas](https://peps.python.org/pep-0008/)
- [Python `abc` modulio dokumentacija](https://docs.python.org/3/library/abc.html)
- [Python `unittest` modulio dokumentacija](https://docs.python.org/3/library/unittest.html)
- [Refactoring.Guru — Factory Method](https://refactoring.guru/design-patterns/factory-method)
