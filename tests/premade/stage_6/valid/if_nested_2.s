    JUC @main
main:
    MOVI $0, %RA
    MOV %R12, %R0
    SUBI $2, %R0
    STOR %RA, %R0
    MOVI $1, %RA
    MOV %R12, %R0
    SUBI $4, %R0
    STOR %RA, %R0
    MOV %R12, %R0
    SUBI $2, %R0
    LOAD %RA, %R0
    CMPI 0, %RA
    JEQ .if0_else
    MOVI $1, %RA
    MOV %R12, %R0
    SUBI $4, %R0
    STOR %RA, %R0
    JUC .if0_end
.if0_else:
    MOV %R12, %R0
    SUBI $4, %R0
    LOAD %RA, %R0
    CMPI 0, %RA
    JEQ .if1_else
    MOVI $2, %RA
    MOV %R12, %R0
    SUBI $4, %R0
    STOR %RA, %R0
    JUC .if1_end
.if1_else:
.if1_end:
.if0_end:
    MOV %R12, %R0
    SUBI $4, %R0
    LOAD %RA, %R0
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
