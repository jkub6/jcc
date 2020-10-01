    JUC @main
main:
    LUI $0x0f, %RA
    ADDUI $0xff, %RA
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
