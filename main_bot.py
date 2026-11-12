# main_bot.py
# EUROBOT - MAIN PROGRAM
# Version 0.1

from machine import Pin # <- This is the library for controlling the GPIO pins of the Raspberry Pi Pico. The Pi Pico needs to have MicroPython installed for this to work. https://www.raspberrypi.com/documentation/microcontrollers/micropython.html
import time



print("======================")
print("EUROBOT STARTET")
print("======================")

# LED des Raspberry Pi Pico
led = Pin("LED", Pin.OUT)

# mit einem solchen while True loop läuft der einfach für immer; der Rest des Codes wird nicht ausgeführt
# while True:
#    led.toggle()
#
#    print("Eurobot funktioniert!")
#
#    time.sleep(1)

# Bewegen des Bots
spr = 800    # Anzahl Steps pro Umdrehung ? - muss eben verifiziert werden, hardware-abhängig. wird aber wahrscheinlich schon passebn
step = Pin("step", Pin.OUT) # Definieren des Step Pins
dir = Pin("dir", Pin.OUT) # Definieren des Richtungspins
step_count = spr # Anzahl schritte

def uhrzeigerumdrehung(spr, step, dir):
    dir.value(1)    # Setzt Richtungs-Pin auf Im Uhrzeigersinn
    for _ in range(step_count):
        step.value(1)    # Setzt Step-Pin auf 3.3 V
        time.sleep_us(1250)
        step.value(0)    # Setzt Step-Pin auf 0 V
        time.sleep_us(1250)

def gegenuhrzeigerumdrehung(spr, step, dir):
    dir.value(0) # Setzt Richtungs-Pin auf gegen den Uhrzeigersinn
    for _ in range(step_count):
        step.value(1) # Setzt Step-Pin auf 3.3 V
        time.sleep_us(1250)
        step.value(0) # Setzt Step-Pin auf 0 V
        time.sleep_us(1250)


