    JUC main
main:
    MOVI $0, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOVI $0, %RA
    MOV %R12, %R0
    SUBI $4, %R0
    STOR %RA, %R0
    MOV %R12, %R0
    SUBI $2, %R0
    LOAD %RA, %R0
    CMPI 0, %RA
    JNE .ter0_false
    MOVI $1, %RA
    MOV %R12, %R0
    SUBI $4, %R0
    STOR %RA, %R0
    JUC .ter0_done
.ter0_false:
    MOVI $2, %RA
    MOV %R12, %R0
    SUBI $4, %R0
    STOR %RA, %R0
.ter0_done:
    MOV %R12, %R0
    SUBI $4, %R0
    LOAD %RA, %R0
    JUC .end
.end:
