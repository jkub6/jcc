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
    BEQ $0x4
    MOVI $1, %RA
    BUC $0x2
    MOVI $0, %RA
    CMPI $0, %RA
    BNE $0x2
    MOVI $0, %RA
    JUC .end
.end:
