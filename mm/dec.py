def op(inst):
    if inst < 10000:
        ret = 0
    elif inst < 20000:
        ret = 1
    elif inst < 30000:
        ret = 2
    elif inst < 40000:
        ret = 3
    elif inst < 50000:
        ret = 4
    elif inst < 60000:
        ret = 5
    elif inst < 70000:
        ret = 6
    elif inst < 80000:
        ret = 7
    elif inst < 90000:
        ret = 8
    elif inst < 100000:
        raise Exception("Invalid instruction: " + inst)
    elif inst < 110000:
        ret = 9
    elif inst >= 110000 and inst < 120000:
        ret = 10
    else:
        raise Exception("Invalid instruction: " + inst)

    return ret

def mmm(inst):
    return inst%1000

def r(inst):
    return (inst%10000)//1000

def s(inst):
    return inst%10
