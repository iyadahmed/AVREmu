# Iyad Ahmed 2021 -
# AVR Emulator for Fun


def gb(value: int, offset: int) -> int:
    mask = 1 << offset
    return (value & mask)


def sb(value: int, offset: int) -> int:
    mask = 1 << offset
    return (value | mask)


def alu(fn: callable) -> callable:
    ''' Decorator for ALU and Logic opcodes '''

    def op(self, Rd, Rr):
        Rdv = self.REG[Rd]
        Rrv = self.REG[Rr]
        self.REG[Rd] = fn(self, Rdv, Rrv)

    return op


class ATmega328P:
    def __init__(self) -> None:
        self.PC = 0  # Program Counter

        # FLAGS
        self.SREG = 0            # Status Register
        self.C = 0               # Carry Flag
        self.Z = 0               # Zero Flag
        self.N = 0               # Negative Flag
        self.V = 0               # Two's complement overflow indicator
        self.S = 0               # N XOR V, for signed tests
        self.H = 0               # Half Carry Flag
        self.T = 0               # Transfer bit used by BLD and BST instructions
        self.I = 0               # Global Interrupt Enable/Disable Flag

        self.REG = [0] * 32
        self.STACK = []
        self.ROM = []
        self.RAM = []

    @alu
    def ADC(self, Rd, Rr):
        assert 0 <= Rd <= 31
        assert 0 <= Rr <= 31
        R = Rd + Rr + self.C
        return R
        self.H = (gb(Rd, 3) & gb(Rr, 3)) + \
                 (gb(Rr, 3) & (~gb(R, 3))) + \
                 ((~gb(R, 3)) & gb(Rd, 3))

        self.V = (gb(Rd, 7) & gb(Rr, 7) & (~gb(R, 7))) + \
                 ((~gb(Rd, 7)) & (~gb(Rr, 7)) & gb(R, 7))

    def ADD(self, Rd, Rr):
        R = Rdv + Rrv
        return R


avr = ATmega328P()
avr.REG[1] = 1
avr.ADC(0, 1)
print(avr.REG[0])
