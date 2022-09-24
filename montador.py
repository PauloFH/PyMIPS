import re


def regToBin(registrador):
    if registrador == "$zero":
        return "0"
    if registrador == "$s0" or registrador == "$16":
        return "16"
    if registrador == "$s1" or registrador == "$17":
        return "17"
    if registrador == "$s2" or registrador == "$18":
        return "18"
    if registrador == "$s3" or registrador == "$19":
        return "19"
    if registrador == "$s4" or registrador == "$20":
        return "20"
    if registrador == "$s5" or registrador == "$21":
        return "21"
    if registrador == "$s6" or registrador == "$22":
        return "22"
    if registrador == "$s7" or registrador == "$23":
        return "23"
    if registrador == "$t0" or registrador == "$8":
        return "8"
    if registrador == "$t1" or registrador == "$9":
        return "9"
    if registrador == "$t2" or registrador == "$10":
        return "10"
    if registrador == "$t3" or registrador == "$11":
        return "11"
    if registrador == "$t4" or registrador == "$12":
        return "12"
    if registrador == "$t5" or registrador == "$13":
        return "13"
    if registrador == "$t6" or registrador == "$14":
        return "14"
    if registrador == "$t7" or registrador == "$15":
        return "15"


def asmtobin(asm):
    for lines in asm:
        asm_split = re.split()
    args = []
    for i in range(len(asm_split)):
        if asm_split[i] != "":
            args.append(asm_split[i])
    opcode = 0
    func = 0
    rd = 0
    rs = 0
    rt = 0
    shamt = 0
    imm = 0
    adress = 0
    numeroEmBinario = 0
    if (args[0] == "sll"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 0
        rd = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        rt = 0
        shamt = regToBin(args[1][3])
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    if (args[0] == "srl"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 2
        rd = regToBin(args[1][1])
        rs = 0
        rt = regToBin(args[1][2])
        shamt = regToBin(args[1][3])
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "add"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 32
        rd = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        rt = regToBin(args[1][3])
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "sub"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 34
        rd = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        rt = regToBin(args[1][3])
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "and"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 36
        rd = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        rt = regToBin(args[1][3])
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "or"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 37
        rd = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        rt = regToBin(args[1][3])
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "jr"):
        if (len(args) != 1):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 8
        rd = 0
        rs = regToBin(args[1][1])
        rt = 0
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "mfhi"):
        if (len(args) != 1):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 16
        rd = regToBin(args[1][1])
        rs = 0
        rt = 0
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "mflo"):
        if (len(args) != 1):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 18
        rd = 0
        rs = regToBin(args[1][1])
        rt = 0
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "mult"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 24
        rd = 0
        rs = regToBin(args[1][1])
        rt = regToBin(args[1][2])
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "multu"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 25
        rd = 0
        rs = regToBin(args[1][1])
        rt = regToBin(args[1][2])
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "div"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 26
        rd = 0
        rs = regToBin(args[1][1])
        rt = regToBin(args[1][2])
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "divu"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 27
        rd = 0
        rs = regToBin(args[1][1])
        rt = regToBin(args[1][2])
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "addu"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 33
        rd = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        rt = regToBin(args[1][3])
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "subu"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 35
        rd = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        rt = regToBin(args[1][3])
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "slt"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 42
        rd = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        rt = regToBin(args[1][3])
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "sltu"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 43
        rd = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        rt = regToBin(args[1][3])
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "mul"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 28
        func = 2
        rd = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        rt = regToBin(args[1][3])
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "beq"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 4
        rt = regToBin(args[1][2])
        rs = regToBin(args[1][1])
        imm = regToBin(args[1][3])
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "bne"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 5
        rt = regToBin(args[1][2])
        rs = regToBin(args[1][1])
        imm = regToBin(args[1][3])
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "addiu"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 9
        rt = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        imm = regToBin(args[1][3])
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "addi"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 8
        rt = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        imm = regToBin(args[1][3])
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "slti"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 10
        rt = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        imm = regToBin(args[1][3])
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "sltiu"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 11
        rt = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        imm = regToBin(args[1][3])
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "andi"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 12
        rt = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        imm = regToBin(args[1][3])
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "ori"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 13
        rt = regToBin(args[1][1])
        rs = regToBin(args[1][2])
        imm = regToBin(args[1][3])
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "lui"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0, 0
        opcode = 15
        rt = regToBin(args[1][1])
        rs = 0
        imm = regToBin(args[1][2])
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "lw"):
        if (args[-1] == ''):
            args = args[0:-1]
        if (len(args) != 3 and len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 35
        rt = regToBin(args[1][1])
        rs = regToBin(args[1][3])
        imm = regToBin(args[1][2])
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "sw"):
        if (args[-1] == ''):
            args = args[0:-1]
        if (len(args) != 3 and len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 43
        rt = regToBin(args[1][1])
        rs = regToBin(args[1][3])
        imm = regToBin(args[1][2])
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "j"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0, 0
        opcode = 3
        adress = args[1][2]
        numeroEmBinario = FamilyJ(opcode, adress)
    elif (args[0] == "jal"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0, 0
        opcode = 2
        adress = args[1][2]
        # tem que fazer a verificação se address é uma label e o endereço dela
        numeroEmBinario = FamilyJ(opcode, adress)
    else:
        return 0
    return numeroEmBinario


def bintohex(numeroEmBinario):
    num = int(numeroEmBinario, 2)
    return format(num, 'x')


def FamilyR(opcode, rt, rs, rd, func, shamt):
    nb = bin(opcode << 26 | rs << 21 | rt << 16 | rd << 11 | shamt << 6 | func)
    return nb


def FamilyI(opcode, rt, rs, imm):
    nb = bin(opcode << 26 | rs << 21 | rt << 16 | imm)
    return nb


def FamilyJ(opcode, adress):
    nb = bin(opcode << 26 | adress)
    return nb
