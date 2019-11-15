    LUI $0x00, %RA
    ADDUI $0x01, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x01, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x02, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDUI $0x02, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x03, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDUI $0x03, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x04, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDUI $0x04, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x05, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDUI $0x05, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x06, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDUI $0x06, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x07, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDUI $0x07, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x08, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDUI $0x0a, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x09, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDUI $0x08, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x0a, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    JUC @main
putGlyph:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x04, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x09, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    TPP %T0
    MUL %T0, %RA
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x05, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPP %T0
    ADD %T0, %RA
    MOVI $0, %T0
    SUB %RA, %T0
    MOV %T0, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x0b, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x03, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x0b, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    TPP %T0
    STOR %T0, %RA
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    JUC @putGlyph._cleanup
putGlyph._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    ADDI $1, %T0
    JUC %T0
getGlyph:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x03, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x09, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    TPP %T0
    MUL %T0, %RA
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x04, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPP %T0
    ADD %T0, %RA
    MOVI $0, %T0
    SUB %RA, %T0
    MOV %T0, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x0b, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x0b, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    LOAD %RA, %RA
    JUC @getGlyph._cleanup
getGlyph._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    ADDI $1, %T0
    JUC %T0
useless:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
useless._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    ADDI $1, %T0
    JUC %T0
wait50Cycles:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x0b, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    LUI $0x00, %RA
    ADDUI $0x01, %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x0c, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x03, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x0b, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    TPP %T0
    SUB %RA, %T0
    MOV %T0, %RA
    MOV %BP, %T0
    LUI $0xff, %T1
    ADDUI $0xfd, %T1
    SUB %T1, %T0
    STOR %RA, %T0
.loop0_begin:
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x03, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPP %T0
    CMP %T0, %RA
    BLT $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    CMPI $0, %RA
    JEQ @.loop0_end
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x03, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x0c, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    TPP %T0
    SUB %RA, %T0
    MOV %T0, %RA
    MOV %BP, %T0
    LUI $0xff, %T1
    ADDUI $0xfd, %T1
    SUB %T1, %T0
    STOR %RA, %T0
    JUC @.loop0_begin
.loop0_end:
    Test
wait50Cycles._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    ADDI $1, %T0
    JUC %T0
main:
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    PUSH %RA
    JAL @wait50Cycles, %RA
    ADDI $1, %SP
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
