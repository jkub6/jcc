    JUC main
main:
    MOVI $0, %RA
    XORI $65535, %RA
    SUBI $0, %RA
    JUC .end
.end:
