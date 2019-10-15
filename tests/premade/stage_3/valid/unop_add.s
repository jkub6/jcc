    JUC main
main:
    MOVI $2, %RA
    XORI $65535, %RA
    PUSH %RA
    MOVI $3, %RA
    POP %R0
    ADD %R0, %RA
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
