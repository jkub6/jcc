    JUC @main
returnFour:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
    LUI $0x00, %RA
    ADDI $0x04, %RA
    JUC @returnFour._cleanup
returnFour._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    JUC %T0
main:
    JAL @returnFour, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
