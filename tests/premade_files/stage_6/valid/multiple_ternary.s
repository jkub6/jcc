    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    TPSH %RA
    LUI $0x00, %RA
    ADDUI $0x02, %RA
    TPP %T0
    CMP %T0, %RA
    BGT $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    CMPI $0, %RA
    JEQ @.ter0_false
    LUI $0x00, %RA
    ADDUI $0x03, %RA
    JUC @.ter0_done
.ter0_false:
    LUI $0x00, %RA
    ADDUI $0x04, %RA
.ter0_done:
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x01, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    TPSH %RA
    LUI $0x00, %RA
    ADDUI $0x02, %RA
    TPP %T0
    CMP %T0, %RA
    BGT $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    CMPI $0, %RA
    JEQ @.ter1_false
    LUI $0x00, %RA
    ADDUI $0x05, %RA
    JUC @.ter1_done
.ter1_false:
    LUI $0x00, %RA
    ADDUI $0x06, %RA
.ter1_done:
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x02, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x01, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x02, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    TPP %T0
    ADD %T0, %RA
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
