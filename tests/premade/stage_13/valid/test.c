#include "../../../../jstdlib/jstdlib.h"

int main()
{
    while (1)
    {
        putGlyph(0,0,GLYPH_D);
        waitMilis(500);
        putGlyph(0,0,GLYPH_BLANK);
        putGlyph(2,2,GLYPH_E);
        waitMilis(500);
        putGlyph(0,0,GLYPH_BLANK);
    }
}