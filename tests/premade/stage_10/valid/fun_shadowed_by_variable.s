    JUC @main
foo:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
    LUI $0x00, %RA
    ADDUI $0x03, %RA
    JUC @foo._cleanup
foo._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    ADDI $1, %T0
    JUC %T0
main:
    LUI $0x00, %RA
    ADDUI $0x05, %RA
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
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
