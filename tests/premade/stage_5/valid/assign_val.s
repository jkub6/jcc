    JUC main
main:
    MOVI $0, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOV %R12, %R0
    SUBI $4, %R0
    STOR %RA, %R0
    MOV %R12, %R0
    SUBI $4, %R0
    LOAD %RA, %R0
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
