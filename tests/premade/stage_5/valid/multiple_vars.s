    JUC main
main:
    MOVI $1, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOVI $2, %RA
    MOV %R12, %R0
    SUBI $4, %R0
    STOR %RA, %R0
    MOV %R12, %R0
    SUBI $2, %R0
    LOAD %RA, %R0
    PUSH %RA
    MOV %R12, %R0
    SUBI $4, %R0
    LOAD %RA, %R0
    POP %R0
    ADD %R0, %RA
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
