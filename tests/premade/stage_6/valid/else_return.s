    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x00, %RA
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
    CMPI $0, %RA
    JEQ @.if0_else
    LUI $0x00, %RA
    ADDI $0x01, %RA
    JUC @main._cleanup
    JUC @.if0_end
.if0_else:
    LUI $0x00, %RA
    ADDI $0x02, %RA
    JUC @main._cleanup
.if0_end:
    LUI $0x00, %RA
    ADDI $0x03, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
