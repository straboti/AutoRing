from machine import Pin
from time import sleep
from lcdDriver import *

lcdOR = 0

def lcdOverRide(onoff):
    global lcdOR
    lcdOR = onoff
def printToLcd(text1,text2):
    global lcdOR
    if lcdOR == 1:
        pass
    elif lcdOR == 0:
        printToLcdRaw(text1,text2)