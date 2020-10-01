    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x01, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x01, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    CMPI $0, %RA
    JEQ @.if0_else
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    JUC @main._cleanup
    JUC @.if0_end
.if0_else:
    LUI $0x00, %RA
    ADDUI $0x02, %RA
    JUC @main._cleanup
.if0_end:
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
