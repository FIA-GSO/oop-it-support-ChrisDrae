"""Geräteverwaltung im internen Netz von OHMega IT — Schüler-Skelett N3.

Aufbauend auf Niveau 1 und 2: NetworkComponent, Device und Printer sind
bereits vollständig implementiert. Im Vergleich zum N2-Stand hat sich
Device verändert: Es enthält jetzt eine NetworkComponent als Attribut
(Komposition) und gibt sie über get_network() heraus. Außerdem besitzen
Device und Printer eine neue Methode `monitor()`, die eine kompakte
Status-Zeile für die Überwachung liefert.

Ihre Aufgaben in Niveau 3:
  - C1: Eine eigenständige Klasse entwerfen, die NetworkComponent per
        Komposition nutzt und ebenfalls eine `monitor()`-Methode anbietet.
  - C2: Eine Monitoring-Tour über eine heterogene Liste laufen lassen,
        in der Drucker und Ihre eigene Klasse zusammen abgefragt werden.
"""


class NetworkComponent:
    """Netzwerkschnittstelle eines Firmengeräts.

    Eine IP-Adresse gilt nur, wenn sie eine Firmen-Adresse ist. Außenstehende
    können die IP über `renew_ip` ändern lassen; die Klasse prüft die Adresse
    selbst. Wie genau die Prüfung aussieht, ist ein internes Detail — von
    außen weder einsehbar noch umgehbar.
    """

    def __init__(self, ip_address: str):
        self._ip_address = ip_address
        self._port = 8080

    def renew_ip(self, new_ip: str) -> bool:
        """Prüft die neue IP und übernimmt sie. Gibt True bei Erfolg zurück."""
        if not self._is_company_address(new_ip):
            print(f"Abgelehnt: {new_ip} ist keine Firmen-Adresse.")
            return False
        print(f"IP geändert von {self._ip_address} zu {new_ip}")
        self._ip_address = new_ip
        return True

    def _is_company_address(self, ip: str) -> bool:
        # Bewusst gekapselt: die Regel ist Implementierungsdetail.
        return ip.startswith("192.168.")

    def get_ip_address(self) -> str:
        """Gibt die aktuelle IP-Adresse zurück."""
        return self._ip_address

    def get_port(self) -> int:
        """Gibt den Port zurück."""
        return self._port

    def __str__(self) -> str:
        return f"NetworkComponent(IP: {self._ip_address}, Port: {self._port})"


class Device:
    """Basisklasse für verwaltete Geräte im Firmennetz.

    Im Vergleich zum N2-Stand hält Device jetzt eine NetworkComponent als
    Attribut (Komposition) statt IP und Port direkt. Beschreibende Felder
    bleiben init-only ohne Getter; der Status bleibt nur lesbar.
    """

    def __init__(self, device_type: str, vendor: str, model: str, ip_address: str):
        self._device_type = device_type
        self._vendor = vendor
        self._model = model
        self._network = NetworkComponent(ip_address)
        self._status = "offline"
        self._active = False
        self._utilization = 0

    def reboot(self) -> None:
        """Startet das Gerät neu und setzt den Laufzeit-Zustand zurück."""
        ip = self._network.get_ip_address()
        print(f"Neustart {self._device_type} {self._model} an {ip}")
        self._status = "online"
        self._active = False
        self._utilization = 0

    def activate(self) -> None:
        """Markiert das Gerät als aktiv."""
        self._active = True

    def set_utilization(self, value: int) -> bool:
        """Setzt die Auslastung in Prozent. Werte außerhalb 0..100 werden abgelehnt."""
        if value < 0 or value > 100:
            print(f"Abgelehnt: Auslastung {value}% liegt außerhalb 0..100.")
            return False
        self._utilization = value
        return True

    def get_status(self) -> str:
        """Gibt den aktuellen Status zurück (nur lesbar)."""
        return self._status

    def get_utilization(self) -> int:
        """Gibt die aktuelle Auslastung in Prozent zurück."""
        return self._utilization

    def is_active(self) -> bool:
        """Gibt zurück, ob das Gerät als aktiv markiert ist."""
        return self._active

    def get_network(self) -> NetworkComponent:
        """Gibt die eingebettete Netzwerkschnittstelle zurück."""
        return self._network

    def monitor(self) -> str:
        """Liefert eine kompakte Statuszeile für die Überwachung."""
        return (
            f"[{self._device_type} {self._model}] "
            f"Status: {self._status} | Auslastung: {self._utilization}%"
        )

    def __str__(self) -> str:
        return (
            f"{self._device_type} - {self._vendor} {self._model} | "
            f"IP: {self._network.get_ip_address()} | Status: {self._status} | "
            f"Aktiv: {self._active} | Auslastung: {self._utilization}%"
        )


