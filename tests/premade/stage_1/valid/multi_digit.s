    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x64, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
