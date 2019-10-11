    JUC main
main:
    MOVI $3, %RA
    MOVI $0, %R0
    SUBI $RA, %R0
    MOV $R0, %RA
    CMPI $0, %RA
    BEQ $2
    MOVI $0, %RA
    BUC $1
    MOVI $1, %RA
    JUC .end
.end:
