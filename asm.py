def run():
    import re
    import util
    import mm
    import const

    #keywords (can't be used for labels)
    ops={"hlt":"00", "ld":"01", "sto":"02", "ld#":"03", "ldi":"04", "add":"05", "sub":"06", 
           "mul":"07", "div":"08", "jmp":"10", "jz":"11", "0":"00"}
    lookup={"r0":0,"r1":1,"r2":2,"r3":3,"r4":4,"r5":5,"r6":6,"r7":7,"r8":8,"r9":9}
    adres=dict()

    # assembly file
    filename = const.filename
    asm = util.getAsm(filename)
    mml = util.getMml(filename)
    # address to start the instructions in memory
    startaddr = 100

    def pass1():
        with open(asm) as f:
            lines = f.readlines()
        lineno = startaddr
        for line in lines:
            tokens = line.split()
            if len(tokens) > 0:
                if tokens[0] not in ops.keys():
                    adres[tokens[0]] = "%03d"%lineno
                lineno = lineno + 1
        f.close()

    def pass2():
        with open(asm) as f:
            lines = f.readlines()
        out = open(mml,"w")
        lineno=startaddr
        try:
            for line in lines:
                tokens = re.split('\s+|\s*,\s*',line)
                if len(tokens) > 0:
                    if tokens[0] not in ops.keys():
                        tokens = tokens[1:]

                    # parse the instruction
                    op = tokens[0]
                    assert op in ops.keys() or util.isInt(op)
                    assert len(tokens) > 1
                    instr = tokens[1:]
                    out.write("%03d"%lineno+" ")
                    if op in ops.keys():
                        out.write(ops[op])
                    
                    if op == "hlt" or op == "0":
                        out.write("0000")
                    elif op == "ld" or op == "sto" or op == "jz":
                        assert len(instr) > 1
                        assert instr[0] in lookup.keys()
                        assert instr[1] in adres.keys()
                        out.write("%1d"%lookup[instr[0]])
                        out.write(adres[instr[1]])
                    elif op == "ld#":
                        assert len(instr) > 1
                        assert instr[0] in lookup.keys()
                        out.write("%1d"%lookup[instr[0]])
                        if util.isInt(instr[1]):
                            out.write("%03d"%int(instr[1]))
                        else:
                            assert instr[1] in adres.keys()
                            out.write(adres[instr[1]])
                    elif op=="ldi" or op=="add" or op=="sub" or op=="mul" or op=="div":
                        assert len(instr) > 1
                        assert instr[0] in lookup.keys()
                        assert instr[1] in lookup.keys()
                        out.write("%1d00"%lookup[instr[0]])
                        out.write("%1d"%lookup[instr[1]])
                    elif op == "jmp":
                        assert len(instr) > 0
                        assert instr[0] in adres.keys()
                        out.write("0"+adres[instr[0]])
                    elif util.isInt(op):
                        out.write("%06d"%int(op))
                    else:
                        print "invalid instruction on line " + str(lineno-startaddr)

                    # put the assembly as a comment at the end of the line
                    out.write("    ")
                    out.write(line+"\n")

                    lineno = lineno + 1
        except Exception:
            print "bad instruction on line " + str(lineno-startaddr)
        finally:
            f.close
            out.close

    pass1()
    pass2()
    mm.run(filename)
