    JUC main
main:
    MOVI $12, %RA
    CMPI $0, %RA
    BEQ $0x4
    MOVI $0, %RA
    BUC $0x2
    MOVI $1, %RA
    JUC .end
.end:
