import st7789
import machine
import time

class DisplayManager:
    # Segmentdefinition für 7-Segment-Anzeige
    SEGMENTS = {
        '0': [1, 1, 1, 1, 1, 1, 0],
        '1': [0, 1, 1, 0, 0, 0, 0],
        '2': [1, 1, 0, 1, 1, 0, 1],
        '3': [1, 1, 1, 1, 0, 0, 1],
        '4': [0, 1, 1, 0, 0, 1, 1],
        '5': [1, 0, 1, 1, 0, 1, 1],
        '6': [1, 0, 1, 1, 1, 1, 1],
        '7': [1, 1, 1, 0, 0, 0, 0],
        '8': [1, 1, 1, 1, 1, 1, 1],
        '9': [1, 1, 1, 1, 0, 1, 1]
    }

    def __init__(self, spi, cs_pin, reset_pin, rotation=1, width=170, height=320):
        self.cs_pin = cs_pin
        self.reset_pin = reset_pin
        self.spi = spi
        self.display = st7789.ST7789(
            spi,
            width=width,
            height=height,
            reset=reset_pin,
            dc=machine.Pin(2, machine.Pin.OUT),
            cs=cs_pin,
            backlight=machine.Pin(5, machine.Pin.OUT),
            rotation=rotation
        )
        self.display.fill(st7789.color565(0, 0, 0))  # Hintergrund schwarz

    def activate(self):
        """CS aktivieren."""
        self.cs_pin.off()
        time.sleep(0.01)  # Sicherheitspuffer
        print(f"Display ({self.cs_pin}): CS aktiviert")

    def deactivate(self):
        """CS deaktivieren."""
        time.sleep(0.01)  # Sicherheitspuffer
        self.cs_pin.on()
        print(f"Display ({self.cs_pin}): CS deaktiviert")

    def clear(self, color=st7789.color565(0, 0, 0)):
        """Löscht das Display."""
        self.activate()
        self.display.fill(color)
        self.deactivate()

    def draw_number(self, x, y, number, length, thickness, fg_color, bg_color):
        """Zeichnet eine mehrstellige Zahl im 7-Segment-Stil."""
        self.activate()
        spacing = length // 4
        for i, digit in enumerate(str(number)):
            self._draw_digit(x + i * (length + spacing), y, digit, length, thickness, fg_color, bg_color)
        self.deactivate()

    def _draw_digit(self, x, y, digit, length, thickness, fg_color, bg_color):
        """Zeichnet eine einzelne Ziffer basierend auf den Segmentdaten."""
        segments = self.SEGMENTS.get(digit, [0] * 7)
        overlap = thickness // 2

        # Position der Segmente
        positions = [
            (x, y, 'h'),  # Segment 0: Oben horizontal
            (x + length - thickness, y, 'v'),  # Segment 1: Rechts oben vertikal
            (x + length - thickness, y + length + overlap, 'v'),  # Segment 2: Rechts unten vertikal
            (x, y + 2 * length, 'h'),  # Segment 3: Unten horizontal
            (x, y + length, 'v'),  # Segment 4: Links unten vertikal
            (x, y + thickness, 'v'),  # Segment 5: Links oben vertikal
            (x, y + length, 'h')  # Segment 6: Mitte horizontal
        ]

        # Segmente zeichnen
        for idx, segment in enumerate(segments):
            pos_x, pos_y, orientation = positions[idx]
            color = fg_color if segment else bg_color
            self._draw_segment(pos_x, pos_y, length, thickness, orientation, color)

    def _draw_segment(self, x, y, length, thickness, orientation, color):
        """Zeichnet ein Segment."""
        if orientation == 'h':  # Horizontal
            self.display.fill_rect(x, y, length, thickness, color)
        elif orientation == 'v':  # Vertikal
            self.display.fill_rect(x, y, thickness, length, color)

    def draw_text(self, x, y, text, font, fg_color, bg_color):
        """Zeichnet Text."""
        self.activate()
        self.display.text(font, text, x, y, fg_color, bg_color)  # Schriftart direkt verwenden
        self.deactivate()
