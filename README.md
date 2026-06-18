[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/abQYVeaN)
# OOP-Tutorial: Geräteverwaltung im IT-Support

Lernsituation für die duale Ausbildung Fachinformatiker:in. Sie modellieren ein internes Geräteverwaltungs-Modul für den OHMega IT-Support — von einer einzelnen Klasse bis zu einer Monitoring-Tour über eine heterogene Geräteliste.

---

## Zwei Wege durch die Lernsituation

**Beide Wege starten gemeinsam** mit [`docs/einstieg.md`](docs/einstieg.md) — Szenario, fachliche Motivation und die Einstiegsfragen fürs Unterrichtsgespräch. Danach wählen Sie (bzw. wählt Ihre Lehrkraft) die Arbeitsweise:

| Weg | Für wen | Arbeitsdokument |
| --- | --- | --- |
| **Geleitet** | Schritt-für-Schritt, mit Code-Skelett und kleinen Aufgaben (A1–C4) | [`docs/lernsituation_it_support.md`](docs/lernsituation_it_support.md) + `it_support.py` |
| **Offen** | Selbstorganisiert: Anforderungen statt Aufgaben, erst eigener UML-Entwurf, dann Code | [`docs/offen/pflichtenheft_it_support.md`](docs/offen/pflichtenheft_it_support.md) + `it_support_offen.py` |

Beide führen zum selben Ziel und sind gleichwertig. Der offene Weg darf den geleiteten jederzeit als Stütze heranziehen.

---

## Schnellstart

1. Repo klonen oder herunterladen.
2. Python einrichten — siehe [`docs/howto_setup.md`](docs/howto_setup.md).
3. **Einstieg lesen (beide Wege):** [`docs/einstieg.md`](docs/einstieg.md) — Szenario, Motivation, Einstiegsfragen.
4. **Weg wählen** (Tabelle oben) und im jeweiligen Arbeitsdokument loslegen — geleitet z. B. mit Niveau 1 in `it_support.py`.

---

## Dateien im Überblick

### Was Sie bearbeiten

| Datei                | Weg / Niveau | Zweck                                                                                    |
| -------------------- | ------------ | ---------------------------------------------------------------------------------------- |
| `it_support.py`      | geleitet 1+2 | Skelett mit `# TODO`-Markern für `NetworkComponent`, `Device`, `Printer`                 |
| `it_support_n3.py`   | geleitet 3   | Klassen aus N1+N2 vorgegeben (jetzt mit Komposition); Sie ergänzen eigene Klasse + Tour |
| `it_support_offen.py`| offen        | Leere Startdatei — Sie strukturieren alles selbst nach dem Pflichtenheft                 |

### Was Sie lesen

| Datei                                                                  | Inhalt                                                              |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------- |
| [`docs/einstieg.md`](docs/einstieg.md)                                 | **Gemeinsamer Einstieg (beide Wege)** — Szenario, Motivation, vier Grundpfeiler, Einstiegsfragen |
| [`docs/lernsituation_it_support.md`](docs/lernsituation_it_support.md) | **Hauptdokument geleitet** — alle Aufgaben (A1–C4), Fragen          |
| [`docs/howto_setup.md`](docs/howto_setup.md)                           | venv- und VS-Code-Setup                                             |
| [`docs/howto_listen.md`](docs/howto_listen.md)                         | Refresher zu Python-Listen (relevant ab N3)                         |
| [`docs/howto_pytest.md`](docs/howto_pytest.md)                         | pytest-Bedienung (optional, für eigene Tests)                       |
| [`docs/howto_uml.md`](docs/howto_uml.md)                               | UML-Klassendiagramme lesen und mit UMLetino zeichnen                |
| [`docs/testprotokoll_it_support.md`](docs/testprotokoll_it_support.md) | Vorlage für Ihre Test-Dokumentation (geleiteter Weg)                |
| [`docs/offen/pflichtenheft_it_support.md`](docs/offen/pflichtenheft_it_support.md) | **Offener Weg** — Anforderungen, Abnahmekriterien, Leitplanken-Fragen |
| [`docs/offen/abnahme_it_support.md`](docs/offen/abnahme_it_support.md) | Abnahme- & Reflexionsprotokoll (offener Weg)                        |

---

## Zusammenspiel der Klassen

Als Landkarte in Worten — die formalen UML-Klassendiagramme dazu dokumentieren die Zwischenstände direkt im Aufgaben-Dokument ([Niveau 2](docs/lernsituation_it_support.md) und Niveau 3):

- **`NetworkComponent`** modelliert eine Netzwerkschnittstelle (IP, Port) und steht in Niveau 1/2 eigenständig.
- **`Device`** ist die Basisklasse für verwaltete Geräte; **`Printer` ist-ein `Device`** (Vererbung).
- Ab Niveau 3 **hat-ein `Device` eine `NetworkComponent`** (Komposition statt direkter IP-Speicherung), und `Device`/`Printer` bekommen eine `monitor()`-Methode.
- In C1 entwerfen Sie zusätzlich eine **eigenständige vierte Klasse**, die `NetworkComponent` ebenfalls per Komposition nutzt, aber **nicht** von `Device` erbt.

---

## Skelett ausführen

Aus dem Wurzelverzeichnis des Repos:

```bash
python it_support.py
python it_support_n3.py
python it_support_offen.py
```

> **Hinweis:** `python it_support.py` läuft im Anfangszustand fehlerfrei, erzeugt aber **keine** Ausgabe — das ist kein Fehler, sondern der erwartete Ausgangsstand. Die `main()`-Funktion enthält auskommentierte Demo-Zeilen, die Sie schrittweise einkommentieren, sobald die jeweiligen Aufgaben fertig sind.

`python it_support_n3.py` zeigt schon im Ausgangszustand die Drucker-Demo und die IP-Validierung — die Monitoring-Tour aktivieren Sie selbst in Aufgabe C2.

---

## Werkzeuge

- **Python 3** (aktuelle Version)
- **venv** für die Projektisolation
- **pytest** für Tests — Aufruf: `python -m pytest`
- **VS Code** als empfohlene Entwicklungsumgebung

Detaillierte Setup-Anleitung in [`docs/howto_setup.md`](docs/howto_setup.md).

---

## Hilfe und Feedback

Fragen zur Aufgabenstellung gehen an die Lehrkraft. Inhaltliche Stützen finden Sie in den `howto_*.md`-Dokumenten und in der Lernsituation selbst.
