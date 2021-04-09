jelzoFile = open("jelzok.txt", "w")
kicsFile = open("kicsengok.txt", "w")
setFile = open("settings.txt", "w")
folderData = {
    "e0":["Szerkeszto","e0","e1","e0"],
    "e1":["Csengok","e2","e11","e0"],
    "e2":["Beallitasok","e1","e21","e0"],
    "e11":["owr","1"],
    "e21":["Csengok hossza","e22","e212","e2"],
    "e22":["Automata jelzo","e21","e221","e2"],
    "e211":["Jelzo","e212","e2111","e21"],
    "e212":["Kicsengo","e211","e2121","e21"],
    "e221":["BE","e222","e2211","e22"],
    "e2111":["owr","2"]
    }
def folderNav(fld,b):
    readFolder = folderData[fld]
    returnVal = ""
    folder = fld
    if readFolder[0] == "owr":
        if readFolder[1] == "1":
            pass
        else:
            pass
    if b == 1:
        folder = readFolder[1]
    elif b == 2:
        folder = readFolder[2]
    elif b == 3:
        folder = readFolder[3]
    else:
        print("err")
    readFolder = folderData[folder]
    returnVal = [readFolder[0],folder]
    return returnVal
def load(file):
    if file == "s":
        return setFile.read()
    elif file == "j":
        return jelzoFile.read()
    elif file == "k":
        return kicsFile.read()
    else:
        pass
def saveToFile(file,data):
    if file == "s":
        setFile.write(data)
    elif file == "j":
        jelzoFile.write(data)
    elif file == "k":
        kicsFile.write(data)
    else:
        pass
jelzok = load("j")
kicsengok = load("k")
settings = load("s")
def autoSave():
    fileJ = load("j")
    fileK = load("k")
    fileS = load("s")
    global jelzok
    global kicsengok
    global settings
    if jelzok != fileJ:
        save("j")
    if kicsengok != fileK:
        save("k")
    if settings != fileS:
        save("s")
    jelzoFile.close()
    kicsFile.close()
    setFile.close()
    jelzoFile = open("jelzok.txt", "w")
    kicsFile = open("kicsengok.txt", "w")
    setFile = open("settings.txt", "w")
    
        