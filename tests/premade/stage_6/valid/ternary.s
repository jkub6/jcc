    JUC main
main:
    MOVI $2, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOV %R12, %R0
    SUBI $2, %R0
    LOAD %RA, %R0
    PUSH %RA
    MOVI $1, %RA
    POP %R0
    CMP $RA, %R0
    BGT $0x4
    MOVI $0, %RA
    BUC $0x2
    MOVI $1, %RA
    CMPI 0, %RA
    JNE .ter0_false
    MOVI $4, %RA
    JUC .ter0_done
.ter0_false:
    MOVI $5, %RA
.ter0_done:
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
