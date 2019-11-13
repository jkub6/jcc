    JUC @main
main:
.loop0_begin:
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    CMPI $0, %RA
    JEQ @.loop0_end
    JUC @.loop0_end
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    JUC @main._cleanup
    JUC @.loop0_begin
.loop0_end:
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
