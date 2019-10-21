    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x00, %RA
    XORI $-1, %RA
    MOVI $0, %T0
    SUB %RA, %T0
    MOV %T0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
