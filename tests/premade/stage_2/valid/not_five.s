    JUC main
main:
    MOVI $5, %RA
    CMPI $0, %RA
    BEQ $2
    MOVI $0, %RA
    BUC $1
    MOVI $1, %RA
    JUC .end
.end:
