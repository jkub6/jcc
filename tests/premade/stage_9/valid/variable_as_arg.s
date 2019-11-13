    JUC @main
foo:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x03, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    PUSH %RA
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    POP %T0
    ADD %T0, %RA
    JUC @foo._cleanup
foo._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    ADDI $1, %T0
    JUC %T0
main:
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x01, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x01, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    PUSH %RA
    JAL @foo, %RA
    ADDI $1, %SP
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
