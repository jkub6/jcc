    JUC main
main:
    MOVI $2, %RA
    PUSH %RA
    MOVI $1, %RA
    MOVI $0, %R0
    SUBI $RA, %R0
    MOV $R0, %RA
    POP %R0
    SUB %R0, %RA
    JUC .end
.end: