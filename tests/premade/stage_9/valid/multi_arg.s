    JUC @main
sub_3:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x05, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    PUSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x04, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    POP %T0
    SUB %RA, %T0
    MOV %T0, %RA
    PUSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x03, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    POP %T0
    SUB %RA, %T0
    MOV %T0, %RA
    JUC @sub_3._cleanup
sub_3._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    ADDI $1, %T0
    JUC %T0
main:
    LUI $0x00, %RA
    ADDUI $0x0a, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDUI $0x04, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDUI $0x02, %RA
    PUSH %RA
    JAL @sub_3, %RA
    ADDI $3, %SP
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
