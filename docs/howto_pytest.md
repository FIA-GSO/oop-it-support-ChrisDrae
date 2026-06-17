# Howto: pytest — automatisierte Tests in Python

## Ziel

`pytest` ist das verbreitetste Test-Framework in Python. Diese Anleitung zeigt Ihnen die Grundlagen, damit Sie eigene Tests für die Klassen aus diesem Tutorial schreiben können.

> **Hinweis zu dieser Lernsituation:** Die Pflicht-Aufgaben (A1 bis C4) verlangen **keine** pytest-Tests — Sie dokumentieren Ihre Beobachtungen im Testprotokoll (`testprotokoll_it_support.md`). Wenn Sie zusätzlich automatisiert testen wollen, hilft Ihnen dieses Howto. Empfohlen vor allem für die Validierungslogik in B1 und B2b.

---

## 1. Installation

In aktiver virtueller Umgebung (siehe `howto_setup.md`):

```bash
pip install pytest
```

Prüfen:

```bash
python -m pytest --version
```

---

## 2. Konvention für Test-Dateien

`pytest` findet Tests automatisch nach Namens-Konvention:

- Datei beginnt mit `test_` (z. B. `test_validator.py`, `test_it_support.py`).
- Funktion innerhalb der Datei beginnt ebenfalls mit `test_`.

Eine Test-Datei für dieses Tutorial könnte z. B. `test_it_support.py` heißen und im Repo-Wurzelverzeichnis neben `it_support.py` liegen.

---

## 3. Eine Test-Funktion schreiben

Ein Test ist eine ganz normale Funktion, die mit `assert` ein erwartetes Verhalten prüft:

```python
from it_support import NetworkComponent


def test_renew_ip_lehnt_fremde_adresse_ab():
    nc = NetworkComponent("192.168.10.42")
    ergebnis = nc.renew_ip("10.0.0.5")
    assert ergebnis is False
    assert nc.get_ip_address() == "192.168.10.42"


def test_renew_ip_uebernimmt_firmen_adresse():
    nc = NetworkComponent("192.168.10.42")
    ergebnis = nc.renew_ip("192.168.10.99")
    assert ergebnis is True
    assert nc.get_ip_address() == "192.168.10.99"
```

> **Zur Erinnerung:** `assert <bedingung>` lässt den Test bestehen, wenn die Bedingung wahr ist. Ist sie falsch, schlägt der Test fehl und `pytest` zeigt den genauen Wert an.

---

## 4. Tests ausführen

Aus dem Repo-Wurzelverzeichnis:

```bash
python -m pytest
```

Beispiel-Ausgabe bei Erfolg:

```
============================= test session starts =============================
collected 2 items

test_it_support.py ..                                                    [100%]

============================== 2 passed in 0.04s ==============================
```

Jeder Punkt steht für einen erfolgreichen Test. Bei Fehlern erscheinen `F` statt Punkten und detaillierte Fehlermeldungen.

> **Wichtig:** Verwenden Sie immer `python -m pytest`, nicht direkt `pytest`. Der Aufruf über `python -m` stellt sicher, dass die richtige Python-Installation und venv genutzt werden.

---

## 5. Fehlerausgabe lesen

Beispiel:

```
=================================== FAILURES ===================================
______________ test_renew_ip_uebernimmt_firmen_adresse _______________

    def test_renew_ip_uebernimmt_firmen_adresse():
        nc = NetworkComponent("192.168.10.42")
        ergebnis = nc.renew_ip("192.168.10.99")
>       assert ergebnis is True
E       assert None is True

test_it_support.py:14: AssertionError
```

Lesehilfe:

- **Block-Kopf** (`______ test_… ______`): Welcher Test ist fehlgeschlagen.
- **Code-Auszug**: Die Zeile mit `>` ist die fehlgeschlagene Assertion.
- **`E …`-Zeile**: Was tatsächlich verglichen wurde. Hier: `ergebnis` war `None`, erwartet war `True`. Vermutliche Ursache: `renew_ip` hat keinen `return`-Wert.
- **Pfad und Zeilennummer**: Wo genau im Test die Assertion fehlschlug.

---

## 6. Mehr Detail mit `-v`

Mit `-v` (verbose) sehen Sie pro Test eine eigene Zeile inkl. Status:

```bash
python -m pytest -v
```

Ausgabe-Beispiel:

```
test_it_support.py::test_renew_ip_lehnt_fremde_adresse_ab PASSED         [ 50%]
test_it_support.py::test_renew_ip_uebernimmt_firmen_adresse PASSED       [100%]
```

---

## 7. Häufige Probleme

### `ModuleNotFoundError: No module named 'it_support'`

`pytest` muss aus dem Repo-Wurzelverzeichnis aufgerufen werden, damit `from it_support import ...` funktioniert. Prüfen Sie Ihren Arbeitspfad.

### `pytest: command not found`

Sie haben `pytest` ohne aktive venv aufgerufen oder nicht installiert. Aktivieren Sie venv und installieren Sie pytest erneut. Tipp: nutzen Sie `python -m pytest` statt direktem `pytest`-Aufruf.

### Tests werden nicht gefunden

- Datei beginnt nicht mit `test_`.
- Funktion beginnt nicht mit `test_`.
- Datei liegt in einem Ordner ohne `__init__.py` (für dieses Tutorial nicht relevant — Tests gehören neben `it_support.py`).

---

## 8. Vorschläge für eigene Tests

Sinnvolle Stellen, um pytest-Tests zu schreiben:

| Aufgabe | Test-Idee |
|---|---|
| B1 | `renew_ip` lehnt Adresse außerhalb `192.168.` ab; `renew_ip` akzeptiert gültige Adresse; Rückgabewert stimmt. |
| B2b | `set_utilization` lehnt -1, 101, 150 ab; akzeptiert 0, 50, 100; Auslastung wird (oder wird nicht) angepasst. |
| B3 | `Printer("HP", "LJ", "192.168.10.42")` liefert über `__str__` einen String, der `Toner` enthält. |
| C1 | Ihre eigene Klasse: `monitor()` liefert einen nicht-leeren String. |
| C2 | Eine heterogene Liste lässt sich iterieren, alle Elemente liefern einen `monitor()`-String. |

---

## 9. Mehr lernen

- Offizielle Doku: [docs.pytest.org](https://docs.pytest.org/)
- `python -m pytest --help` für die Optionsübersicht.