class Printer(Device):
    """Bürodrucker; spezialisiert Device um die Tonerverwaltung."""

    def __init__(self, vendor: str, model: str, ip_address: str):
        super().__init__("Drucker", vendor, model, ip_address)
        self._toner_percent = 100

    def use_toner(self, amount: int) -> None:
        """Reduziert den Tonerstand um den angegebenen Prozentwert."""
        self._toner_percent = self._toner_percent - amount

    def monitor(self) -> str:
        """Erweitert die Monitoring-Zeile um den Tonerstand."""
        return super().monitor() + f" | Toner: {self._toner_percent}%"

    def __str__(self) -> str:
        return super().__str__() + f" | Toner: {self._toner_percent}%"


# ---------------------------------------------------------------------------
# TODO C1 — Eigene Klasse mit Komposition und monitor()
#
# Entwerfen Sie eine Klasse, die NetworkComponent per Komposition nutzt und
# NICHT von Device erbt. Wählen Sie ein realistisches Szenario aus dem
# IT-Umfeld (z. B. Raumsensor, IP-Telefon, Türverriegelung, Smart-Display).
#
# Anforderungen:
#   - mindestens drei Attribute, davon eines self._network: NetworkComponent
#   - mindestens eine Methode, die den Zustand des Objekts sinnvoll ändert
#   - get_network() für den Lese-Zugriff auf die Netzwerk-Komponente
#   - eine Methode monitor() -> str, die eine kompakte Status-Zeile für die
#     Überwachung liefert (Format frei, aber sprechend)
#   - sprechende __str__-Repräsentation
#
# Schreiben Sie Ihre Klasse unterhalb dieser Zeile.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Optional — TODO C4 ✦ Bonus
# Wandeln Sie für Ihre eigene Klasse oder für Device einen Getter/Setter in
# das pythonische @property-Pattern um. Recherchieren Sie selbständig, wie
# @property und der zugehörige @<name>.setter funktionieren.
# ---------------------------------------------------------------------------


def main() -> None:
    """Demo zum N3-Stand. Drucker funktioniert sofort; Ihre eigene Klasse
    und die Monitoring-Tour ergänzen Sie selbst.
    """
    printer = Printer("HP", "LaserJet Pro", "192.168.10.42")
    printer.activate()
    printer.set_utilization(35)
    printer.use_toner(7)
    print(printer)

    print()
    print("--- Detail-Verbergen über Komposition ---")
    printer.get_network().renew_ip("10.0.0.5")
    printer.get_network().renew_ip("192.168.10.99")
    print(printer)

    # TODO C1: Erzeugen Sie eine Instanz Ihrer eigenen Klasse und geben Sie sie aus.
    # my_thing = ...
    # print(my_thing)

    # TODO C2: Monitoring-Tour
    # Bauen Sie eine Liste mit dem Drucker und Ihrer eigenen Klasse.
    # Iterieren Sie über die Liste und rufen Sie monitor() für jedes Element auf.
    # Achtung: jedes Objekt muss eine monitor()-Methode haben — sonst gibt es
    # zur Laufzeit einen AttributeError.
    #
    # ueberwachung = [printer, my_thing]
    # print()
    # print("--- Monitoring-Tour ---")
    # for ding in ueberwachung:
    #     print(ding.monitor())


if __name__ == "__main__":
    main()
