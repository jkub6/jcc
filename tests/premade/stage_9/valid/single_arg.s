    JUC @main
twice:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
    LUI $0x00, %RA
    ADDI $0x02, %RA
    PUSH %RA
    MOV %BP, %T0
    LUI $0xff, %T1
    ADDI $0xfe, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    POP %T0
    MUL %T0, %RA
    JUC @twice._cleanup
twice._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    JUC %T0
main:
    LUI $0x00, %RA
    ADDI $0x03, %RA
    PUSH %RA
    JAL @twice, %RA
    ADDI $1, %SP
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
