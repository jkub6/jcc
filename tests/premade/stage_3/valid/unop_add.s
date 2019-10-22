    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x02, %RA
    NOT %RA, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDI $0x03, %RA
    POP %T0
    ADD %T0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
