# Howto: Listen in Python

## Ziel

Listen sind die wichtigste Sammlungsstruktur in Python. Sie speichern mehrere Werte unter einem Namen und erlauben das Iterieren über die enthaltenen Elemente. In dieser Lernsituation brauchen Sie Listen ab **Niveau 3** für die Monitoring-Tour über mehrere Geräte.

---

## 1. Eine Liste erzeugen

Eine Liste schreiben Sie zwischen eckige Klammern, Elemente durch Komma getrennt:

```python
geraete = ["Drucker", "Sensor", "IP-Telefon"]
zahlen = [1, 2, 3, 4]
leer = []
```

Listen sind in Python **typenlos**: Eine Liste darf grundsätzlich Werte verschiedener Typen enthalten.

---

## 2. Auf einzelne Elemente zugreifen

Der Index startet bei `0`:

```python
print(geraete[0])   # "Drucker"
print(geraete[2])   # "IP-Telefon"
```

Negative Indizes zählen vom Ende:

```python
print(geraete[-1])  # "IP-Telefon" (letztes Element)
```

---

## 3. Länge bestimmen

`len()` liefert die Anzahl der Elemente:

```python
print(len(geraete))   # 3
```

---

## 4. Ein Element anhängen

`append()` hängt am Ende an:

```python
geraete.append("Server")
print(geraete)
# ["Drucker", "Sensor", "IP-Telefon", "Server"]
```

---

## 5. Über alle Elemente iterieren

Mit `for ... in ...`:

```python
for geraet in geraete:
    print(geraet)
```

Ausgabe:

```
Drucker
Sensor
IP-Telefon
Server
```

---

## 6. Listen mit eigenen Objekten

Listen können beliebige Werte enthalten — auch Instanzen Ihrer eigenen Klassen:

```python
drucker = Printer("HP", "LaserJet Pro", "192.168.10.42")
sensor = MyOwnSensor("Temperatur", "Serverraum A", "192.168.20.17")

ueberwachung = [drucker, sensor]
for ding in ueberwachung:
    print(ding.monitor())
```

Genau dieses Muster nutzen Sie in **Aufgabe C2** (Monitoring-Tour).

> **Tellerrand — Python vs. C#/Java:** In Python ist eine Liste typenlos: `[1, "zwei", drucker]` ist erlaubt. In C# und Java sind Listen typisiert (`List<int>`, `ArrayList<Device>`). Die Heterogenität in Python ist mächtig, verlangt aber Disziplin: Achten Sie darauf, dass alle Elemente in einer Iteration die aufgerufene Methode wirklich anbieten — sonst gibt es zur Laufzeit einen `AttributeError`.

---

## Verwandte Sammlungstypen — Ausblick

- **Tupel** (`(a, b, c)`) sind Listen ähnlich, aber unveränderlich.
- **Dictionaries** (`{"k": v}`) speichern Schlüssel-Wert-Paare.

Beide kommen in dieser Lernsituation **nicht** vor; Sie werden ihnen in späteren Themen begegnen.
