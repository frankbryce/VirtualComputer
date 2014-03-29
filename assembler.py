# command line arguments
# python compiler.py <file to run>
import sys
import os.path

def run(filename):
    filename = os.path.abspath(filename)
    if not os.path.isfile(filename):
        print "Error: " + filename + " does not exist "
        sys.exit(0)

    # get absolute path
    fname, ext = os.path.splitext(filename)

    # add include directory to python path for this session
    sys.path.insert(0, os.path.abspath("inc"))


    if ext == ".asm":
        print ".asm execution not implemented"
    elif ext == ".mm": # mm assembly language
        from asm import asm
        from mm import mm
        asm.run(fname + ext, fname + ".mml")
        mm.run(fname + ".mml")
    elif ext == ".mml":
        # run the .mml file
        from mm import mm
        mm.run(fname + ext)
    else:
        print "Error: unknown file extension \"" + ext + "\""

