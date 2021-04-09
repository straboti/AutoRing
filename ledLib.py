from machine import Pin
from time import sleep

ledR = Pin(0, Pin.OUT)
ledG = Pin(1, Pin.OUT)
ledB = Pin(2, Pin.OUT)
onBoardLed = Pin(25, Pin.OUT)
def stopLed():
    ledR.off()
    ledG.off()
    ledB.off()
    onBoardLed.off()
def rgbLed(a,b,c,d):
    for n in range(4):
        if n == 0:
            currentColor = a
        elif n == 1:  
            currentColor = b
        elif n == 2:
            currentColor = c
        else:
            currentColor = d
        if currentColor == "r":
            ledR.on()
            ledG.off()
            ledB.off()
        elif currentColor == "g":
            ledR.off()
            ledG.on()
            ledB.off()
        elif currentColor == "b":
            ledR.off()
            ledG.off()
            ledB.on()
        else:
            ledR.off()
            ledG.off()
            ledB.off()
        sleep(0.5)
def blink(timeon,timeoff):
    onBoardLed.on()    
    sleep(timeon)
    onBoardLed.off()
    sleep(timeoff)
def broadcast(status):
    if status == "ok":
        rgbLed("g","g","g","g")
    elif status == "regged":
        rgbLed("g","o","g","o")
    elif status == "jelzo":
        rgbLed("g","b","o","b")
    elif status == "kics":
        rgbLed("r","b","o","b")
    elif status == "memdel":
        rgbLed("r","r","r","g")
    else:
        broadcast("ok")