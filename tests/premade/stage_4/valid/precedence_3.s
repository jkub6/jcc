    JUC @main
main:
    MOVI $2, %RA
    PUSH %RA
    MOVI $2, %RA
    PUSH %RA
    MOVI $0, %RA
    POP %R0
    CMP $RA, %R0
    BGT $2
    MOVI $0, %RA
    BUC $1
    MOVI $1, %RA
    POP %R0
    CMP $RA, %R0
    BEQ $2
    MOVI $0, %RA
    BUC $1
    MOVI $1, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
