# global variables
memory = []
registers = []
comment = []
#next instruction
pReg = 0
    
def run(filename):
    # imports
    import inst
    import dec
    import util
    import const
    
    global memory
    global registers
    global pReg
    global comment
    
    #current instruction
    iReg = 0
    # debug flag
    debug = const.debug
    #program file
    prog = util.getMml(filename)

    # display state
    def disp():
        print
        print("The Mythical Machine")
        print
        print("P reg  %06d"%pReg + "      I reg %06d"%iReg)
        print
        print("reg 0  %06d"%registers[0] + "      reg 5  %06d"%registers[5])
        print("reg 1  %06d"%registers[1] + "      reg 6  %06d"%registers[6])
        print("reg 2  %06d"%registers[2] + "      reg 7  %06d"%registers[7])
        print("reg 3  %06d"%registers[3] + "      reg 8  %06d"%registers[8])
        print("reg 4  %06d"%registers[4] + "      reg 9  %06d"%registers[9])

    # initialization function
    def init():
        global memory
        global registers
        global pReg
        global comment
        memory = [0] * 1000
        comment = [''] * 1000
        registers = [0] * 10

        # load the program
        with open(prog) as f:
            program = f.readlines()

        pReg = int(program[0].split()[0])
        for p in program:
            try:
                line = p.split()
                if line.__len__() > 1:
                    memory[int(line[0])] = int(line[1])
                    if line.__len__() > 2:
                        comment[int(line[0])] = " ".join(line[2:len(line)])
            except Exception:
                print "Bad formatting for program: " + prog
                quit()
        

    # add code here to read in assembly program
    #  ... and store instructions in list of strings
    init()

    # add code here to iterate through the list,
    #  executing them

    while True:
        # get next instruction address
        iReg = pReg
        instr = memory[iReg]

        # decode the instruction
        op = dec.op(instr)
        mmm = dec.mmm(instr)
        r = dec.r(instr)
        s = dec.s(instr)

        # display state if debugging
        if debug == 1:
            print
            print(iReg)
            print comment[iReg]
            print(instr)
            print(op)
            print(mmm)
            print(r)
            print(s)
            print

        # execute instruction and get next instruction address
        pReg = inst.arr[op](memory,registers,mmm,r,s,iReg)

        # display state if debugging
        if debug == 1:
            disp()

        # hack to make the program stop
        if pReg == -1:
            iReg = 0
            break

    disp()
