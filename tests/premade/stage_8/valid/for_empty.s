    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x00, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x01, %T1
    SUB %T1, %T0
    STOR %RA, %T0
.loop0_begin:
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x01, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    PUSH %RA
    LUI $0x00, %RA
    ADDI $0x01, %RA
    POP %T0
    ADD %T0, %RA
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
    BGT $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    CMPI $0, %RA
    JEQ @.if0_else
    JUC @.loop0_end
    JUC @.if0_end
.if0_else:
.if0_end:
    JUC @.loop0_begin
.loop0_end:
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x01, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
