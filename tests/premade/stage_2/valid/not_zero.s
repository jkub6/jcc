    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x00, %RA
    CMPI $0, %RA
    BEQ $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
