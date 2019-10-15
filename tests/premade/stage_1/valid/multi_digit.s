    JUC main
main:
    MOVI $100, %RA
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
