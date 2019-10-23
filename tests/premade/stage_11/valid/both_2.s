    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x13, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x01, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x01, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    MOV %T0, %RA
    LOAD %RA, %RA
    MOV %T0, %RA
    LOAD %RA, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
