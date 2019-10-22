    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x02, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x01, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x01, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    PUSH %RA
    LUI $0x00, %RA
    ADDI $0x03, %RA
    POP %T0
    CMP %RA, %T0
    BLT $2
    MOVI $0, %RA
    BUC $1
    MOVI $1, %RA
    CMPI $0, %RA
    JEQ @.if0_else
    LUI $0x00, %RA
    ADDI $0x03, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x02, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x02, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    JUC @main._cleanup
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x01, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    JUC @main._cleanup
    JUC @.if0_end
.if0_else:
.if0_end:
main._cleanup:
    JUC @.end
.end:
