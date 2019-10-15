    JUC main
main:
    MOVI $1, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOVI $2, %RA
    MOV %R12, %R0
    SUBI $4, %R0
    STOR %RA, %R0
    MOVI $0, %RA
    MOV %R12, %R0
    SUBI $6, %R0
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
    BGT $0x4
    MOVI $0, %RA
    BUC $0x2
    MOVI $1, %RA
    CMPI 0, %RA
    JNE .ter0_false
    MOVI $5, %RA
    JUC .ter0_done
.ter0_false:
    MOV %R12, %R0
    SUBI $6, %R0
    LOAD %RA, %R0
    CMPI 0, %RA
    JNE .ter1_false
    MOVI $6, %RA
    JUC .ter1_done
.ter1_false:
    MOVI $7, %RA
.ter1_done:
.ter0_done:
    JUC .end
.end:
