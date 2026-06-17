# Howto: Setup — Python, virtuelle Umgebung und VS Code

## Ziel

Diese Anleitung führt Sie in unter 15 Minuten zu einer funktionsfähigen Arbeitsumgebung für das OOP-Tutorial.

---

## 1. Voraussetzungen

- **Python 3** (aktuelle Version, mindestens 3.9). Prüfen Sie in der Konsole:
  ```bash
  python --version
  ```
  Erwartete Ausgabe: `Python 3.x.y`. Falls Python fehlt, installieren Sie es von [python.org](https://www.python.org/downloads/) (auf Windows beim Installer **„Add Python to PATH"** aktivieren).

- **VS Code** als empfohlene Entwicklungsumgebung. Download: [code.visualstudio.com](https://code.visualstudio.com/).
  - Empfohlene Erweiterung: **Python** (Microsoft).

- **git** (optional, aber praktisch für Klonen und Abgabe):
  ```bash
  git --version
  ```

---

## 2. Repo holen

**Per git:**
```bash
git clone <Repo-URL>
cd oop-it-support
```

**Ohne git:** ZIP herunterladen, in einen Ordner Ihrer Wahl entpacken, in der Konsole in den Ordner wechseln.

---

## 3. Virtuelle Umgebung (venv) anlegen

Eine **virtuelle Umgebung** isoliert die Pakete dieses Projekts vom System-Python. Das schützt vor Versionskonflikten zwischen Projekten.

Im Repo-Wurzelverzeichnis:

```bash
python -m venv .venv
```

Dieser Befehl erzeugt einen Ordner `.venv` mit einer eigenen Python-Installation.

---

## 4. venv aktivieren

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (cmd.exe):**
```cmd
.venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

Nach erfolgreicher Aktivierung steht `(.venv)` am Anfang Ihrer Konsolen-Eingabezeile. Solange diese Markierung sichtbar ist, arbeiten Sie in der isolierten Umgebung.

> **Bei jedem neuen Konsolenfenster** müssen Sie venv erneut aktivieren.

> **Tellerrand — PowerShell-Sperre auf Windows:** Falls die Aktivierung in PowerShell mit einer Fehlermeldung zu „Skripte können nicht ausgeführt werden" abbricht, einmalig erlauben:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```

---

## 5. Pakete installieren (optional)

Für dieses Tutorial werden **keine** zusätzlichen Pakete zwingend benötigt — alle Beispiele laufen mit der Python-Standardbibliothek.

Wenn Sie eigene Tests mit pytest schreiben möchten (siehe `docs/howto_pytest.md`):

```bash
pip install pytest
```

---

## 6. VS Code öffnen und Python-Interpreter wählen

1. **Ordner öffnen:** `File → Open Folder…` und das Repo-Wurzelverzeichnis wählen.
2. **Python-Interpreter wählen:** `Ctrl+Shift+P` → tippen Sie `Python: Select Interpreter` → wählen Sie den Eintrag mit `.venv` im Pfad. VS Code merkt sich die Wahl pro Projekt.
3. **Datei öffnen:** im Datei-Browser `it_support.py` doppelklicken.

---

## 7. Skelett ausführen

In der VS-Code-Konsole oder einem externen Terminal (mit aktiver venv):

```bash
python it_support.py
```

Erwartete Ausgabe im Anfangszustand: **keine** — das ist kein Fehler. Die `main()`-Funktion enthält auskommentierte Demo-Zeilen, die Sie schrittweise einkommentieren, sobald die jeweiligen Aufgaben fertig sind.

Für das N3-Skelett:

```bash
python it_support_n3.py
```

Hier sehen Sie schon im Ausgangszustand die Drucker-Demo und die IP-Validierung.

---

## 8. Häufige Probleme

### `python` nicht gefunden

- Auf Windows ggf. `py` statt `python`:
  ```bash
  py -m venv .venv
  py it_support.py
  ```
- Oder: Python-Installation reparieren und „Add to PATH" aktivieren.

### venv-Aktivierung schlägt fehl

- Pfadtrennzeichen passen nicht zum Betriebssystem. Windows: Backslash, Linux/macOS: Forward Slash.
- Auf Windows-PowerShell: ExecutionPolicy-Problem (siehe Tellerrand in Abschnitt 4).

### VS Code findet die venv nicht

- VS Code neu starten, dann erneut `Python: Select Interpreter`.
- Manuell den Pfad eingeben: `.venv/Scripts/python.exe` (Windows) bzw. `.venv/bin/python` (Linux/macOS).

### `python it_support.py` läuft, gibt aber nichts aus

- Das ist im Anfangszustand **korrekt**. Die `main()`-Funktion enthält nur auskommentierte Zeilen. Kommentieren Sie schrittweise ein, sobald die zugehörigen Aufgaben fertig sind.

---

## 9. venv beenden

Wenn Sie die isolierte Umgebung verlassen wollen:

```bash
deactivate
```

`(.venv)` verschwindet aus der Eingabezeile.
