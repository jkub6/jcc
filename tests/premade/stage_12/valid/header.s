    JUC @main
three:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
    LUI $0x00, %RA
    ADDI $0x03, %RA
    JUC @three._cleanup
three._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    JUC %T0
main:
    JAL @three, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
