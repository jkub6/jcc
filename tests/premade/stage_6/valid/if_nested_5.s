    JUC main
main:
    MOVI $0, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOVI $0, %RA
    CMPI 0, %RA
    JNE .if0_else
    MOVI $0, %RA
    CMPI 0, %RA
    JNE .if1_else
    MOVI $3, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    JUC .if1_done
.if1_else:
    MOVI $4, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
.if1_done:
    JUC .if0_done
.if0_else:
    MOVI $1, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
.if0_done:
    MOV %R12, %R0
    SUBI $2, %R0
    LOAD %RA, %R0
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
