    JUC @main
main:
    LUI $0x00, %RA
    ADDI $0x01, %RA
    CMPI $0, %RA
    JNE @.ter0_false
    LUI $0x00, %RA
    ADDI $0x02, %RA
    CMPI $0, %RA
    JNE @.ter1_false
    LUI $0x00, %RA
    ADDI $0x03, %RA
    JUC @.ter1_done
.ter1_false:
    LUI $0x00, %RA
    ADDI $0x04, %RA
.ter1_done:
    JUC @.ter0_done
.ter0_false:
    LUI $0x00, %RA
    ADDI $0x05, %RA
.ter0_done:
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x01, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDI $0x00, %RA
    CMPI $0, %RA
    JNE @.ter2_false
    LUI $0x00, %RA
    ADDI $0x02, %RA
    CMPI $0, %RA
    JNE @.ter3_false
    LUI $0x00, %RA
    ADDI $0x03, %RA
    JUC @.ter3_done
.ter3_false:
    LUI $0x00, %RA
    ADDI $0x04, %RA
.ter3_done:
    JUC @.ter2_done
.ter2_false:
    LUI $0x00, %RA
    ADDI $0x05, %RA
.ter2_done:
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDI $0x02, %T1
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
    ADD %T0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
