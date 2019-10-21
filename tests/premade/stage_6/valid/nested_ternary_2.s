    JUC @main
main:
    MOVI $1, %RA
    CMPI 0, %RA
    JNE .ter0_false
    MOVI $2, %RA
    CMPI 0, %RA
    JNE .ter1_false
    MOVI $3, %RA
    JUC .ter1_done
.ter1_false:
    MOVI $4, %RA
.ter1_done:
    JUC .ter0_done
.ter0_false:
    MOVI $5, %RA
.ter0_done:
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOVI $0, %RA
    CMPI 0, %RA
    JNE .ter2_false
    MOVI $2, %RA
    CMPI 0, %RA
    JNE .ter3_false
    MOVI $3, %RA
    JUC .ter3_done
.ter3_false:
    MOVI $4, %RA
.ter3_done:
    JUC .ter2_done
.ter2_false:
    MOVI $5, %RA
.ter2_done:
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
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
