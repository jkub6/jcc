int GLYPH_BLANK = 1;
int GLYPH_E = 1;
int GLYPH_A = 2;
int GLYPH_D = 3;
int GLYPH_G = 4;
int GLYPH_B = 5;
int GLYPH_FISH = 6;
int GLYPH_ERROR = 7;

int SCREEN_WIDTH = 10;
int SCREEN_HEIGHT = 8;


int putGlyph(int x, int y, int glyph)
{
    if (x < 0 || x >= SCREEN_WIDTH || y < 0 || y >= SCREEN_HEIGHT)
    {
        putGlyph(0, 0, GLYPH_ERROR);
        return 0;
    }

    int address = -(y * SCREEN_WIDTH + x);
    *(address) = glyph;
    return 0;
}


int getGlyph(int x, int y)
{
    if (x < 0 || x >= SCREEN_WIDTH || y < 0 || y >= SCREEN_HEIGHT)
    {
        putGlyph(0, 0, GLYPH_ERROR);
        return 0;
    }

    int address = -(y * SCREEN_WIDTH + x);
    return *address;
}

int getMemValue()
{
    asm("LUI $0xff, %T0");
    asm("ADDUI $0x6d, %T0");
    asm("LOAD %RA, %T0");
}

int setMemValue(int input)
{
    //*(addrstore + i)
    asm("LUI %T0, $input");
    asm("ADDUI %T0, $input");
    asm("LOAD %RA, %T0");
}


int wait60Cycles() { }  // empty function call takes 60 cycles


int wait16Cycles(int times)  // busywork for waiting cycles
{
    // times must be >= 7
    times;  // Load times argument into %RA

    // offset times input
    asm("ADDI $-7, %RA");

    // loop with overhead of 16 cycles
    asm("CMPI $0, %RA");
    asm("BEQ $3");
    asm("ADDI $-1, %RA");
    asm("BUC $-3");
}


int waitMilis(int milis)  // busywork for waiting miliseconds
{
    milis;  // Load milis argument into %RA

    // offset milis input
    asm("ADDI $-1, %RA");

    // loop with overhead of 1ms
    asm("CMPI $0, %RA");
    asm("BEQ $9");
    asm("ADDI $-1, %RA");
    asm("LUI $12, %T0");
    asm("ADDUI $50, %T0");
    asm("CMPI $0, %T0");
    asm("BEQ $3");
    asm("ADDI $-1, %T0");
    asm("BUC $-3");
    asm("BUC $-9");

    // make no loop overhead 1 ms
    asm("LUI $12, %T0");
    asm("ADDUI $45, %T0");
    asm("CMPI $0, %T0");
    asm("BEQ $3");
    asm("ADDI $-1, %T0");
    asm("BUC $-3");
}


int waitSecs(int secs)  // too long to test with simulator
{
    for (int i = 0; i < secs; i = i + 1)
    {
        // wait 1 second - 56 cycles (approximate for loop overhead)
        waitMilis(999);
        wait16Cycles(309);
    }
}