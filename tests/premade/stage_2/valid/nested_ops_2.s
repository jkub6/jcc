    JUC main
main:
    MOVI $0, %RA
    XORI $65535, %RA    ; unary operator "~"
    SUBI $0, %RA    ; unary operator "-"
    JUC .end
.end:
