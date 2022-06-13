#!/bin/python 
# Apagar Raspberry con un Botón en los terminales 8 y GND. El terminal 8 es el GPIO14.
import RPi.GPIO as GPIO  
import time  
import os  

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)  

def Apagar(channel):  
   os.system("sudo shutdown -h now")  

GPIO.add_event_detect(11, GPIO.FALLING, callback = Apagar, bouncetime = 2000)  

while 1:  
   time.sleep(1) 
