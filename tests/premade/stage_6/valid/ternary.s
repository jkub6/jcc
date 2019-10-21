    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x02, %RA
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
    PUSH %RA
    LUI $0x00, %RA
    ADDI $0x01, %RA
    POP %T0
    CMP %RA, %T0
    BGT $2
    MOVI $0, %RA
    BUC $1
    MOVI $1, %RA
    CMPI $0, %RA
    JNE @.ter0_false
    LUI $0x00, %RA
    ADDI $0x04, %RA
    JUC @.ter0_done
.ter0_false:
    LUI $0x00, %RA
    ADDI $0x05, %RA
.ter0_done:
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
