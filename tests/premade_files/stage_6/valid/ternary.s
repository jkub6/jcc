    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x02, %RA
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
    TPSH %RA
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    TPP %T0
    CMP %T0, %RA
    BGT $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    CMPI $0, %RA
    JEQ @.ter0_false
    LUI $0x00, %RA
    ADDUI $0x04, %RA
    JUC @.ter0_done
.ter0_false:
    LUI $0x00, %RA
    ADDUI $0x05, %RA
.ter0_done:
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
