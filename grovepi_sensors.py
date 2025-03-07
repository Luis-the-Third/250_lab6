import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
setText("")
string = ""

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    

    distance = grovepi.ultrasonicRead(ultrasonic_ranger)


    # TODO: read threshold from potentiometer
    threshold = grovepi.analogRead(potentiometer)

    # TODO: format LCD text according to threshold
    
    if(distance > threshold):
      setRGB(255, 0, 0)
      string = "D: " + str(distance) + "cm  OBJ\nT: " + str(threshold) + "cm"

    else:
      setRGB(0, 255, 0)
      string = "D: " + str(distance) + "cm  NO OBJ\nT: " + str(threshold) + "cm"


    time.sleep(1)
    setText(string)




  
    
  except IOError:
    print("Error")
