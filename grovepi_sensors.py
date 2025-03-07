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

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    distance = grovepi.ultrasonicRead(ultrasonic_ranger)
    setText("Distance: " + str(distance) + "cm")


    # TODO: read threshold from potentiometer
    threshold = grovepi.analogRead(potentiometer)
    setText("Threshold: " + str(threshold) + "cm")

    # TODO: format LCD text according to threshold
    if(distance > threshold):
      setRGB(255, 0, 0)
      setText("OBJ PRES")
    else:
      setRGB(0, 255, 0)
      setText("No obj pres")


  
    
  except IOError:
    print("Error")