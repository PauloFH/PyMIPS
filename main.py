
from typing import List

import montador

asms = open("mips.asm")
asm = asms.readlines()
asms.close()
bins: List[str] = []
labels = []  # Labels do codigo
inL = []  # endereço das labels
inf = []  # Endereço das funções
fun = []  # funções
address = 4194304  # endereço inicial de 0x00400000 em decimal
label = ""  # string criada para salvar as labels dentro da lista
strf = ""  # string criada para salvar as funções do código
for line in asm:
    # simulando a atividade do pc
    if line.find(':') > 0:
        # quando encontrar um label na linha, a parte sem a label
        # será escrita na string de funções
        labelchar = False
        label = ""
        strf = ""
        for x in line.strip():
            if not labelchar:
                if x == ':':
                    labels.append(label)
                    # acrescentando a label a lista de labels
                    inL.append(address)
                    # acrescentando o endereço correspondente ao label na lista
                    labelchar = True
                else:
                    label += x
            else:
                strf = line.strip(label)
                label += ':'
                # acrescentando os ":" ao final do label
        fun.append(strf.strip())
        inf.append(address)
    else:
        fun.append(line.strip())
        inf.append(address)
    address += 4  # adiocionando 4 unidades ao endereço atual


montador.asmtobin(fun, bins, labels, inL)

bin_return = open("return.bin.", 'w')

for i in range(len(bins)):
    bin_return.write(str(bins[i]) + '\n')
    # escrevendo a lista de números binários no arquivo
bin_return.close()
