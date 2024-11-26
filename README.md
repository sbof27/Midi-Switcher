# Midi-Switcher

## Projekt-Struktur
```plaintext
Midi-Switcher
│
├── docs/                # Projekt-Dokumentation (z. B. README, technische Details)
├── firmware/            # Code für den ESP32-S3
│   ├── midi/            # MIDI-spezifische Logik
│   ├── display/         # Code für die Benutzeroberfläche
│   └── network/         # Wi-Fi- oder Bluetooth-Funktionen
├── app/                 # Falls eine App/Webinterface entwickelt wird
├── hardware/            # Schaltpläne, Layouts und technische Daten
└── tests/               # Test-Skripte und Simulationen
`

### Display Driver
Dies ist der verwendete Display Treiber: https://github.com/russhughes/st7789_mpy
