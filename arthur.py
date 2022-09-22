from operator import rshift
from turtle import rt
import re
import os.path
import sys

filename = "Untitled"
fileexists = False

def asmtoint(asm):
    asm_split = re.split(" |, |\(|\)", asm)
    args = []
    for i in range (len(asm_split)):
        if (asm_split[i] != ""):
            args.append(asm_split[i])
    #print args
    opcode = 0
    func = 0
    rd = 0
    rs = 0
    rt = 0
    imm = 0
    if (args[0] == "sll"):
        if (len(args) != 4):
            return 0,0,0,0,0,0
        opcode = 0
        func = 0
        rd = 8
        rs = 3
        rt = 10
        FamilyR()
    elif (args[0] == "add"):
        if (len(args) != 4):
            return 0,0,0,0,0,0
        opcode = 0
        func = 32
        rd = 8
        rs = 9
        rt = 10
        FamilyR()
    elif (args[0] == "sub"):
        if (len(args) != 4):
            return 0,0,0,0,0,0
        opcode = 0
        func = 34
        rd = 8
        rs = 9
        rt = 10
        FamilyR()
    elif (args[0] == "and"):
        if (len(args) != 4):
            return 0,0,0,0,0,0
        opcode = 0
        func = 36
        rd = 8
        rs = 9
        rt = 10
        FamilyR()
    elif (args[0] == "or"):
        if (len(args) != 4):
            return 0,0,0,0,0,0
        opcode = 0
        func = 37
        rd = 8
        rs = 9
        rt = 10
        FamilyR()
    elif (args[0] == "srl"):
        if (len(args) != 4):
            return 0,0,0,0,0,0
        opcode = 0
        func = 2
        rd = 8
        rs = 0
        rt = 10
        imn = 3
        FamilyR()
    elif (args[0] == "addu"):
        if (len(args) != 4):
            return 0,0,0,0,0,0
        opcode = 0
        func = 33
        rd = 8
        rs = 9
        rt = 10
        FamilyR()
    elif (args[0] == "subu"):
        if (len(args) != 4):
            return 0,0,0,0,0,0
        opcode = 0
        func = 35
        rd = 8
        rs = 9
        rt = 10
        FamilyR()
    elif (args[0] == "slt"):
        if (len(args) != 4):
            return 0,0,0,0,0,0
        opcode = 0
        func = 42
        rd = 8
        rs = 9
        rt = 10
        FamilyR()
    elif (args[0] == "sltu"):
        if (len(args) != 4):
            return 0,0,0,0,0,0
        opcode = 0
        func = 43
        rd = 8
        rs = 9
        rt = 10
        FamilyR()
    elif (args[0] == "mul"):
        if (len(args) != 4):
            return 0,0,0,0,0,0
        opcode = 28
        func = 2
        rd = 8
        rs = 9
        rt = 10
        FamilyR()                        
    elif (args[0] == "bez"):
        if (len(args) != 3):
            return 0,0,0,0,0,0
        opcode = 1
        rt = 0
        rs = int(args[1][1:])
        imm = int(args[2])
    elif (args[0] == "bnez"):
        if (len(args) != 3):
            return 0,0,0,0,0,0
        opcode = 1
        rt = 1
        rs = int(args[1][1:])
        imm = int(args[2])
    elif (args[0] == "bgez"):
        if (len(args) != 3):
            return 0,0,0,0,0,0
        opcode = 1
        rt = 2
        rs = int(args[1][1:])
        imm = int(args[2])
    elif (args[0] == "blez"):
        if (len(args) != 3):
            return 0,0,0,0,0,0
        opcode = 1
        rt = 3
        rs = int(args[1][1:])
        imm = int(args[2])
    elif (args[0] == "bgz"):
        if (len(args) != 3):
            return 0,0,0,0,0,0
        opcode = 1
        rt = 4
        rs = int(args[1][1:])
        imm = int(args[2])
    elif (args[0] == "blz"):
        if (len(args) != 3):
            return 0
        opcode = 1
        rt = 5
        rs = int(args[1][1:])
        imm = int(args[2])
    elif (args[0] == "lw"):
        if (args[-1] == ''):
            args = args[0:-1]
        if (len(args) != 3 and len(args) != 4):
            return 0,0,0,0,0,0
        opcode = 2
        rt = int(args[1][1:])
        if (len(args) == 3):
            imm = 0
            rs = int(args[2][1:])
        else:
            imm = int(args[2])
            rs = int(args[3][1:])
    elif (args[0] == "sw"):
        if (args[-1] == ''):
            args = args[0:-1]
        if (len(args) != 3 and len(args) != 4):
            return 0,0,0,0,0,0
        opcode = 3
        rt = int(args[1][1:])
        if (len(args) == 3):
            imm = 0
            rs = int(args[2][1:])
        else:
            imm = int(args[2])
            rs = int(args[3][1:])
    else:
        return 0,0,0,0,0,0
    return opcode, rs, rt, rd, func, imm

def inttohex(opcode, rs, rt, rd, func, imm):
    if (opcode == 0):
        opstr = format(opcode, '02b')
        rsstr = format(rs, '03b')
        rtstr = format(rt, '03b')
        rdstr = format(rd, '03b')
        fnstr = format(func, '05b')
        #print opstr, rsstr, rtstr, rdstr, fnstr
        instruction = opstr + rsstr + rtstr + rdstr + fnstr
    else :
        opstr = format(opcode, '02b')
        rtstr = format(rt, '03b')
        rsstr = format(rs, '03b')
        if (imm < 0):
            imm2s = ((-imm) ^ 255) + 1
            immstr = format(imm2s, '08b')
        else :
            immstr = format(imm, '08b')
        #print opstr, rtstr, rsstr, immstr
        instruction = opstr + rsstr + rtstr + immstr
    return format(int(instruction, 2), '04x')

    
def FamilyR():
    opcodeFR = opcode
    rtFR = rt
    rsFR = rs
    rdFR = rd
    sa
    funct 
    numeroBinario = opcode << rs << rt << rd << sa << funct
    return numeroBinario
    
    
def FamilyI():
    opcodeFR = opcode
    rtFR = rt
    rsFR = rs
    contante   
    numeroBinario= opcode << rs << rt << constante
    return numeroBinario
    
def FamilyI():
    opcodeFR = opcode
    adress   
    numeroBinario= opcode << adress
    return numeroBinario