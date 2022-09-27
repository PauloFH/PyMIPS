sll $8, $9, 3
L2: srl $t2, $9, 3
jr $t0
mfhi $s0
mflo $s1
mult $9, $10
multu $9, $10
div $9, $11
divu $9, $10
L1: add $t0, $s2 , $s1
addu $s2, $9, $10
sub $9, $10, $9
subu $8, $9, $10
and $8, $9, $10
or $10, $9, $8
sltu $8, $9, $10
mul $8, $9, $10
beq $8, $t0, L1
bne $t4, $9, L2
addi $10, $s1 7
addiu $8, $9, 5
slti $8, $9, 3
sltiu $8, $9, 6
andi $s5 , $t1 3
ori $8, $9, 6
lw $s2, 4($t1)
sw $8, 4($9)
j L1
jal L2