    JUC main
main:
    MOVI $0x1a, %RA
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
