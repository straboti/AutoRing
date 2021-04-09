from machine import Pin
from time import sleep
from ledLib import *
from lcdLib import *
from inputLib import *
from memoryLib import *

version = "1.0"

print("XXXXXX  XXXXXX  XXXXXX   XXXXXX  X      ")
print("X       X    X  X     X  X    X  X      ")
print("X       X XX X  X     X  X    X  X      ")
print("X       X XX X  XXXXXX   XXXXXX  X      ")
print("X       X    X  X    X   X    X  X      ")
print("XXXXXX  XXXXXX  X     X  X    X  XXXXXX ")
sleep(1)
print("------------------------------")
print("CORAL_SW AutoRing")
print("Kernel V " + version)
print("Program: Strauss Botond")
print("Telefon: +36 30 768 1179")
print("Email: straboti07@gmail.com")
print("A szoftver másolását az 1999 évi LXXVI. tövény védi!")
print("------------------------------")
sleep(1)
print("\n")
print("OLVASÁSHOZ CSAK KAPCSOLD LE A KÓD FUTTATÁSÁT!")
print("import kész")

printToLcd("CORAL Kernel","Strauss Botond")
sleep(2)
pxt1 = "AutoRing V " + version
printToLcd(pxt1,"+36-30-768-1179")
sleep(3)
printToLcd("Rendszerinditas,","kerjuk varjon")
#Logikai változók

debugMode = 0
main = 0
print("debug off")

def stopAll():
    stopLed()
print("stopAll def")
def relay(st):
    if st == "on":
        rel1.on()
        rel2.on()
        rel3.on()
        rel4.on()
    else:
        rel1.off()
        rel2.off()
        rel3.off()
        rel4.off()
print("rel def")
def init():
    sensorRefresh()
    stopAll()
    startMain()
print("init def")
def startMain():
    rgbLed("g","b","g","b")
init()
broadcast("ok")
def cseng(hossz):
    if main == 1:
        if hossz == "r":
            print("csengo be")
            sleep(1)
            print("csengo ki")
        elif hossz == "h":
            print("csengo be")
            sleep(5)
            print("csengo ki")
print("helyi funkciók definiálva")
printToLcd("Rendszer elindul","")
sleep(1)
printToLcd("AutoRing","Fomenu")
main = 1
activityCycle = 1
while True:
    if activityCycle == 10:
       # print("ccl")
        activityCycle = 1
    blink(0.05,0.05)
    sensorRefresh()
    inputsRefresh()
    activityCycle += 1 