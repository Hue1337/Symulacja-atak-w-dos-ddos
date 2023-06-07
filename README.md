# Dokumentacja

Autor: Mateusz Głuchowski

Strona: github.com/hue1337/Symulacja-ataków-dos-ddos

## Temat projektu:

- Symulacja ataków DoS oraz DDoS.

## Skład grupy projektowej:

- Mateusz Głuchowski- Lider

## Opis zadania symulacji w języku naturalnym:

- Projekt przedstawia symulację ataków DoS oraz DDoS opartą na komunikacji między serwerami i klientami poprzez sockety. Podczas symulacji zbierane są dane odnośnie stanu serwera (ofiary), które można poddać analizie. Projekt ma na celu zwizualizowanie faktycznych ataków z rodziny Denial od Service oraz jaki mają wpływa na zachowanie się serwera (ofiary). Nadmieniam, iż jest to tylko symulacja, a nie faktyczne skrypty DoS oraz DDoS.

## Dokumentacja projektu:

- Diagramy: [link](https://github.com/Hue1337/Symulacja-atak-w-dos-ddos/tree/main/doc/UML)
- Dokumentacja wygenerowana poprzez `pydoc`: [link](https://github.com/Hue1337/Symulacja-atak-w-dos-ddos/tree/main/doc)

## Technologie:

- UML: [cloud.smartdraw.com](https://cloud.smartdraw.com/)
- Język programowania: `Python 3.11.3`
- System operacyjny: `macOS Ventura 13.3.1`

## Instrukcja dla systemów z rodziny `Unix`:

- Pierwsze uruchomienie:
    - `cd src/`
    - `chmod +x first_run.sh`
    - `./first_run.sh`
- Kolejne uruchomienia:
    - `chmod +x run.sh`
    - `./run.sh`

## Struktura projektu:

```jsx
├── README.md
└── src
    ├── after_statistics.py
    ├── attack.py
    ├── attack_interface.py
    ├── client.py
    ├── data
    │   ├── ddos
    │   │   └── <DDOS DATA>
    │   ├── dos
    │   │   └── <DOS DATA>
    │   └── line_charts
    │       ├── ddos
    │       │   └── <DDOS LINE CHARTS>
    │       └── dos
    │           └── <DOS LINE CHARTS>
    ├── ddos.py
    ├── dos.py
    ├── first_run.sh
    ├── main.py
    ├── run.sh
    ├── server.py
    ├── server_interface.py
    ├── settings.py
    └── status.py
```
