    JUC main
main:
    MOVI $0, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOV %R12, %R0
    SUBI $2, %R0
    LOAD %RA, %R0
    CMPI 0, %RA
    JEQ .if0_else
    MOVI $1, %RA
    JUC main._cleanup
    JUC .if0_end
.if0_else:
    MOVI $2, %RA
    JUC main._cleanup
.if0_end:
main._cleanup:
    JUC .end
.end:
