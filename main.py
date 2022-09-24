import montador


asms = open("test.asm")
asm = asms.readlines()
montador.asmtobinandhex(asm)
