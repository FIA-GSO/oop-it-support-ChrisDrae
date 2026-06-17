# Testprotokoll — OOP-Tutorial: Geräteverwaltung im IT-Support

> **Vorlage zum Ausfüllen.** Kopieren Sie diese Datei vor Beginn unter eigenem Namen, z. B. `testprotokoll_<nachname>.md`. Tragen Sie für jeden Test die tatsächliche Beobachtung ein und kreuzen Sie den Status an.

---

## Kopf

- **Name:** _______________________________________
- **Datum:** _______________________________________
- **Bearbeitete Niveaus:** [ ] N1   [ ] N2   [ ] N3
- **Bonus C4 bearbeitet:** [ ] ja   [ ] nein

---

## Pflicht-Tests

Diese Tests sind für jedes bearbeitete Niveau auszuführen und zu dokumentieren.

### Test 1 — `__str__` der `NetworkComponent` (Niveau 1)

- **Aufgabe:** A2
- **Aktion:**
  ```python
  nc = NetworkComponent("192.168.10.42")
  print(nc)
  ```
- **Erwartung:** Ausgabe enthält IP `192.168.10.42` und Port `8080` in sprechender Form.
- **Beobachtung:**
  ```
  ________________________________________________________
  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung
- **Bemerkung:** _______________________________________________

---

### Test 2 — `renew_ip` lehnt fremde IP ab (Niveau 2)

- **Aufgabe:** B1
- **Aktion:**
  ```python
  nc = NetworkComponent("192.168.10.42")
  ergebnis = nc.renew_ip("10.0.0.5")
  print(ergebnis, nc.get_ip_address())
  ```
- **Erwartung:** Ablehnungs-Meldung wird ausgegeben; `ergebnis` ist `False`; IP bleibt `192.168.10.42`.
- **Beobachtung:**
  ```
  ________________________________________________________
  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung
- **Bemerkung:** _______________________________________________

---

### Test 3 — `renew_ip` übernimmt gültige IP (Niveau 2)

- **Aufgabe:** B1
- **Aktion:**
  ```python
  ergebnis = nc.renew_ip("192.168.10.99")
  print(ergebnis, nc.get_ip_address())
  ```
- **Erwartung:** Änderungs-Meldung wird ausgegeben; `ergebnis` ist `True`; IP ist jetzt `192.168.10.99`.
- **Beobachtung:**
  ```
  ________________________________________________________
  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung
- **Bemerkung:** _______________________________________________

---

### Test 4 — Reboot-Zyklus (Niveau 2)

- **Aufgabe:** B2a
- **Aktion:**
  ```python
  printer = Printer("HP", "LaserJet Pro", "192.168.10.42")
  printer.activate()
  printer.set_utilization(35)
  print("vor Reboot:", printer)
  printer.reboot()
  print("nach Reboot:", printer)
  ```
- **Erwartung:** Vor Reboot: aktiv `True`, Auslastung `35%`. Nach Reboot: Status `online`, aktiv `False`, Auslastung `0%`.
- **Beobachtung:**
  ```
  ________________________________________________________
  ________________________________________________________
  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung
- **Bemerkung:** _______________________________________________

---

### Test 5 — `set_utilization` lehnt Werte außerhalb 0..100 ab (Niveau 2)

- **Aufgabe:** B2b
- **Aktion:**
  ```python
  ergebnis = printer.set_utilization(150)
  print(ergebnis, printer.get_utilization())
  ```
- **Erwartung:** Ablehnungs-Meldung; `ergebnis` ist `False`; Auslastung bleibt unverändert.
- **Beobachtung:**
  ```
  ________________________________________________________
  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung
- **Bemerkung:** _______________________________________________

---

### Test 6 — `Printer.__str__` enthält Tonerstand (Niveau 2)

- **Aufgabe:** B3
- **Aktion:**
  ```python
  printer.use_toner(7)
  print(printer)
  ```
- **Erwartung:** Ausgabe enthält die Eltern-Information **plus** Toner-Angabe `93%`.
- **Beobachtung:**
  ```
  ________________________________________________________
  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung
- **Bemerkung:** _______________________________________________

---

### Test 7 — Eigene Klasse aus C1: `monitor()` läuft (Niveau 3)

- **Aufgabe:** C1
- **Klassenname Ihrer C1-Klasse:** _______________________________
- **Szenario:** ________________________________________________
- **Aktion:**
  ```python
  obj = <Ihre Klasse>(...)
  print(obj.monitor())
  ```
- **Erwartung:** Sprechende Statuszeile, Format frei.
- **Beobachtung:**
  ```
  ________________________________________________________
  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung
- **Bemerkung:** _______________________________________________

---

### Test 8 — Monitoring-Tour über heterogene Liste (Niveau 3)

- **Aufgabe:** C2
- **Aktion:**
  ```python
  ueberwachung = [printer, obj]
  for ding in ueberwachung:
      print(ding.monitor())
  ```
- **Erwartung:** Zwei Zeilen Ausgabe, jeweils im Format der zugehörigen Klasse.
- **Beobachtung:**
  ```
  ________________________________________________________
  ________________________________________________________
  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung
- **Bemerkung:** _______________________________________________

---

## Eigene Tests

Tragen Sie hier zusätzliche Tests ein, die Ihnen sinnvoll erscheinen — Randfälle, Fehlerfälle, eigene Szenarien.

### Eigener Test 1 — _________________________________________

- **Aufgabe / Bezug:** _________________________________________
- **Aktion:**
  ```python

  ```
- **Erwartung:** _____________________________________________
- **Beobachtung:**
  ```

  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung
- **Bemerkung:** _____________________________________________

### Eigener Test 2 — _________________________________________

- **Aufgabe / Bezug:** _________________________________________
- **Aktion:**
  ```python

  ```
- **Erwartung:** _____________________________________________
- **Beobachtung:**
  ```

  ```
- **Status:** [ ] wie erwartet   [ ] Abweichung
- **Bemerkung:** _____________________________________________

---

## Schluss-Reflexion

Beantworten Sie kurz (jeweils 1–3 Sätze):

1. **Welcher Test war für Sie am aufschlussreichsten — und warum?**
   _____________________________________________________________
   _____________________________________________________________

2. **Gab es Abweichungen, die Sie zunächst überrascht haben? Wie haben Sie sie geklärt?**
   _____________________________________________________________
   _____________________________________________________________

3. **Welche Tests würden Sie zusätzlich vorsehen, wenn dieses Modul in einem echten Monitoring-Tool eingesetzt würde?**
   _____________________________________________________________
   _____________________________________________________________
