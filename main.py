
from typing import List
import montador

asms = open("test.asm")
asm = asms.readlines()
asms.close()
labels = []  # Labels do codigo
inL = []  # endereço das labels
inf = []  # Endereço das funções
fun = []  # funções
address = 4194304
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
                strf = line.strip(label)
                label += ':'
        fun.append(strf.strip())
        inf.append(address)
    else:
        fun.append(line.strip())
        inf.append(address)
    address += 4
print(fun)

bins: List[int] = []
montador.asmtobin(fun, bins, labels, inL)

bin_return = open("return.bin.", 'w')

for i in range(len(bins)):
    bin_return.write(str(bins[i]) + '\n')
bin_return.close()
