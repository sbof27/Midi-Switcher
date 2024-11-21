import machine
from display_manager import DisplayManager
from vga1_16x32 import WIDTH, HEIGHT, FIRST, LAST, _FONT
import st7789

# Schriftart manuell zusammenstellen
vga1_16x32 = {
    'WIDTH': WIDTH,
    'HEIGHT': HEIGHT,
    'FIRST': FIRST,
    'LAST': LAST,
    'FONT': _FONT
}

# Farben definieren
BLACK = st7789.color565(0, 0, 0)
WHITE = st7789.color565(255, 255, 255)

# SPI-Bus initialisieren
spi = machine.SPI(1, baudrate=20000000, polarity=1, phase=1, sck=machine.Pin(18), mosi=machine.Pin(23))

# CS- und Reset-Pins definieren
cs_pin1 = machine.Pin(15, machine.Pin.OUT)
cs_pin2 = machine.Pin(16, machine.Pin.OUT)
reset_pin1 = machine.Pin(4, machine.Pin.OUT)
reset_pin2 = machine.Pin(17, machine.Pin.OUT)

# Displays initialisieren
display1 = DisplayManager(spi, cs_pin1, reset_pin1, rotation=1)
display2 = DisplayManager(spi, cs_pin2, reset_pin2, rotation=1)

# Inhalte für Display 1
display1.clear(BLACK)
display1.draw_number(10, 10, "058", 40, 10, WHITE, BLACK)
display1.draw_text(10, 120, "Clean Tone", vga1_16x32, WHITE, BLACK)

# Inhalte für Display 2
display2.clear(BLACK)
display2.draw_number(10, 10, "002", 40, 10, WHITE, BLACK)
display2.draw_text(10, 120, "Crunch", vga1_16x32, WHITE, BLACK)

print("Beide Displays gezeichnet!")
