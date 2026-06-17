# Einstieg: Objektorientierte Geräteverwaltung im IT-Support

> **Für beide Wege — geleitet wie offen.** Dieses Dokument ist der gemeinsame Einstieg in die Lernsituation: Es klärt das Szenario, die fachliche Motivation und die Konzepte, um die es geht. Es eignet sich als Grundlage für die **Einstiegsstunde** und das **Unterrichtsgespräch**. Erst danach wählen Sie Ihren Arbeitsweg (siehe [README](../README.md) → „Zwei Wege durch die Lernsituation").

---

## 1. Das Szenario

Sie arbeiten als Auszubildende:r im **OHMega IT-Support**. Bisher dokumentiert das Team die Netzwerkgeräte — Drucker, Sensoren, IP-Telefone, … — in einer Tabellenkalkulation. Das skaliert nicht mehr: Statusabfragen kosten Zeit, beim manuellen Eintragen schleichen sich Fehler ein, und niemand kann auf einen Blick sehen, welches Gerät gerade Probleme macht.

Die Teamleitung möchte deshalb mittelfristig ein eigenes **Monitoring-Werkzeug** bauen, das den Zustand aller Geräte zentral abfragt und in einer einheitlichen Sicht anzeigt. Bevor das Werkzeug entstehen kann, braucht es eine saubere **Datengrundlage** in Python: ein Modul, das jedes Gerät als Objekt mit definierten Eigenschaften und Methoden modelliert. Genau dieses Modul bauen Sie in dieser Lernsituation auf.

---

## 2. Warum überhaupt objektorientiert?

Sie könnten jedes Gerät auch als lose Sammlung von Variablen oder als weitere Tabellenzeile führen — genau das stößt aber an dieselben Grenzen wie die bisherige Tabellenkalkulation: Daten und die zugehörigen Regeln (Was ist eine gültige Firmen-IP? Ab wann gilt ein Gerät als ausgelastet?) liegen getrennt, jeder kann jeden Wert überschreiben, und jede neue Geräteart zieht Anpassungen quer durch den Code nach sich.

Die **objektorientierte Programmierung (OOP)** bündelt Daten und Verhalten in **Objekten**, sichert sie über **Kapselung** gegen unkontrollierte Zugriffe, vermeidet mit **Vererbung** und **Polymorphismus** doppelten Code und hält das Modell erweiterbar. Deshalb ist OOP das vorherrschende Paradigma in der professionellen Software- und IT-Verwaltung — und ein Prüfungsschwerpunkt Ihrer Ausbildung als Fachinformatiker:in.

---

## 3. Worum es fachlich geht — die vier Grundpfeiler der OOP

In dieser Lernsituation erarbeiten Sie die **vier Grundpfeiler der objektorientierten Programmierung** — genau die Konzepte, deren Darstellung und Erklärung in der Abschlussprüfung der Fachinformatiker:innen erwartet wird:

- **Abstraktion** (auch _Generalisierung_) — Reale Geräte werden als **Klassen** modelliert und auf die wesentlichen Attribute und Methoden reduziert; gemeinsame Eigenschaften zieht man in eine Basisklasse zusammen.
- **Kapselung** — Daten und die Regeln, die sie schützen, liegen zusammen in der Klasse; der Zugriff von außen wird kontrolliert (Detail-Verbergen und Zugriffsschutz).
- **Vererbung** — Eine spezialisierte Klasse („ist-ein") übernimmt Eigenschaften einer allgemeineren Klasse und vermeidet so doppelten Code.
- **Polymorphismus** — Verschiedene Objekte reagieren auf denselben Methodenaufruf jeweils auf ihre eigene Art.

Darauf aufbauend lernen Sie zwei **erweiterte, aber praxisrelevante Konzepte** kennen, die über die vier Grundpfeiler hinausgehen:

- **Komposition** — Eine Klasse baut sich aus anderen Objekten auf („hat-ein") — als bewusste Alternative zur Vererbung.
- **Monitoring-Tour** — Heterogene Geräte werden über eine gemeinsame Methode einheitlich abgefragt — Polymorphismus in der Anwendung und ein erster Vorgriff auf das spätere Werkzeug.

---

## 4. Berufsbezug

Solche Strukturen begegnen Ihnen später in der **Configuration Management Database (CMDB)** jeder professionellen IT-Verwaltung — Stichworte: ServiceNow, OTRS, i-doit. Werkzeuge wie Nagios, Zabbix oder Prometheus arbeiten intern mit denselben Konzepten: Geräte als Objekte mit Status, Auslastung und Endpunkt. Wenn Sie später mit C# oder Java arbeiten, finden Sie die vier Grundpfeiler fast 1:1 wieder — sie sind sprachübergreifend.

---

## 5. Einstiegsfragen für das Unterrichtsgespräch

Diskutieren Sie diese Fragen, bevor Sie Ihren Arbeitsweg beginnen — sie eröffnen die Lernsituation und brauchen noch keine Programmierkenntnisse:

1. Welche Probleme der bisherigen Tabellenlösung lassen sich mit **Objekten** (Daten + zugehörige Regeln an einem Ort) besser lösen als mit einzelnen Variablen oder Tabellenzeilen?
2. Wo sind Ihnen die Begriffe **Klasse, Objekt, Vererbung oder Kapselung** schon begegnet — in der Ausbildung, in IT-Werkzeugen oder in anderen Programmiersprachen?
3. Warum lohnt es sich, **zuerst zu modellieren** (welche Geräte gibt es, was haben sie gemeinsam?), bevor man die erste Zeile Code schreibt?

---

## 6. Und jetzt? Ihren Weg wählen

Dieselbe Aufgabe, zwei gleichwertige Arbeitsweisen — wählen Sie (bzw. wählt Ihre Lehrkraft) den passenden:

| Weg | Für wen | Sie starten in |
| --- | --- | --- |
| **Geleitet** | Schritt für Schritt, mit Code-Skelett und kleinen Aufgaben (A1–C4) | [`lernsituation_it_support.md`](lernsituation_it_support.md) |
| **Offen** | Selbstorganisiert: Anforderungen statt Aufgaben, erst eigener UML-Entwurf, dann Code | [`offen/pflichtenheft_it_support.md`](offen/pflichtenheft_it_support.md) |

Beide führen zum selben Ziel. Der offene Weg darf den geleiteten jederzeit als Stütze heranziehen.
