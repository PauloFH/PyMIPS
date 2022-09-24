import montador


asms = open("test.asm")
asm = asms.readlines()
numeroBinDaLinha = montador.asmtobin(asm)
numeroHexDaLinha = montador.bintohex(numeroBinDaLinha)
