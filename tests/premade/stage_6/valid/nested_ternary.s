    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x01, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x01, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDI $0x02, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x02, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDI $0x00, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x03, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x01, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    PUSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x02, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    POP %T0
    CMP %RA, %T0
    BGT $2
    MOVI $0, %RA
    BUC $1
    MOVI $1, %RA
    CMPI $0, %RA
    JNE @.ter0_false
    LUI $0x00, %RA
    ADDI $0x05, %RA
    JUC @.ter0_done
.ter0_false:
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x03, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    CMPI $0, %RA
    JNE @.ter1_false
    LUI $0x00, %RA
    ADDI $0x06, %RA
    JUC @.ter1_done
.ter1_false:
    LUI $0x00, %RA
    ADDI $0x07, %RA
.ter1_done:
.ter0_done:
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
