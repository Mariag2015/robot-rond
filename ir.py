import RPi.GPIO as GPIO
import time

led = 18
infrarouge1 = 6
infrarouge2 = 12
infrarouge3 = 14
infrarouge4 = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)

GPIO.setup(infrarouge1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(infrarouge2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(infrarouge3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(infrarouge4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def IR_callback(channel):
    print("Obstscle détecté!Nous sommes dans l'interruption!")
    
GPIO.add_event_detect(infrarouge1,GPIO.FALLING,callback=IR_callback,bouncetime=300)
GPIO.add_event_detect(infrarouge2,GPIO.FALLING,callback=IR_callback,bouncetime=300)
GPIO.add_event_detect(infrarouge3,GPIO.FALLING,callback=IR_callback,bouncetime=300)
GPIO.add_event_detect(infrarouge4,GPIO.FALLING,callback=IR_callback,bouncetime=300)
try:
    print("En attente du bouton...")
    while True: #Sans arrêt
        time.sleep(1)
except KeyboardInterrupt:
    print("Fin")
finally:
    GPIO.cleanup()