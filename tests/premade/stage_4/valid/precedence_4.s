    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x02, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDUI $0x02, %RA
    POP %T0
    CMP %T0, %RA
    BEQ $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    POP %T0
    CMPI $0, %T0
    BEQ $3
    MOVI $1, %T1
    BUC $2
    MOVI $0, %T1
    CMPI $0, %RA
    BEQ $2
    MOVI $1, %T1
    MOV %T1, %RA
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
