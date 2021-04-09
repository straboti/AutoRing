import machine
import utime
from time import *

rs = machine.Pin(16,machine.Pin.OUT)
e = machine.Pin(17,machine.Pin.OUT)
d4 = machine.Pin(18,machine.Pin.OUT)
d5 = machine.Pin(19,machine.Pin.OUT)
d6 = machine.Pin(20,machine.Pin.OUT)
d7 = machine.Pin(21,machine.Pin.OUT)

pow1 = machine.Pin(15,machine.Pin.OUT)
pow2 = machine.Pin(22,machine.Pin.OUT)
cont = machine.Pin(14,machine.Pin.OUT)

pow1.on()
pow2.on()
cont.on()

def pulseE():
    e.value(1)
    delayShort()
    e.value(0)
    delayShort()
    
def delayShort():
    utime.sleep_us(40)
    
def delay():
    utime.sleep_ms(2)
    
def delayBig():
    utime.sleep(0.3)

def send2LCD4(BinNum):
    d4.value((BinNum & 0b00000001) >>0)
    d5.value((BinNum & 0b00000010) >>1)
    d6.value((BinNum & 0b00000100) >>2)
    d7.value((BinNum & 0b00001000) >>3)
    pulseE()

def send2LCD8(BinNum):
    d4.value((BinNum & 0b00010000) >>4)
    d5.value((BinNum & 0b00100000) >>5)
    d6.value((BinNum & 0b01000000) >>6)
    d7.value((BinNum & 0b10000000) >>7)
    pulseE()
    d4.value((BinNum & 0b00000001) >>0)
    d5.value((BinNum & 0b00000010) >>1)
    d6.value((BinNum & 0b00000100) >>2)
    d7.value((BinNum & 0b00001000) >>3)
    pulseE()
    
def whichLinePos(line, pos):
    b = 0
    if (line == 1):
        b = 0
    if (line == 2):
        b = 40
    if (line == 3):
        b = 20
    if (line == 4):
        b = 60
    cursorHome()
    for x in range(0,b+pos):
        moveCursorR()

def clearDisplay():#blanks the LCD, needs a long delay.
    rs.value(0)
    send2LCD8(0b00000001)
    rs.value(1)
    delay()        
def cursorHome():#returns the cursor to home, needs a long delay.
    rs.value(0)
    send2LCD8(0b00000010)
    rs.value(1)
    delay()
def cursorMoveForward():
    rs.value(0)
    send2LCD8(0b00000110)
    rs.value(1)
def cursorMoveBack():
    rs.value(0)
    send2LCD8(0b00000100)
    rs.value(1)
def moveCursorR():#write text from left to right
    rs.value(0)
    send2LCD8(0b00010100)
    rs.value(1)
def moveCursorL():#write text from right to left (backwards)
    rs.value(0)
    send2LCD8(0b00010000)
    rs.value(1)
def cursorOff():
    rs.value(0)
    send2LCD8(0b00001100)
    rs.value(1)
def cursorOn():
    rs.value(0)
    send2LCD8(0b00001110)
    rs.value(1)
def blinkOn():
    rs.value(0)
    send2LCD8(0b00001111)
    rs.value(1)
def blinkOff():
    rs.value(0)
    send2LCD8(0b00001100)
    rs.value(1)
def displayShiftR():#move all caractors one space right
    rs.value(0)
    send2LCD8(0b00011100)
    rs.value(1)
def displayShiftL():#move all caractors one space left
    rs.value(0)
    send2LCD8(0b00011000)
    rs.value(1)
def displayOff():
    rs.value(0)
    send2LCD8(0b00001000)
    rs.value(1)
def displayOn():
    rs.value(0)
    send2LCD8(0b00001100)
    rs.value(1)
    
def setUpLCD():
    rs.value(0)
    send2LCD4(0b0011)
    send2LCD4(0b0011)
    send2LCD4(0b0011)
    send2LCD4(0b0010)
    send2LCD8(0b00101000)
    send2LCD8(0b00001100)
    send2LCD8(0b00000110)
    send2LCD8(0b00000001)
    rs.value(1)

setUpLCD()
whichLinePos(1,0)
def printToLcdRaw(txt1,txt2):
    clearDisplay()
    sleep(0.1)
    whichLinePos(1,0)
    for x in txt1:
        send2LCD8(ord(x))
    whichLinePos(2,0)
    for x in txt2:
        send2LCD8(ord(x))
       
