    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x00, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x01, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDI $0x01, %RA
    CMPI $0, %RA
    JNE @.ter0_false
    LUI $0x00, %RA
    ADDI $0x02, %RA
    JUC @.ter0_done
.ter0_false:
    LUI $0x00, %RA
    ADDI $0x03, %RA
.ter0_done:
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
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
