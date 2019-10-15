    JUC main
main:
    MOVI $2, %RA
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
