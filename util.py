def isInt(s):
    try:
        int(s)
        return True
    except:
        return False

def getAsm(fn):
    return "asmcode/"+fn+".asm"

def getMml(fn):
    return "assemblies/"+fn+".mml"
