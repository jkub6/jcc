    JUC main
main:
    MOVI $3, %RA
    SUBI $0, %RA    ; unary operator "-"
    CMPI $0, %RA    ; unary operator "!"
    BEQ $2
    MOVI $0, %RA
    BUC $1
    MOVI $1, %RA
    JUC .end
.end:
