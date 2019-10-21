    JUC @main
main:
    MOVI $0, %RA
    PUSH %RA
    MOVI $0, %RA
    POP %R0
    CMPI $0, %R0
    BEQ $2
    MOVI $1, %RA
    BUC $1
    MOVI $0, %RA
    CMPI $0, %RA
    BEQ $1
    MOVI $1, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
