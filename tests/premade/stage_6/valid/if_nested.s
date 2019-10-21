    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x01, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x02, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDI $0x00, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x04, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x02, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    CMPI $0, %RA
    JEQ @.if0_else
    LUI $0x00, %RA
    ADDI $0x01, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x04, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    JUC @.if0_end
.if0_else:
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x04, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    CMPI $0, %RA
    JEQ @.if1_else
    LUI $0x00, %RA
    ADDI $0x02, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x04, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    JUC @.if1_end
.if1_else:
.if1_end:
.if0_end:
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x04, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
