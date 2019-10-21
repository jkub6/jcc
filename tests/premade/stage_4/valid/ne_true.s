    JUC @main
main:
    MOVI $1, %RA
    MOVI $0, %R0
    SUBI $RA, %R0
    MOV $R0, %RA
    PUSH %RA
    MOVI $2, %RA
    MOVI $0, %R0
    SUBI $RA, %R0
    MOV $R0, %RA
    POP %R0
    CMP $RA, %R0
    BNE $2
    MOVI $0, %RA
    BUC $1
    MOVI $1, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
