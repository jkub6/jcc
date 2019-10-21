    JUC @main
main:
    MOVI $1, %RA
    PUSH %RA
    MOVI $2, %RA
    POP %R0
    ADD %R0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
