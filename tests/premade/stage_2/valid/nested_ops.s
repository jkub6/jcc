    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x03, %RA
    MOVI $0, %T0
    SUB %RA, %T0
    MOV %T0, %RA
    CMPI $0, %RA
    BEQ $2
    MOVI $0, %RA
    BUC $1
    MOVI $1, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
