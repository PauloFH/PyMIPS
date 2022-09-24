import montador

asms = open("test.asm")
asm = asms.readlines()
labels = []  # Labels do codigo
inL = []  # endereço das labels
inf = []  # Endereço das funções
fun = []  # funções
address = 0x4000000
label = ""
strf = ""
for line in asm:
    if line.find(':') > 0:
        labelchar = False
        label = ""
        strf = ""
        for x in line.strip():
            if not labelchar:
                if x == ':':
                    labels.append(label)
                    inL.append(address)
                    labelchar = True
                else:
                    label += x
            else:
                Str = line.strip(label)
                label += ':'
    else:
        fun.append(strf.strip())
        inf.append(address)
    address += 4


def lines():
    lns = 0

    pass


numeroBinDaLinha = montador.asmtobin(asm)

print(numeroBinDaLinha)
