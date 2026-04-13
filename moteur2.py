import time
import RPi.GPIO as GPIO
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

GPIO.setup(22,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)

while True:
    commande = input("com: ").strip()
    
        
    if commande == "w":
        GPIO.output(27,True)
        GPIO.output(17,True)
        GPIO.output(22,True)
        GPIO.output(23,True)
        
    elif commande == "s":
        GPIO.output(23,True)
        GPIO.output(17,True)
        GPIO.output(22,False)
        GPIO.output(27,False)
        
    elif commande == "a":
        GPIO.output(27,True)
        GPIO.output(17,False)
        
    elif commande == "d":
        GPIO.output(27,False)
        GPIO.output(17,True)
        
    elif commande == "q":
        GPIO.output(27,False)
        GPIO.output(17,False)
        GPIO.output(22,False)
        GPIO.output(23,False)
        
         


