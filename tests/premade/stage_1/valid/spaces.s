    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
