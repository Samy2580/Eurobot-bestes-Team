import time
from servo import servo # noch entsprechende library auf dem pico installieren, dient zur vereinfachung der servo steuerung, hier der Link zur Erklärung: https://docs.micropython.org/en/latest/pyboard/tutorial/servo.html
rotationservo1 = Servo(Pin_Id =xy) # Hier noch entsprechende Pin Id einfügen

def servodrehen():
    rotationservo1.write(30) # Setzt den Winkel des Servos auf 30 Grad
    time.sleep(2.0) # Wartet für 2 Sekunden
    rotationservo1.write(60) # Setzt den Winkel des Servos auf 60 Grad
    time.sleep(2.0) # Wartet für 2 Sekunden
    rotationservo1.write(90) # Setzt den Winkel des Servos auf 90 Grad

