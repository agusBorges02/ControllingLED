import RPi.GPIO as GPIO
import time

# Configuración del GPIO de la Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # El pin GPIO 17 controla el relé

# Activar el relé (encender el LED)
GPIO.output(17, GPIO.HIGH)
time.sleep(5)  # Mantener encendido por 5 segundos

# Desactivar el relé (apagar el LED)
GPIO.output(17, GPIO.LOW)

# Limpieza
GPIO.cleanup()
