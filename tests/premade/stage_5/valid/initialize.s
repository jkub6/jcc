    JUC main
main:
    MOVI $2, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOVI $0, %RA
    JUC .end
.end:
