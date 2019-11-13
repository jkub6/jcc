    JUC @main
twice:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
    LUI $0x00, %RA
    ADDUI $0x02, %RA
    PUSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x03, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    POP %T0
    MUL %T0, %RA
    JUC @twice._cleanup
twice._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    ADDI $1, %T0
    JUC %T0
main:
    LUI $0x00, %RA
    ADDUI $0x03, %RA
    PUSH %RA
    JAL @twice, %RA
    ADDI $1, %SP
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
