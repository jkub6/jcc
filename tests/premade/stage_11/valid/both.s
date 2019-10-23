    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x07, %RA
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
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x02, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x02, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    LOAD %RA, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
