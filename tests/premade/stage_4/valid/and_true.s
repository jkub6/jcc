    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    MOVI $0, %T0
    SUB %RA, %T0
    MOV %T0, %RA
    POP %T0
    CMPI $0, %T0
    BEQ $3
    MOVI $1, %T1
    BUC $2
    MOVI $0, %T1
    CMPI $0, %RA
    BNE $2
    MOVI $0, %T1
    MOV %T1, %RA
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
