    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x01, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDI $0x02, %RA
    POP %T0
    SUB %T0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
