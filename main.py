# Iyad Ahmed 2021 -
# AVR Emulator for Fun

from ctypes import c_int8


class Register:
    def __init__(self):
        self.value = c_int8(0)

    def set_value(self, value):
        self.value = c_int8(value)

    def __getitem__(self, key):
        return self.value & (1 << key)

    def __setitem__(self, key, value):
        if value:
            self.value = c_int8(self.value | (1 << key))
        else:
            self.value = c_int8(self.value & ~(1 << key))


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

        self.REG = [Register()] * 32
        self.STACK = []
        self.ROM = []
        self.RAM = []

    def ADD(self, Rd, Rr):
        assert 0 <= Rd <= 31
        assert 0 <= Rr <= 31
        Rdv = self.REG[Rd]
        Rrv = self.REG[Rr]
        Rv = Rdv + Rrv
        self.REG[Rd] = Rv

        Rdv3 = get_bit(Rdv, 3)
        Rrv3 = get_bit(Rrv, 3)
        Rv3 = get_bit(Rv, 3)
        self.H = Rdv3 & Rrv3 + Rrv3 & ~Rv3 + ~Rv3 & Rdv3    # Set if there was a carry from bit 3; cleared otherwise.

        Rdv7 = get_bit(Rdv, 7)
        Rrv7 = get_bit(Rrv, 7)
        Rv7 = get_bit(Rv, 7)
        self.V = R >   # Set if two’s complement overflow resulted from the operation; cleared otherwise.

        self.N = Rv7
        self.S = self.N ^ self.V
        

    def ADC(self, Rd, Rr):
        R = Rd + Rr + self.C
        return R


avr = ATmega328P()
avr.REG[1] = 5
avr.ADD(0, 1)
print(avr.REG[0])
