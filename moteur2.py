import time
import RPi.GPIO as GPIO
import subprocess

DIRG_PIN = 27
DIRD_PIN = 23
VITG_PIN = 22
VITD_PIN = 17

def moteur_init():   
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.OUT)
    GPIO.setup(23,GPIO.OUT)

    GPIO.setup(22,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)

def ir_init():
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
    GPIO.add_event_detect(infrarouge1,GPIO.FALLING,callback=IR_callback,bouncetime=300)
    GPIO.add_event_detect(infrarouge2,GPIO.FALLING,callback=IR_callback,bouncetime=300)
    GPIO.add_event_detect(infrarouge3,GPIO.FALLING,callback=IR_callback,bouncetime=300)
    GPIO.add_event_detect(infrarouge4,GPIO.FALLING,callback=IR_callback,bouncetime=300)

def IR_callback(channel):
    print("Obstscle détecté!Nous sommes dans l'interruption!")
    
ir_init()
moteur_init()
while True:
    commande = input("com: ").strip()
    
        
    if commande == "w":
        DirG = True
        DirD = True
        VitG = True
        VitD = True
        GPIO.output(DIRG_PIN,True)
        GPIO.output(VITD_PIN,True)
        GPIO.output(VITG_PIN,True)
        GPIO.output(DIRD_PIN,True)
        
    elif commande == "s":
        DirD = True
        VitD = True
        VitG = False
        DirG = False
        GPIO.output(DIRD_PIN,True)
        GPIO.output(VITD_PIN,True)
        GPIO.output(VITG_PIN,False)
        GPIO.output(DIRG_PIN,False)
        
    elif commande == "a":
        DirG = True
        VitD = False
        GPIO.output(DIRG_PIN,True)
        GPIO.output(VITD_PIN ,False)
        
    elif commande == "d":  
        DirG = False
        VitD = True
        GPIO.output(DIRG_PIN,False)
        GPIO.output(VITD_PIN ,True)
        
        
    elif commande == "q":     
        DirG = False
        DirD = False
        VitG = False
        VitD = False
        GPIO.output(DIRG_PIN,False)
        GPIO.output(VITD_PIN,False)
        GPIO.output(VITG_PIN,False)
        GPIO.output(DIRD_PIN,False)
         




         


