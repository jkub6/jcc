    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x01, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDI $0x01, %RA
    MOVI $0, %T0
    SUB %RA, %T0
    MOV %T0, %RA
    POP %T0
    CMPI $0, %T0
    BEQ $3
    MOVI $1, %RA
    BUC $2
    MOVI $0, %RA
    CMPI $0, %RA
    BNE $2
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
