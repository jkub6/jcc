    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    TPSH %RA
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    TPP %T0
    ADD %T0, %RA
    XORI -1, %RA
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
