    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x07, %RA
    TPSH %RA
    LUI $0x00, %RA
    ADDUI $0x04, %RA
    TPP %T0
    MUL %T0, %RA
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
