    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x01, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDI $0x00, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDI $0x02, %RA
    POP %T0
    CMPI $0, %T0
    BEQ $3
    MOVI $1, %RA
    BUC $2
    MOVI $0, %RA
    CMPI $0, %RA
    BNE $2
    MOVI $0, %RA
    POP %T0
    CMPI $0, %T0
    BEQ $3
    MOVI $1, %RA
    BUC $2
    MOVI $0, %RA
    CMPI $0, %RA
    BEQ $2
    MOVI $1, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
