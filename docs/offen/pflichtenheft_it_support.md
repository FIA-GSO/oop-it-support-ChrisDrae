# Pflichtenheft: Geräteverwaltung im IT-Support (offener Weg)

> **Dies ist Ihr Hauptdokument für den offenen Weg durch die Lernsituation.** Es beschreibt, **was** das Modul können muss — nicht, wie Sie es im Einzelnen umsetzen. Klassennamen, Methodenzuschnitt und innere Struktur entwerfen Sie selbst. Wer lieber kleinschrittig geführt arbeitet, nutzt stattdessen den geleiteten Weg (`it_support.py` + `docs/lernsituation_it_support.md`).

---

## 1. Ausgangslage und Ziel

> **Gemeinsamer Einstieg:** Das ausführliche Szenario, die Motivation („Warum OOP?"), die vier Grundpfeiler und die Einstiegsfragen für das Unterrichtsgespräch stehen — für beide Wege — in [`../einstieg.md`](../einstieg.md). Die folgende Ausgangslage fasst sie für den offenen Weg knapp zusammen.

Sie arbeiten als Auszubildende:r im **OHMega IT-Support**. Die Netzwerkgeräte — Drucker, Sensoren, IP-Telefone, … — werden bisher in einer Tabellenkalkulation gepflegt. Das skaliert nicht: Statusabfragen kosten Zeit, beim manuellen Eintragen entstehen Fehler.

Die Teamleitung möchte mittelfristig ein **Monitoring-Werkzeug** bauen, das den Zustand aller Geräte zentral abfragt. Bevor das Werkzeug entstehen kann, braucht es eine saubere **Datengrundlage** in Python: ein Modul, das jedes Gerät als Objekt mit definierten Eigenschaften und Methoden modelliert.

**Ihr Auftrag:** Entwerfen und implementieren Sie dieses Modul objektorientiert. Sie liefern am Ende ab:

1. ein **UML-Klassendiagramm** Ihrer Struktur (Entwurf),
2. den **Quellcode** in `it_support_offen.py`,
3. ein ausgefülltes **Abnahmeprotokoll** (`docs/offen/abnahme_it_support.md`).

> **Berufsbezug:** Solche Strukturen begegnen Ihnen später in jeder **Configuration Management Database (CMDB)** (ServiceNow, i-doit, OTRS) und in Monitoring-Tools (Nagios, Zabbix, Prometheus). Geräte als Objekte mit Status, Auslastung und Endpunkt sind dort Alltag.

---

## 2. Vorgehen: erst Entwurf, dann Code

Halten Sie diese Reihenfolge ein — sie ist Teil des Lernziels:

1. **Anforderungen lesen** (Abschnitt 4) und offene Punkte klären.
2. **Entwurf zeichnen:** UML-Klassendiagramm Ihrer geplanten Klassen (Abschnitt 5). Nutzen Sie [`../howto_uml.md`](../howto_uml.md).
3. **Implementieren** in `it_support_offen.py`, ausgehend von Ihrem Diagramm.
4. **Prüfen:** Abnahmekriterien durchgehen (Abschnitt 7), eigene Tests schreiben, Diagramm mit Code abgleichen.

> Wer zuerst die Struktur zeichnet, merkt früh, ob Verantwortlichkeiten sauber verteilt sind — und baut nicht mitten in der Implementierung um.

---

## 3. Konzept-Kompass

Diese objektorientierten Konzepte brauchen Sie. Die Kurzdefinition genügt zum Start; vertiefen Sie über die Quellen in Abschnitt 8.

| Konzept | In einem Satz |
| --- | --- |
| **Klasse / Objekt** | Eine Klasse ist der Bauplan, ein Objekt eine konkrete Ausprägung davon (Bauplan Haus ↔ konkretes Haus). |
| **Attribut / Methode** | Ein Attribut ist ein **Wert**, den ein Objekt speichert; eine Methode ist eine Funktion, die zum Objekt gehört. |
| **Konstruktor** (`__init__`) | Spezielle Methode, die einmal bei der Erzeugung eines Objekts läuft und seine Attribute einrichtet. |
| **Getter / Setter** | Lese- bzw. Schreibmethode für ein (gekapseltes) Attribut; ein _validierender_ Setter weist ungültige Werte ab. |
| **Text-Repräsentation** (`__str__`) | Methode, die das Objekt als sprechenden Text liefert; wird von `print(...)` / `str(...)` automatisch aufgerufen. |
| **Datenkapselung** | Daten und die Regeln, die sie schützen, liegen zusammen in der Klasse; der Zugriff von außen wird kontrolliert. |
| **Detail-Verbergen** | Eine interne Regel (z. B. eine Prüfung) bleibt in der Klasse und ist von außen weder einsehbar noch umgehbar. |
| **Vererbung** | Eine Klasse („ist-ein") übernimmt Eigenschaften einer allgemeineren Klasse und ergänzt oder überschreibt sie. |
| **Komposition** | Eine Klasse („hat-ein") enthält ein Objekt einer anderen Klasse als Bestandteil. |
| **Polymorphismus** | Verschiedene Objekte reagieren auf denselben Methodenaufruf jeweils auf ihre eigene Art. |

> **Sichtbarkeit in Python:** Ein führender Unterstrich (`_name`) signalisiert „intern, bitte nicht von außen anfassen". Es ist eine **Konvention**, kein erzwungenes Verbot — anders als `private` in C#/Java. Nutzen Sie den Unterstrich bewusst zur Kennzeichnung interner Attribute.

---

## 4. Funktionale Anforderungen

Die Anforderungen sind in **drei Ausbaustufen** gegliedert, die den Niveaus entsprechen. Jede Stufe setzt die vorige als abgeschlossen voraus. Die Anforderungen beschreiben **beobachtbares Verhalten** — wie Sie die Klassen und Methoden benennen und schneiden, entscheiden Sie.

### Ausbaustufe A ✦ — Netzwerkschnittstelle (Kernmodell)

| Nr. | Anforderung |
| --- | --- |
| **/FA10/** | Es gibt eine Klasse, die eine **Netzwerkschnittstelle** eines Firmengeräts modelliert. Sie speichert eine **IP-Adresse** und einen **Port** (Standardwert `8080`). |
| **/FA11/** | Die IP-Adresse und der Port sind von außen **lesbar** abrufbar. |
| **/FA12/** | Das Objekt liefert eine **sprechende Text-Repräsentation** (z. B. für `print(...)`), die IP und Port enthält. |

### Ausbaustufe B ✦✦ — Kapselung und Vererbung

| Nr. | Anforderung |
| --- | --- |
| **/FA20/** | Die IP der Netzwerkschnittstelle lässt sich **ändern, aber nicht beliebig**: Nur **Firmen-Adressen** sind zulässig. Die Geschäftsregel lautet: Eine Firmen-Adresse beginnt mit `192.168.`. |
| **/FA21/** | Die **Prüfregel ist intern gekapselt** (Detail-Verbergen): Es gibt **keinen** öffentlichen Weg, eine IP ungeprüft zu setzen, und die Regel ist von außen nicht ablesbar. Eine abgelehnte Änderung wird als Meldung ausgegeben; eine erfolgreiche ebenfalls. Der Erfolg ist am Rückgabewert erkennbar. |
| **/FA22/** | Es gibt eine Basisklasse für **verwaltete Geräte**. Ein Gerät kennt mindestens: Gerätetyp, Hersteller, Modell, eine Netzwerk-Adresse sowie einen Laufzeit-Zustand aus **Status** (`offline`/`online`), **Aktiv-Kennzeichen** und **Auslastung** (Prozent). |
| **/FA23/** | Das Gerät hat einen **Lebenszyklus**: Ein **Neustart** gibt eine Meldung aus und setzt den Laufzeit-Zustand definiert zurück (Status `online`, nicht aktiv, Auslastung `0`). Ein Gerät lässt sich **aktivieren**. |
| **/FA24/** | Das Gerät zeigt **Zugriffsschutz in mehreren Spielarten** — alle drei müssen vorkommen: <br>**(a) validierender Schreibzugriff:** Die Auslastung lässt sich setzen, Werte außerhalb `0..100` werden abgelehnt (mit Meldung; Erfolg am Rückgabewert erkennbar). <br>**(b) nur lesender Zugriff:** Status, Auslastung und Aktiv-Kennzeichen sind lesbar, aber **nicht** direkt setzbar — sie ändern sich nur über die vorgesehenen Aktionen (Neustart, Aktivieren, Auslastung setzen). <br>**(c) nur intern:** Gerätetyp, Hersteller und Modell werden bei der Erzeugung festgelegt, haben **weder Lese- noch Schreibzugriff** von außen und erscheinen nur in der Text-Repräsentation. |
| **/FA25/** | Es gibt mindestens ein **spezialisiertes Gerät** (z. B. einen Drucker), das per **Vererbung** von der Basisklasse abgeleitet ist, ein eigenes Merkmal ergänzt (z. B. einen Tonerstand mit zugehöriger Aktion) und die Text-Repräsentation der Basisklasse **erweitert statt ersetzt**. |

### Ausbaustufe C ✦✦✦ — Komposition und Polymorphismus

| Nr. | Anforderung |
| --- | --- |
| **/FA30/** | Das Gerät hält seine Netzwerkschnittstelle per **Komposition** („hat-ein"): Es speichert ein Objekt der Netzwerk-Klasse als Attribut, statt IP und Port direkt zu führen. Die Schnittstelle ist lesend abrufbar. |
| **/FA31/** | Jede überwachbare Klasse bietet eine **Monitoring-Methode** an, die eine **kompakte Statuszeile** für die Überwachung liefert (Format frei, aber sprechend). **Wichtig:** Diese Methode trägt über **alle** überwachbaren Klassen hinweg **denselben Namen** — das ist die Voraussetzung für /FA33/. |
| **/FA32/** | Es gibt **mindestens eine weitere, eigenständige Klasse** (frei wählbares IT-Szenario, z. B. Raumsensor, IP-Telefon, Türverriegelung, Smart-Display). Sie nutzt die Netzwerkschnittstelle ebenfalls per **Komposition** und erbt **nicht** von der Geräte-Basisklasse. Sie hat mindestens drei Attribute (eines davon die Netzwerkschnittstelle), mindestens eine zustandsändernde Methode und bietet die Monitoring-Methode aus /FA31/ an. |
| **/FA33/** | Eine **Monitoring-Tour** fragt eine **heterogene Liste** verschiedener Geräte-Objekte einheitlich ab: Die Liste wird durchlaufen, und für jedes Objekt wird **dieselbe** Monitoring-Methode aufgerufen und ausgegeben (**Polymorphismus**). |

---

## 5. Dokumentationsanforderung — UML-Klassendiagramm

| Nr. | Anforderung |
| --- | --- |
| **/DA10/** | Vor der Implementierung erstellen Sie ein **UML-Klassendiagramm** Ihrer geplanten Struktur. Empfohlenes Werkzeug: **UMLetino** (siehe [`../howto_uml.md`](../howto_uml.md)). |
| **/DA11/** | Das Diagramm zeigt alle Klassen mit **Attributen und Methoden** sowie deren **Sichtbarkeit** (`+`/`-`/`#`). |
| **/DA12/** | Das Diagramm zeigt die **Beziehungen** korrekt: **Vererbung** (Dreieck ▷) und **Komposition** (Raute ◆). |
| **/DA13/** | Vor der Abgabe gleichen Sie Diagramm und Code ab: Beide müssen **dieselben** Klassen, Beziehungen und öffentlichen Methoden zeigen. Exportieren Sie das Diagramm als Bild (PNG/SVG) für die Abgabe. |

---

## 6. Qualitäts- und Rahmenanforderungen

| Nr. | Anforderung |
| --- | --- |
| **/QA10/** | Der Code liegt in **`it_support_offen.py`** und ist über `python it_support_offen.py` ausführbar. Eine `main()`-Demo zeigt die wichtigsten Funktionen, inklusive der Monitoring-Tour. |
| **/QA11/** | **Sprachregelung:** **Bezeichner** (Klassen, Methoden, Variablen) auf **Englisch**, in snake_case bzw. PascalCase. **Kommentare, Docstrings und Konsolenausgaben** auf **Deutsch**. |
| **/QA12/** | **Type Hints** an allen Funktions- und Methodensignaturen (Parameter und Rückgabewert). |
| **/QA13/** | **Docstrings** an allen öffentlichen Methoden: kurze Einleitungszeile, bei Bedarf Parameter/Rückgabe in Klartext. |
| **/QA14/** | Lesbarer Stil nach **PEP 8**. Keine verschachtelten Einzeiler oder Tricks zugunsten von Kürze — im Zweifel mehrere Zeilen mit sprechenden Zwischenvariablen. |
| **/RA10/** | Werkzeuge: **Python 3**, Projektisolation mit **venv** (siehe [`../howto_setup.md`](../howto_setup.md)). Tests optional mit **pytest** (siehe [`../howto_pytest.md`](../howto_pytest.md)). Versionierung mit **git**. |

---

## 7. Abnahmekriterien

Das Modul ist abgenommen, wenn folgende **beobachtbaren** Kriterien erfüllt sind. Dokumentieren Sie die Nachweise im Abnahmeprotokoll ([`abnahme_it_support.md`](abnahme_it_support.md)).

- [ ] **/FA12/** Die Netzwerkschnittstelle liefert eine sprechende Text-Repräsentation mit IP und Port.
- [ ] **/FA20–21/** Eine **fremde** IP (z. B. `10.0.0.5`) wird **abgelehnt**, die alte IP bleibt erhalten; eine **Firmen-IP** (z. B. `192.168.10.99`) wird **übernommen**.
- [ ] **/FA23/** Nach einem Neustart sind Status `online`, Aktiv `False`, Auslastung `0`.
- [ ] **/FA24a/** Eine Auslastung von `150` wird abgelehnt, ein gültiger Wert übernommen.
- [ ] **/FA24b/c/** Status/Aktiv sind lesbar, aber nicht direkt setzbar; Hersteller/Modell erscheinen nur in der Text-Ausgabe.
- [ ] **/FA25/** Das spezialisierte Gerät zeigt in seiner Text-Ausgabe die **geerbte** Information **plus** sein eigenes Merkmal.
- [ ] **/FA30/** Das Gerät hält die Netzwerkschnittstelle als Komposition (keine direkte IP-Speicherung mehr).
- [ ] **/FA32/** Eine eigenständige, **nicht** abgeleitete Klasse mit Komposition und Monitoring-Methode existiert.
- [ ] **/FA33/** Die Monitoring-Tour gibt für eine Liste aus mindestens zwei verschiedenen Objekttypen je eine Statuszeile aus.
- [ ] **/DA13/** Ein UML-Klassendiagramm liegt vor und stimmt mit dem Code überein.
- [ ] **/QA10–14/** Code ausführbar, Sprachregelung, Type Hints, Docstrings und Stil eingehalten.

---

## 8. Informationsressourcen

Der offene Weg lebt davon, dass Sie selbst recherchieren. Diese Quellen helfen:

**Im Projekt:**
- [`../howto_uml.md`](../howto_uml.md) — UML-Klassendiagramme lesen und mit UMLetino zeichnen.
- [`../howto_setup.md`](../howto_setup.md) — Python und Entwicklungsumgebung einrichten.
- [`../howto_pytest.md`](../howto_pytest.md) — Tests schreiben und ausführen.
- [`../howto_listen.md`](../howto_listen.md) — Refresher zu Python-Listen (für die Monitoring-Tour).

**Extern:**
- Offizielle Python-Dokumentation: <https://docs.python.org/3/tutorial/classes.html> (Klassen, Vererbung).
- Python-`property` (für die optionale Vertiefung): <https://docs.python.org/3/library/functions.html#property>.

> **Wenn Sie nicht weiterkommen:** Der geleitete Weg (`docs/lernsituation_it_support.md`) zerlegt dieselbe Aufgabe in kleine Schritte. Sie dürfen ihn jederzeit als Stütze heranziehen — er ist kein „Schummeln", sondern eine zweite Tür zum selben Raum.

---

## 9. Leitplanken-Fragen

### 9.1 Orientierung — bevor Sie beginnen

Beantworten Sie diese Fragen für sich, bevor Sie das Diagramm zeichnen. Die Antworten stehen in diesem Pflichtenheft.

1. Welche Rolle hat das Modul, das Sie bauen, im Tagesgeschäft des OHMega IT-Supports — und was ist ausdrücklich **nicht** Ihre Aufgabe?
2. Welche drei Artefakte liefern Sie am Ende ab?
3. Was ist laut Abschnitt 2 Ihr **erster** konkreter Arbeitsschritt — noch vor der ersten Zeile Code?
4. Woran erkennen Sie am Ende, dass Ihr Modul abgenommen werden kann?

### 9.2 Reflexion — wenn Sie fertig sind

Beantworten Sie schriftlich (jeweils 2–4 Sätze). Sie gehören ins Abnahmeprotokoll.

1. **Detail-Verbergen:** Warum gibt es bewusst keinen direkten Weg, die IP ungeprüft zu setzen? Welchen Vorteil hat es, die Prüfregel in der Klasse zu verstecken?
2. **Komposition vs. Vererbung:** Warum erbt Ihre eigenständige Klasse (/FA32/) **nicht** von der Geräte-Basisklasse? Welche Eigenschaft eines Geräts wäre auf sie falsch übertragen worden?
3. **Polymorphismus:** Warum funktioniert die Monitoring-Tour nur, wenn alle Klassen die Monitoring-Methode unter demselben Namen anbieten? Was passiert zur Laufzeit, wenn eine Klasse sie nicht hat?
