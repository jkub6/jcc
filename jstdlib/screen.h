int GLYPH_E = 1;
int GLYPH_A = 2;
int GLYPH_D = 3;
int GLYPH_G = 4;
int GLYPH_B = 5;
int GLYPH_FISH = 6;

int putGlyph(int x, int y, int glyph)
{
    int *address;
    address = x + y; /* some formula */
    *(address) = glyph;
    return 0;
}