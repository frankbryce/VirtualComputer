def halt(memory,registers,mmm,r,s,iReg):
    #print("Program Halting")
    return -1

def lwi(memory,registers,mmm,r,s,iReg):
    #print "Load from Memory with immediate address"
    registers[r] = memory[mmm]
    return iReg+1
    
def swi(memory,registers,mmm,r,s,iReg):
    #print "Store to Memory with immediage address"
    memory[mmm] = registers[r]
    return iReg+1

def li(memory,registers,mmm,r,s,iReg):
    #print "Load with immediate"
    registers[r] = mmm
    return iReg+1

def lwr(memory,registers,mmm,r,s,iReg):
    #print "Load from memory with address in register"
    registers[r] = memory[registers[s]]
    return iReg+1

def add(memory,registers,mmm,r,s,iReg):
    #print "add"
    registers[r] = registers[r] + registers[s]
    return iReg+1

def sub(memory,registers,mmm,r,s,iReg):
    #print "sub"
    registers[r] = registers[r] - registers[s]
    return iReg+1

def mul(memory,registers,mmm,r,s,iReg):
    #print "mul"
    registers[r] = registers[r] * registers[s]
    return iReg+1

def div(memory,registers,mmm,r,s,iReg):
    #print "div"
    registers[r] = registers[r] / registers[s]
    return iReg+1

def ji(memory,registers,mmm,r,s,iReg):
    #print "jump immediate"
    return mmm

def jci(memory,registers,mmm,r,s,iReg):
    #print "jump conditional immediate"
    if (registers[r] == 0):
        return mmm
    else:
        return iReg+1

arr = []
arr.append(halt)
arr.append(lwi)
arr.append(swi)
arr.append(li)
arr.append(lwr)
arr.append(add)
arr.append(sub)
arr.append(mul)
arr.append(div)
arr.append(ji)
arr.append(jci)

