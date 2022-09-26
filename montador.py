
def regToBin(registrador):
    if registrador == "$zero":
        return 0
    if registrador == "$s0" or registrador == "$16":
        return 16
    if registrador == "$s1" or registrador == "$17":
        return 17
    if registrador == "$s2" or registrador == "$18":
        return 18
    if registrador == "$s3" or registrador == "$19":
        return 19
    if registrador == "$s4" or registrador == "$20":
        return 20
    if registrador == "$s5" or registrador == "$21":
        return 21
    if registrador == "$s6" or registrador == "$22":
        return 22
    if registrador == "$s7" or registrador == "$23":
        return 23
    if registrador == "$t0" or registrador == "$8":
        return 8
    if registrador == "$t1" or registrador == "$9":
        return 9
    if registrador == "$t2" or registrador == "$10":
        return 10
    if registrador == "$t3" or registrador == "$11":
        return 11
    if registrador == "$t4" or registrador == "$12":
        return 12
    if registrador == "$t5" or registrador == "$13":
        return 13
    if registrador == "$t6" or registrador == "$14":
        return 14
    if registrador == "$t7" or registrador == "$15":
        return 15


def asmtobin(fun, Bins, labels, inL):
    args = []
    theaddress = 4194304
    for lines in fun:
        lines = lines.replace(',', '').replace('(', ' ')\
            .replace(')', ' ').split()
        args.append(lines)
    print(args)
    opcode = 0
    func = 0
    rd = 0
    rs = 0
    rt = 0
    shamt = 0
    imm = 0
    adress = 0
    numeroEmBinario = 0
    for lines in args:
        if (lines[0] == "sll"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 0
            rd = regToBin(lines[1])
            rs = regToBin(lines[2])
            rt = 0
            shamt = regToBin(lines[3])
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        if (lines[0] == "srl"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 2
            rd = regToBin(lines[1])
            rs = 0
            rt = regToBin(lines[2])
            shamt = regToBin(lines[3])
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "add"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 32
            rd = regToBin(lines[1])
            rs = regToBin(lines[2])
            rt = regToBin(lines[3])
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "sub"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 34
            rd = regToBin(lines[1])
            rs = regToBin(lines[2])
            rt = regToBin(lines[3])
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "and"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 36
            rd = regToBin(lines[1])
            rs = regToBin(lines[2])
            rt = regToBin(lines[3])
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "or"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 37
            rd = regToBin(lines[1])
            rs = regToBin(lines[2])
            rt = regToBin(lines[3])
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "jr"):
            if (len(lines) != 1):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 8
            rd = 0
            rs = regToBin(lines[1])
            rt = 0
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "mfhi"):
            if (len(lines) != 1):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 16
            rd = regToBin(lines[1])
            rs = 0
            rt = 0
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "mflo"):
            if (len(lines) != 1):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 18
            rd = 0
            rs = regToBin(lines[1])
            rt = 0
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "mult"):
            if (len(lines) != 3):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 24
            rd = 0
            rs = regToBin(lines[1])
            rt = regToBin(lines[2])
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "multu"):
            if (len(lines) != 3):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 25
            rd = 0
            rs = regToBin(lines[1])
            rt = regToBin(lines[2])
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "div"):
            if (len(lines) != 3):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 26
            rd = 0
            rs = regToBin(lines[1])
            rt = regToBin(lines[2])
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "divu"):
            if (len(lines) != 3):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 27
            rd = 0
            rs = regToBin(lines[1])
            rt = regToBin(lines[2])
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "addu"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 33
            rd = regToBin(lines[1])
            rs = regToBin(lines[2])
            rt = regToBin(lines[3])
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "subu"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 35
            rd = regToBin(lines[1])
            rs = regToBin(lines[2])
            rt = regToBin(lines[3])
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "slt"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 42
            rd = regToBin(lines[1])
            rs = regToBin(lines[2])
            rt = regToBin(lines[3])
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "sltu"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 0
            func = 43
            rd = regToBin(lines[1])
            rs = regToBin(lines[2])
            rt = regToBin(lines[3])
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "mul"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 28
            func = 2
            rd = regToBin(lines[1])
            rs = regToBin(lines[2])
            rt = regToBin(lines[3])
            shamt = 0
            numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "beq"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 4
            rt = regToBin(lines[2])
            rs = regToBin(lines[1])
            for i in range(len(labels)):
                if labels[i] == lines[3]:
                    imm = negative(lines[3])
                    numeroEmBinario = bin(opcode << 26 | rt << 21 | rs << 16)
                    numeroEmBinario = numeroEmBinario[2:15]+imm
                    numeroEmBinario = Formated(numeroEmBinario)
            Bins.append(numeroEmBinario)
        elif (lines[0] == "bne"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 5
            rt = regToBin(lines[2])
            rs = regToBin(lines[1])
            if labels[i] == lines[1]:
                imm = negative(lines[3])
                numeroEmBinario = bin(opcode << 26 | rt << 21 | rs << 16)
                numeroEmBinario = numeroEmBinario[2:15]+imm
                numeroEmBinario = Formated(numeroEmBinario)

            Bins.append(numeroEmBinario)
        elif (lines[0] == "addiu"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 9
            rt = regToBin(lines[1])
            rs = regToBin(lines[2])
            imm = int(lines[3])
            numeroEmBinario = FamilyI(opcode, rt, rs, imm)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "addi"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 8
            rt = regToBin(lines[1])
            rs = regToBin(lines[2])
            imm = int(lines[3])
            numeroEmBinario = FamilyI(opcode, rt, rs, imm)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "slti"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 10
            rt = regToBin(lines[1])
            rs = regToBin(lines[2])
            imm = int(lines[3])
            numeroEmBinario = FamilyI(opcode, rt, rs, imm)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "sltiu"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 11
            rt = regToBin(lines[1])
            rs = regToBin(lines[2])
            imm = int(lines[3])
            numeroEmBinario = FamilyI(opcode, rt, rs, imm)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "andi"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 12
            rt = regToBin(lines[1])
            rs = regToBin(lines[2])
            imm = int(lines[3])
            numeroEmBinario = FamilyI(opcode, rt, rs, imm)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "ori"):
            if (len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 13
            rt = regToBin(lines[1])
            rs = regToBin(lines[2])
            imm = int(lines[3])
            numeroEmBinario = FamilyI(opcode, rt, rs, imm)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "lui"):
            if (len(lines) != 3):
                return 0, 0, 0, 0, 0, 0
            opcode = 15
            rt = regToBin(lines[1])
            rs = 0
            imm = regToBin(lines[2])
            numeroEmBinario = FamilyI(opcode, rt, rs, imm)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "lw"):
            if (args[-1] == ''):
                args = args[0:-1]
            if (len(lines) != 3 and len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 35
            rt = regToBin(lines[1])
            rs = regToBin(lines[3])
            imm = regToBin(lines[2])
            numeroEmBinario = FamilyI(opcode, rt, rs, imm)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "sw"):
            if (args[-1] == ''):
                args = args[0:-1]
            if (len(lines) != 3 and len(lines) != 4):
                return 0, 0, 0, 0, 0, 0
            opcode = 43
            rt = regToBin(lines[1])
            rs = regToBin(lines[3])
            imm = regToBin(lines[2])
            numeroEmBinario = FamilyI(opcode, rt, rs, imm)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        elif (lines[0] == "j"):
            if (len(lines) != 2):
                return 0, 0, 0, 0, 0, 0
            opcode = 3
            for i in range(len(labels)):
                if labels[i] == lines[1]:
                    address = (inL[i])/4
                    address = bin(int(address)).zfill(26)
                    address = address.replace("b", "0")
            numeroEmBinario = bin(opcode << 26 | int(address, 2))
            Bins.append(numeroEmBinario)
        elif (lines[0] == "jal"):
            if (len(lines) != 2):
                return 0, 0, 0, 0, 0, 0
            opcode = 2
            for i in range(len(labels)):
                if labels[i] == lines[1]:
                    address = (inL[i])/4
                    if address.find('-') != -1:
                        negative(imm)
                    else:
                        address = address.replace("b", "0")
            numeroEmBinario = FamilyJ(opcode, adress)
            numeroEmBinario = Formated(numeroEmBinario[2:])
            Bins.append(numeroEmBinario)
        else:
            return 0
        theaddress += 4


def bintohex(numeroEmBinario):
    num = int(numeroEmBinario, 2)
    return format(num, 'x')


def FamilyR(opcode, rt, rs, rd, func, shamt):
    nb = bin(opcode << 26 | rs << 21 | rt << 16 | rd << 11 | shamt << 6 | func)
    return nb


def FamilyI(opcode, rt, rs, imm):
    nb = bin(opcode << 26 | rs << 21 | rt << 16 | int(imm))
    return nb


def FamilyJ(opcode, adress):
    nb = bin(opcode << 26 | adress)
    return nb


def Formated(nb):
    nb_new = len(nb)
    a = 32-nb_new
    return (("0"*a)+nb)


def negative(bi):
    s = bin(bi & int("1"*16, 2))[2:]
    return ("{0:0>%s}" % (16)).format(s)
