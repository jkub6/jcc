    JUC @main
main:
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDUI $0x02, %RA
    POP %T0
    SUB %RA, %T0
MOV %T0, %RA
    JUC @main._cleanup
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
