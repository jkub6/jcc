    JUC main
main:
    MOVI $0, %RA
    XORI $65535, %RA
    MOVI $0, %R0
    SUBI $RA, %R0
    MOV $R0, %RA
    JUC .end
.end:
