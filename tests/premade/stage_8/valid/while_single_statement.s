    JUC @main
main:
    MOVI $0, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
.whi0_begin:
    MOV %R12, %R0
    SUBI $2, %R0
    LOAD %RA, %R0
    PUSH %RA
    MOVI $5, %RA
    POP %R0
    CMP $RA, %R0
    BLT $2
    MOVI $0, %RA
    BUC $1
    MOVI $1, %RA
    CMPI 0, %RA
    JEQ .whi0_end
    MOV %R12, %R0
    SUBI $2, %R0
    LOAD %RA, %R0
    PUSH %RA
    MOVI $2, %RA
    POP %R0
    ADD %R0, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    JUC .whi0_begin
.whi0_end:
    MOV %R12, %R0
    SUBI $2, %R0
    LOAD %RA, %R0
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
