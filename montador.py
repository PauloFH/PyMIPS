import re


def asmtobin(asm):
    asm_split = re.split(",|\(|\)", asm)
    args = []
    for i in range(len(asm_split)):
        if (asm_split[i] != ""):
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
        rd = 8
        rs = 9
        rt = 10
        shamt = 3
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    if (args[0] == "srl"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 2
        rd = 8
        rs = 3
        rt = 10
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "add"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 32
        rd = 8
        rs = 9
        rt = 10
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "sub"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 34
        rd = 8
        rs = 9
        rt = 10
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "and"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 36
        rd = 8
        rs = 9
        rt = 10
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "or"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 37
        rd = 8
        rs = 9
        rt = 10
        shamt = 0
        numeroEmBinario =  FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "jr"):
        if (len(args) != 1):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 8
        rd = 0
        rs = 8
        rt = 0
        shamt = 0
        numeroEmBinario =  FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "mfhi"):
        if (len(args) != 1):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 16
        rd = 8
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
        rs = 8
        rt = 0
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "mult"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 24
        rd = 0
        rs = 9
        rt = 10
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "multu"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 25
        rd = 0
        rs = 9
        rt = 10
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "div"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 26
        rd = 0
        rs = 9
        rt = 10
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "divu"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 27
        rd = 0
        rs = 9
        rt = 10
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "addu"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 33
        rd = 8
        rs = 9
        rt = 10
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "subu"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 35
        rd = 8
        rs = 9
        rt = 10
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "slt"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 42
        rd = 8
        rs = 9
        rt = 10
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "sltu"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 0
        func = 43
        rd = 8
        rs = 9
        rt = 10
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "mul"):
        if (len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 28
        func = 2
        rd = 8
        rs = 9
        rt = 10
        shamt = 0
        numeroEmBinario = FamilyR(opcode, rt, rs, rd, func, shamt)
    elif (args[0] == "beq"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 1
        rt = 4
        rs = 8
        imm = 3
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "bne"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 5
        rt = 9
        rs = 8
        imm = 3
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "addiu"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 9
        rt = 8
        rs = 9
        imm = 3
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "addi"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 8
        rt = 8
        rs = 9
        imm = 3
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "slti"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 10
        rt = 8
        rs = 9
        imm = 3
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "sltiu"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 11
        rt = 8
        rs = 9
        imm = 3
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "andi"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 12
        rt = 8
        rs = 9
        imm = 3
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "ori"):
        if (len(args) != 3):
            return 0, 0, 0, 0, 0, 0
        opcode = 13
        rt = 8
        rs = 9
        imm = 3
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "lui"):
        if (len(args) != 2):
            return 0, 0, 0, 0, 0, 0
        opcode = 15
        rt = 8
        rs = 0
        imm = 3
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "lw"):
        if (args[-1] == ''):
            args = args[0:-1]
        if (len(args) != 3 and len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 35
        rt = 8
        imm = 4
        rs = 9
        numeroEmBinario = FamilyI(opcode, rt, rs, imm)
    elif (args[0] == "sw"):
        if (args[-1] == ''):
            args = args[0:-1]
        if (len(args) != 3 and len(args) != 4):
            return 0, 0, 0, 0, 0, 0
        opcode = 43
        rt = 8
        imm = 4
        rs = 9
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
        numeroEmBinario = FamilyJ(opcode, adress)
    else:
        return 0
    return numeroEmBinario

def bintohex(numeroEmBinario):
    num = int(numeroEmBinario, 2)
    return(format(num, 'x'))


def FamilyR(opcode, rt, rs, rd, func, shamt):
    nb = bin(opcode << 26 | rs << 21 | rt << 16 | rd << 11 | shamt << 6 | func)
    return nb


def FamilyI(opcode, rt, rs, imm):
    nb = bin(opcode << 26 | rs << 21 | rt << 16 | imm)
    return nb


def FamilyJ(opcode, adress):
    nb = bin(opcode << 26 | adress)
    return nb
