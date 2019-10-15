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
    JNE .if0_else
    MOVI $2, %RA
    MOV %R12, %R0
    SUBI $4, %R0
    STOR %RA, %R0
    MOV %R12, %R0
    SUBI $4, %R0
    LOAD %RA, %R0
    JUC main._cleanup
    JUC .if0_done
.if0_else:
    MOVI $3, %RA
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
    CMP $RA, %R0
    BLT $0x4
    MOVI $0, %RA
    BUC $0x2
    MOVI $1, %RA
    CMPI 0, %RA
    JNE .if1_else
    MOVI $4, %RA
    JUC main._cleanup
    JUC .if1_done
.if1_else:
    MOVI $5, %RA
    JUC main._cleanup
.if1_done:
.if0_done:
    MOV %R12, %R0
    SUBI $2, %R0
    LOAD %RA, %R0
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
