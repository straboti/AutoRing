from machine import Pin
from time import sleep
from memoryLib import *
from lcdLib import *

b1Raw = Pin(3, Pin.IN, Pin.PULL_UP)
b2Raw = Pin(4, Pin.IN, Pin.PULL_UP)
b3Raw = Pin(5, Pin.IN, Pin.PULL_UP)
bigButtonRaw = Pin(6, Pin.IN, Pin.PULL_UP)
debugRaw = Pin(10, Pin.IN, Pin.PULL_UP)
b1Trigger = 0
b2Trigger = 0
b3Trigger = 0
bigButtonTrigger = 0
cFolder = "e0"

def buttonPressed(b):
    global cFolder
    #data = folderNav(cFolder,b)
    #cFolder = data[1]
    #printToLcd(data[0],"")
def sensorRefresh():
    global b1
    global b2
    global b3
    global bigButton
    global sw
    global debug
    debug = int(not(debugRaw).value())
    b1 = int(not(b1Raw).value())
    b2 = int(not(b2Raw).value())
    b3 = int(not(b3Raw).value())
    bigButton = int(not(debugRaw).value())
    if debug == 1:
        print("sensorUpdate")
def inputsRefresh():
    global bigButtonTrigger;
    global bigButton;
    global b1Trigger;
    global b1;
    global b2Trigger;
    global b2
    global b3Trigger;
    global b3;
    if b1 == 1:
        b1Trigger = 1
    elif b1Trigger == 1:
        buttonPressed(1)
        b1Trigger = 0
    if b2 == 1:
        b2Trigger = 1
    elif b2Trigger == 1:
        buttonPressed(2)
        b2Trigger = 0
    if b3 == 1:
        b3Trigger = 1
    elif b3Trigger == 1:
        buttonPressed(3)
        b3Trigger = 0
    if bigButton == 1:
        bigButtonTrigger = 1
    elif bigButtonTrigger == 1:
        buttonPressed(4)