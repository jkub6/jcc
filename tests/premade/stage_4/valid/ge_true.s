    JUC @main
main:
    MOVI $1, %RA
    PUSH %RA
    MOVI $1, %RA
    POP %R0
    CMP $RA, %R0
    BGE $2
    MOVI $0, %RA
    BUC $1
    MOVI $1, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
