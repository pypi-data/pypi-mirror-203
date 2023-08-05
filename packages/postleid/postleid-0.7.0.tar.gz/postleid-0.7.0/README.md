# Postleid

Skript zum Korrigieren von Postleitzahlen in Excel-Dateien

Es werden Postleitzahlenregeln für 187 Länder unterstützt
(siehe countries.txt).

## Installation

_in einem Virtual Environment_

```
pip install -U postleid
```

## Benutzung

Korrigieren von Postleitzahlen mit `postleid fix …`

Optionen lt. Hilfeaufruf (`postleid fix …`):

```
Aufruf: postleid fix [-h] [-o AUSGABEDATEI] [-s EINSTELLUNGSDATEI] EXCELDATEI

Postleitzahlen in Excel-Dateien korrigieren

Positionsparameter:
  EXCELDATEI            die Original-Exceldatei

Optionen:
  -h, --help            diese Meldung anzeigen und beenden
  -o AUSGABEDATEI, --output-file AUSGABEDATEI
                        die Ausgabedatei (Standardwert: Name der Original-
                        Exceldatei mit vorangestelltem 'fixed-')
  -s EINSTELLUNGSDATEI, --settings-file EINSTELLUNGSDATEI
                        die Datei mit Benutzereinstellungen (Standardwert:
                        postleid-settings.yaml im aktuellen Verzeichnis)

```
