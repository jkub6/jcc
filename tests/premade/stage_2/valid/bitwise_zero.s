    JUC @main
main:
    MOVI $0, %RA
    XORI $65535, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
