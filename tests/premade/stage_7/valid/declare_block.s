    JUC main
main:
    MOVI $5, %RA
    CMPI 0, %RA
    JNE .if0_else
    MOVI $0, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOV %R12, %R0
    SUBI $2, %R0
    LOAD %RA, %R0
    JUC main._cleanup
    JUC .if0_done
.if0_else:
.if0_done:
main._cleanup:
    JUC .end
.end:
