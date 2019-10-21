    JUC @main
main:
    MOVI $0, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOVI $1, %RA
    CMPI 0, %RA
    JNE .ter0_false
    MOVI $2, %RA
    JUC .ter0_done
.ter0_false:
    MOVI $3, %RA
.ter0_done:
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOV %R12, %R0
    SUBI $2, %R0
    LOAD %RA, %R0
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
