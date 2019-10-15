    JUC main
main:
    MOVI $1, %RA
    PUSH %RA
    MOVI $2, %RA
    POP %R0
    CMP $RA, %R0
    BGT $0x4
    MOVI $0, %RA
    BUC $0x2
    MOVI $1, %RA
    CMPI 0, %RA
    JNE .ter0_false
    MOVI $3, %RA
    JUC .ter0_done
.ter0_false:
    MOVI $4, %RA
.ter0_done:
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOVI $1, %RA
    PUSH %RA
    MOVI $2, %RA
    POP %R0
    CMP $RA, %R0
    BGT $0x4
    MOVI $0, %RA
    BUC $0x2
    MOVI $1, %RA
    CMPI 0, %RA
    JNE .ter1_false
    MOVI $5, %RA
    JUC .ter1_done
.ter1_false:
    MOVI $6, %RA
.ter1_done:
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
    JUC .end
.end:
