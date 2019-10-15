    JUC main
main:
    MOVI $1, %RA
    PUSH %RA
    MOVI $1, %RA
    MOVI $0, %R0
    SUBI $RA, %R0
    MOV $R0, %RA
    POP %R0
    CMP $RA, %R0
    BLE $0x4
    MOVI $0, %RA
    BUC $0x2
    MOVI $1, %RA
    JUC main._cleanup
main._cleanup:
    JUC .end
.end:
