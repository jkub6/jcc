    JUC main
main:
    MOVI $2, %RA
    PUSH %RA
    MOVI $2, %RA
    POP %R0
    ADD %R0, %RA
    MOVI $0, %RA
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
