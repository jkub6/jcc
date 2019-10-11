"""
Simulate binary files. Primarily for unit testing.

This file is a part of Jake's C Compiler (JCC)
(c) Copyright 2019 Jacob Larkin
"""


class Register16:
    """Define a 16 bit register."""

    def __init__(self):
        """Override default constructor."""


class Simulator:
    """Simulate binary files."""

    def __init__(self):
        """Override default constructor."""
        self.r0 = Register16()
        self.r1 = Register16()
        self.r2 = Register16()
        self.r3 = Register16()
        self.r4 = Register16()
        self.r5 = Register16()
        self.r6 = Register16()
        self.r7 = Register16()
        self.r8 = Register16()
        self.r9 = Register16()
        self.r10 = Register16()
        self.r11 = Register16()
        self.r12 = Register16()
        self.r13 = Register16()

        self.ra = Register16()
        self.sp = Register16()

        self.psr = 0

    def reset(self):
        """Reset machine to default state."""

    def run(self):
        """Run the machine."""
