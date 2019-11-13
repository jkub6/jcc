    JUC @main
main:
    LUI $0x03, %RA
    ADDUI $0xe8, %RA
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
