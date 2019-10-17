    JUC main
main:
    MOVI $0, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOVI $1, %RA
    CMPI 0, %RA
    JEQ .if0_else
    MOVI $0, %RA
    CMPI 0, %RA
    JEQ .if1_else
    MOVI $3, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    JUC .if1_end
.if1_else:
    MOVI $4, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
.if1_end:
    JUC .if0_end
.if0_else:
.if0_end:
    MOV %R12, %R0
    SUBI $2, %R0
    LOAD %RA, %R0
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
