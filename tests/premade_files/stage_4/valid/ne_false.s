    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    TPSH %RA
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    TPP %T0
    CMP %T0, %RA
    BNE $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
