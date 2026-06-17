"""Geräteverwaltung im internen Netz von OHMega IT — Schüler-Skelett N1 + N2.

Bearbeiten Sie nur die mit `# TODO`-Markierungen gekennzeichneten Stellen.
Die Aufgaben-IDs (A1, A2, B1, B2a, B2b, B3) verweisen auf die Lernsituation.

Niveau 1 (Aufgaben Ax) bearbeitet die Klasse `NetworkComponent`.
Niveau 2 (Aufgaben Bx) bearbeitet `NetworkComponent.renew_ip` sowie
die neuen Klassen `Device` und `Printer`.
"""


class NetworkComponent:
    """Netzwerkschnittstelle eines Firmengeräts.

    Eine IP-Adresse gilt nur, wenn sie eine Firmen-Adresse ist. Außenstehende
    können die IP über `renew_ip` ändern lassen; die Klasse prüft die Adresse
    selbst. Wie genau die Prüfung aussieht, ist ein internes Detail — von
    außen weder einsehbar noch umgehbar.
    """

    def __init__(self, ip_address: str):
        # TODO A1: Speichern Sie ip_address in self._ip_address.
        # TODO A1: Setzen Sie self._port = 8080.
        pass

    def renew_ip(self, new_ip: str) -> bool:
        """Prüft die neue IP und übernimmt sie. Gibt True bei Erfolg zurück."""
        # TODO B1: Wenn _is_company_address(new_ip) False liefert, geben Sie
        # eine Ablehnungs-Meldung mit print() aus und liefern False zurück.
        # Andernfalls: Meldung mit alter und neuer IP ausgeben, die IP
        # übernehmen und True zurückgeben.
        pass

    def _is_company_address(self, ip: str) -> bool:
        # TODO B1: Liefern Sie True genau dann, wenn ip mit "192.168." beginnt.
        # Tipp: str.startswith() hilft hier.
        pass

    def get_ip_address(self) -> str:
        """Gibt die aktuelle IP-Adresse zurück."""
        # TODO A2
        pass

    def get_port(self) -> int:
        """Gibt den Port zurück."""
        # TODO A2
        pass

    def __str__(self) -> str:
        # TODO A2: Liefern Sie eine sprechende Repräsentation, z. B.
        # "NetworkComponent(IP: 192.168.10.42, Port: 8080)".
        pass


class Device:
    """Basisklasse für verwaltete Geräte im Firmennetz.

    Beschreibende Felder (Gerätetyp, Hersteller, Modell) werden im Konstruktor
    festgelegt und ändern sich danach nicht. Sie haben weder Getter noch Setter
    und erscheinen nur in der String-Ausgabe. IP und Port werden hier direkt
    gehalten. Der Status ist von außen lesbar, aber nicht direkt setzbar —
    er ändert sich ausschließlich durch `reboot()`.
    """

    def __init__(self, device_type: str, vendor: str, model: str, ip_address: str):
        # TODO B2a: Speichern Sie die Argumente in den passenden Attributen
        # (self._device_type, self._vendor, self._model, self._ip_address).
        # Setzen Sie zusätzlich:
        #   self._port = 8080
        #   self._status = "offline"
        #   self._active = False
        #   self._utilization = 0
        pass

    def reboot(self) -> None:
        """Startet das Gerät neu und setzt den Laufzeit-Zustand zurück."""
        # TODO B2a: Geben Sie eine Neustart-Meldung mit print() aus, die
        # Gerätetyp, Modell und IP enthält.
        # Setzen Sie anschließend:
        #   _status = "online", _active = False, _utilization = 0
        pass

    def activate(self) -> None:
        """Markiert das Gerät als aktiv."""
        # TODO B2a
        pass

    def set_utilization(self, value: int) -> bool:
        """Setzt die Auslastung in Prozent. Werte außerhalb 0..100 werden abgelehnt."""
        # TODO B2b: Prüfen Sie, ob value < 0 oder value > 100. Wenn ja:
        # Ablehnungs-Meldung mit print() ausgeben und False zurückgeben.
        # Andernfalls: _utilization setzen und True zurückgeben.
        pass

    def get_status(self) -> str:
        """Gibt den aktuellen Status zurück (nur lesbar)."""
        # TODO B2b
        pass

    def get_utilization(self) -> int:
        """Gibt die aktuelle Auslastung in Prozent zurück."""
        # TODO B2b
        pass

    def is_active(self) -> bool:
        """Gibt zurück, ob das Gerät als aktiv markiert ist."""
        # TODO B2b
        pass

    def __str__(self) -> str:
        # TODO B2a: Liefern Sie eine sprechende Repräsentation, z. B.
        # "Drucker - HP LaserJet Pro | IP: 192.168.10.42 | Status: offline | "
        # "Aktiv: False | Auslastung: 0%"
        pass


class Printer(Device):
    """Bürodrucker; spezialisiert Device um die Tonerverwaltung."""

    def __init__(self, vendor: str, model: str, ip_address: str):
        # TODO B3: Rufen Sie super().__init__("Drucker", vendor, model, ip_address) auf.
        # Initialisieren Sie self._toner_percent = 100.
        pass

    def use_toner(self, amount: int) -> None:
        """Reduziert den Tonerstand um den angegebenen Prozentwert."""
        # TODO B3
        pass

    def __str__(self) -> str:
        # TODO B3: Erweitern Sie die Eltern-Repräsentation um den Tonerstand.
        # Tipp: super().__str__() liefert die Basis-Information.
        pass


def main() -> None:
    """Kleine Demo zum Testen Ihrer Implementierung.

    Kommentieren Sie die Zeilen schrittweise ein, sobald die jeweiligen
    Aufgaben fertig sind.
    """
    # --- Niveau 1 (NetworkComponent) ---
    # nc = NetworkComponent("192.168.10.42")
    # print(nc)

    # --- Niveau 2 (Detail-Verbergen) ---
    # nc.renew_ip("10.0.0.5")        # sollte abgelehnt werden
    # nc.renew_ip("192.168.10.99")   # sollte angenommen werden

    # --- Niveau 2 (Device, Printer) ---
    # printer = Printer("HP", "LaserJet Pro", "192.168.10.42")
    # printer.activate()
    # printer.set_utilization(35)
    # printer.use_toner(7)
    # print(printer)
    # printer.reboot()
    # print(printer)

    # --- Niveau 2 (Zugriffsschutz an Auslastung) ---
    # printer.set_utilization(150)   # sollte abgelehnt werden
    # print(f"Auslastung: {printer.get_utilization()}%")
    pass


if __name__ == "__main__":
    main()
