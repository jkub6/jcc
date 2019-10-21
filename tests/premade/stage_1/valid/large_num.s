    JUC @main
main:
    LUI $0x03, %RA
    ADDI $0xe8, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
