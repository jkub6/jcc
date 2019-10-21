    JUC @main
main:
    MOVI $5, %RA
    MOVI $0, %R0
    SUBI $RA, %R0
    MOV $R0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
