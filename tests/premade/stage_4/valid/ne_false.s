    JUC main
main:
    MOVI $0, %RA
    PUSH %RA
    MOVI $0, %RA
    POP %R0
    CMP $RA, %R0
    BNE $0x4
    MOVI $0, %RA
    BUC $0x2
    MOVI $1, %RA
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
