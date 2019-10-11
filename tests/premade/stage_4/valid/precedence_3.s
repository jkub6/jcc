    JUC main
main:
    MOVI $2, %RA
    PUSH %RA
    MOVI $2, %RA
    PUSH %RA
    MOVI $0, %RA
    POP %R0
    CMP $RA, %R0
    BGT $0x4
    MOVI $0, %RA
    BUC $0x2
    MOVI $1, %RA
    POP %R0
    CMP $RA, %R0
    BEQ $0x4
    MOVI $0, %RA
    BUC $0x2
    MOVI $1, %RA
    JUC .end
.end:
