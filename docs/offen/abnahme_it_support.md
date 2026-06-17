# Abnahmeprotokoll — Geräteverwaltung im IT-Support (offener Weg)

> **Vorlage zum Ausfüllen.** Kopieren Sie diese Datei vor Beginn unter eigenem Namen, z. B. `abnahme_<nachname>.md`. Sie weisen damit nach, dass Ihr Modul die Anforderungen aus dem Pflichtenheft erfüllt. Da Sie Klassen und Methoden selbst benennen, dokumentieren Sie hier **Ihren** Code und **Ihre** Aufrufe.

---

## Kopf

- **Name:** _______________________________________
- **Datum:** _______________________________________
- **Datei mit Ihrem Code:** _______________________________________
- **UML-Diagramm (Dateiname):** _______________________________________

---

## Teil 1 — Entwurf: UML-Klassendiagramm

- [ ] Diagramm liegt als Bild (PNG/SVG) bei.
- [ ] Alle Klassen mit Attributen, Methoden und Sichtbarkeit (`+`/`-`/`#`) sind enthalten. **/DA11/**
- [ ] Vererbung (▷) und Komposition (◆) sind korrekt eingezeichnet. **/DA12/**

**Ihre Klassen (Name → Rolle):**

| Klassenname | Rolle / Verantwortlichkeit | Beziehung zu anderen |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |

---

## Teil 2 — Abnahme-Tests

Tragen Sie für jeden Test Ihre **konkreten** Aufrufe (mit Ihren Klassen-/Methodennamen) und die **tatsächliche** Beobachtung ein.

### Test 1 — Text-Repräsentation der Netzwerkschnittstelle  · /FA12/

- **Aktion:**
  ```python

  ```
- **Erwartung:** Ausgabe enthält IP und Port in sprechender Form.
- **Beobachtung:**
  ```

  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung

---

### Test 2 — Fremde IP wird abgelehnt, Firmen-IP übernommen  · /FA20/, /FA21/

- **Aktion:** (einmal mit einer Nicht-Firmen-IP, einmal mit `192.168.…`)
  ```python

  ```
- **Erwartung:** Fremd-IP abgelehnt (Meldung, alte IP bleibt); Firmen-IP übernommen (Meldung, neue IP aktiv). Erfolg am Rückgabewert erkennbar.
- **Beobachtung:**
  ```

  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung

---

### Test 3 — Neustart setzt den Laufzeit-Zustand zurück  · /FA23/

- **Aktion:** (Gerät aktivieren, Auslastung setzen, ausgeben; dann Neustart, erneut ausgeben)
  ```python

  ```
- **Erwartung:** Nach dem Neustart: Status `online`, Aktiv `False`, Auslastung `0`.
- **Beobachtung:**
  ```

  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung

---

### Test 4 — Auslastung außerhalb 0..100 wird abgelehnt  · /FA24a/

- **Aktion:**
  ```python

  ```
- **Erwartung:** Wert `150` abgelehnt (Meldung, Erfolg am Rückgabewert erkennbar); gültiger Wert übernommen.
- **Beobachtung:**
  ```

  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung

---

### Test 5 — Spezialisiertes Gerät erweitert die Text-Ausgabe  · /FA25/

- **Aktion:**
  ```python

  ```
- **Erwartung:** Ausgabe enthält die **geerbte** Information **plus** das eigene Merkmal (z. B. Tonerstand).
- **Beobachtung:**
  ```

  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung

---

### Test 6 — Eigenständige Klasse mit Komposition  · /FA32/

- **Klassenname:** _______________________  **Szenario:** _______________________
- **Aktion:** (Objekt erzeugen, Monitoring-Methode aufrufen)
  ```python

  ```
- **Erwartung:** Klasse erbt **nicht** von der Geräte-Basisklasse, hält die Netzwerkschnittstelle als Attribut, liefert eine sprechende Statuszeile.
- **Beobachtung:**
  ```

  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung

---

### Test 7 — Monitoring-Tour über heterogene Liste  · /FA33/

- **Aktion:** (Liste aus mindestens zwei verschiedenen Objekttypen durchlaufen, Monitoring-Methode je Objekt aufrufen)
  ```python

  ```
- **Erwartung:** Pro Objekt eine Statuszeile, jeweils im Format der zugehörigen Klasse.
- **Beobachtung:**
  ```

  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung

---

## Teil 3 — Eigene Tests

Tragen Sie hier Tests ein, die Ihnen zusätzlich sinnvoll erscheinen — Randfälle, Fehlerfälle, eigene Szenarien.

### Eigener Test 1 — _________________________________________

- **Bezug (Anforderung):** _______________________
- **Aktion:**
  ```python

  ```
- **Erwartung:** _____________________________________________
- **Beobachtung:**
  ```

  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung

### Eigener Test 2 — _________________________________________

- **Bezug (Anforderung):** _______________________
- **Aktion:**
  ```python

  ```
- **Erwartung:** _____________________________________________
- **Beobachtung:**
  ```

  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung

---

## Teil 4 — Soll/Ist-Abgleich Diagramm ↔ Code

- [ ] Jede Klasse aus dem Diagramm existiert im Code (gleicher Name).
- [ ] Jede Beziehung (Vererbung/Komposition) im Diagramm findet sich im Code wieder.
- [ ] Es gibt keine Klasse im Code, die im Diagramm fehlt.

**Abweichungen, die ich beim Abgleich gefunden und behoben habe:**

_____________________________________________________________
_____________________________________________________________

---

## Teil 5 — Reflexion

Beantworten Sie die Reflexionsfragen aus Abschnitt 9.2 des Pflichtenhefts (jeweils 2–4 Sätze):

1. **Detail-Verbergen — kein direkter IP-Setter:**
   _____________________________________________________________
   _____________________________________________________________

2. **Komposition statt Vererbung bei der eigenständigen Klasse:**
   _____________________________________________________________
   _____________________________________________________________

3. **Polymorphismus — gemeinsamer Methodenname:**
   _____________________________________________________________
   _____________________________________________________________
