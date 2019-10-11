    JUC main
main:
    MOVI $1, %RA
    PUSH %RA
    MOVI $1, %RA
    POP %R0
    ADD %R0, %RA
    XORI $65535, %RA
    JUC .end
.end:
