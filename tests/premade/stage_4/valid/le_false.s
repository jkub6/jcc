    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    MOVI $0, %T0
    SUB %RA, %T0
    MOV %T0, %RA
    POP %T0
    CMP %T0, %RA
    BLE $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
