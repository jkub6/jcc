    JUC main
main:
    MOVI $5, %RA
    CMPI $0, %RA
    BEQ $0x4
    MOVI $0, %RA
    BUC $0x2
    MOVI $1, %RA
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
