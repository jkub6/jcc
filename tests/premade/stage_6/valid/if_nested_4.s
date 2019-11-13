    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x01, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    CMPI $0, %RA
    JEQ @.if0_else
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    CMPI $0, %RA
    JEQ @.if1_else
    LUI $0x00, %RA
    ADDUI $0x03, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x01, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    JUC @.if1_end
.if1_else:
    LUI $0x00, %RA
    ADDUI $0x04, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x01, %T1
    SUB %T1, %T0
    STOR %RA, %T0
.if1_end:
    JUC @.if0_end
.if0_else:
.if0_end:
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x01, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
