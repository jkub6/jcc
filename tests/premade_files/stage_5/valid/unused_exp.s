    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x02, %RA
    TPSH %RA
    LUI $0x00, %RA
    ADDUI $0x02, %RA
    TPP %T0
    ADD %T0, %RA
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
