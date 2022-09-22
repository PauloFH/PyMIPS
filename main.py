class main:
    asm = open("Assembly.asm")
    LineAsm = asm.readlines()
    args = []
    for x in range(len(LineAsm)):
        LineAsm[x]
        if (LineAsm[x] != ""):
            args.append(LineAsm[x])
        print(args[x])
        print()