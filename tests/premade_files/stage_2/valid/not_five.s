    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x05, %RA
    CMPI $0, %RA
    BEQ $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
