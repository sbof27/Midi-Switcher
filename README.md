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
```

### Verwendete Hardware
#### Microcontroller
ESP IDF ESP32-S3-WROOM-1 N8R2 N16R8 44Pin Typ-C 8M PSRAM ESP32 S3
![grafik](https://github.com/user-attachments/assets/50c4f84c-c387-48bf-b7e6-bd904acaf6c0)


### Display Driver
Dies ist der verwendete Display Treiber: https://github.com/russhughes/st7789_mpy
