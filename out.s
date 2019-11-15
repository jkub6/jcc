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
    ADDUI $0x05, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPSH %RA
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    TPP %T0
    CMP %T0, %RA
    BLT $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x05, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x09, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    TPP %T0
    CMP %T0, %RA
    BGE $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    TPP %T0
    CMPI $0, %T0
    BEQ $3
    MOVI $1, %T1
    BUC $2
    MOVI $0, %T1
    CMPI $0, %RA
    BEQ $2
    MOVI $1, %T1
    MOV %T1, %RA
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x04, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPSH %RA
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    TPP %T0
    CMP %T0, %RA
    BLT $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    TPP %T0
    CMPI $0, %T0
    BEQ $3
    MOVI $1, %T1
    BUC $2
    MOVI $0, %T1
    CMPI $0, %RA
    BEQ $2
    MOVI $1, %T1
    MOV %T1, %RA
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x04, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x0a, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    TPP %T0
    CMP %T0, %RA
    BGE $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    TPP %T0
    CMPI $0, %T0
    BEQ $3
    MOVI $1, %T1
    BUC $2
    MOVI $0, %T1
    CMPI $0, %RA
    BEQ $2
    MOVI $1, %T1
    MOV %T1, %RA
    CMPI $0, %RA
    JEQ @.if0_else
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    PUSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x08, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    PUSH %RA
    JAL @putGlyph, %RA
    ADDI $3, %SP
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    JUC @putGlyph._cleanup
    JUC @.if0_end
.if0_else:
.if0_end:
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
    ADDUI $0x04, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPSH %RA
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    TPP %T0
    CMP %T0, %RA
    BLT $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    TPSH %RA
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
    CMP %T0, %RA
    BGE $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    TPP %T0
    CMPI $0, %T0
    BEQ $3
    MOVI $1, %T1
    BUC $2
    MOVI $0, %T1
    CMPI $0, %RA
    BEQ $2
    MOVI $1, %T1
    MOV %T1, %RA
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x03, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPSH %RA
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    TPP %T0
    CMP %T0, %RA
    BLT $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    TPP %T0
    CMPI $0, %T0
    BEQ $3
    MOVI $1, %T1
    BUC $2
    MOVI $0, %T1
    CMPI $0, %RA
    BEQ $2
    MOVI $1, %T1
    MOV %T1, %RA
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x03, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    TPSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x0a, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    TPP %T0
    CMP %T0, %RA
    BGE $3
    MOVI $0, %RA
    BUC $2
    MOVI $1, %RA
    TPP %T0
    CMPI $0, %T0
    BEQ $3
    MOVI $1, %T1
    BUC $2
    MOVI $0, %T1
    CMPI $0, %RA
    BEQ $2
    MOVI $1, %T1
    MOV %T1, %RA
    CMPI $0, %RA
    JEQ @.if1_else
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    PUSH %RA
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    PUSH %RA
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x08, %T1
    SUB %T1, %T0
    LOAD %RA, %T0
    PUSH %RA
    JAL @putGlyph, %RA
    ADDI $3, %SP
    LUI $0x00, %RA
    ADDUI $0x00, %RA
    JUC @getGlyph._cleanup
    JUC @.if1_end
.if1_else:
.if1_end:
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
wait60Cycles:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
wait60Cycles._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    ADDI $1, %T0
    JUC %T0
wait16Cycles:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x03, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    ADDI $-7, %RA
    CMPI $0, $RA
    BEQ $3
    ADDI $-1, %RA
    BUC $-3
wait16Cycles._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    ADDI $1, %T0
    JUC %T0
waitMilis:
    PUSH %RA
    PUSH %BP
    MOV %SP, %BP
    MOV %BP, %T0
    LUI $0x00, %T1
    ADDUI $0x03, %T1
    ADD %T1, %T0
    LOAD %RA, %T0
    ADDI $-1, %RA
    CMPI $0, $RA
    BEQ $9
    ADDI $-1, %RA
    LUI $12, $T0
    ADDUI $50, $T0
    CMPI $0, $T0
    BEQ $3
    ADDI $-1, %T0
    BUC $-3
    BUC $-9
    LUI $12, $T0
    ADDUI $45, $T0
    CMPI $0, $T0
    BEQ $3
    ADDI $-1, %T0
    BUC $-3
waitMilis._cleanup:
    MOV %BP, %SP
    POP %BP
    POP %T0
    ADDI $1, %T0
    JUC %T0
main:
    LUI $0x00, %RA
    ADDUI $0x07, %RA
    PUSH %RA
    JAL @wait16Cycles, %RA
    ADDI $1, %SP
    JAL @wait60Cycles, %RA
    LUI $0x00, %RA
    ADDUI $0xc8, %RA
    PUSH %RA
    JAL @wait16Cycles, %RA
    ADDI $1, %SP
    MOVI $0, %RA
    JUC @main._cleanup
main._cleanup:
    JUC @.end
.end:
