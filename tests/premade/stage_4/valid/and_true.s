    JUC main
main:
    MOVI $1, %RA
    PUSH %RA
    MOVI $1, %RA
    MOVI $0, %R0
    SUBI $RA, %R0
    MOV $R0, %RA
    POP %R0
    CMPI $0, %R0
    BEQ $2
    MOVI $1, %RA
    BUC $1
    MOVI $0, %RA
    CMPI $0, %RA
    BNE $1
    MOVI $0, %RA
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
