    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x01, %RA
    MOVI $0, %T0
    SUB %RA, %T0
    MOV %T0, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDI $0x02, %RA
    MOVI $0, %T0
    SUB %RA, %T0
    MOV %T0, %RA
    POP %T0
    CMP %RA, %T0
    BNE $2
    MOVI $0, %RA
    BUC $1
    MOVI $1, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
