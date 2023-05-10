class MyBigInt:
    def init(self):
        self.value = []

    def setHex(self, hex_str):
        self.value = []
        for i in range(0, len(hex_str), 2):
            byte = hex_str[i:i+2]
            self.value.append(int(byte, 16))

    def getHex(self):
        hex_str = ""
        for byte in self.value:
            hex_str += format(byte, "02x")
        return hex_str

    def INV(self):
        for i in range(len(self.value)):
            self.value[i] = self.value[i] ^ 0xFF

    def XOR(self, other):
        result = MyBigInt()
        for i in range(max(len(self.value), len(other.value))):
            byte1 = self.value[i] if i < len(self.value) else 0
            byte2 = other.value[i] if i < len(other.value) else 0
            result.value.append(byte1 ^ byte2)
        return result

    def OR(self, other):
        result = MyBigInt()
        for i in range(max(len(self.value), len(other.value))):
            byte1 = self.value[i] if i < len(self.value) else 0
            byte2 = other.value[i] if i < len(other.value) else 0
            result.value.append(byte1 | byte2)
        return result

    def AND(self, other):
        result = MyBigInt()
        for i in range(max(len(self.value), len(other.value))):
            byte1 = self.value[i] if i < len(self.value) else 0
            byte2 = other.value[i] if i < len(other.value) else 0
            result.value.append(byte1 & byte2)
        return result

    def shiftR(self, n):
        if n == 0:
            return
        for i in range(len(self.value)-1, -1, -1):
            if i >= n:
                self.value[i] = self.value[i-n]
            else:
                self.value[i] = 0

    def shiftL(self, n):
        if n == 0:
            return
        for i in range(len(self.value)):
            if i + n < len(self.value):
                self.value[i] = self.value[i+n]
            else:
                self.value[i] = 0
        self.value.extend([0] * n)


# Використання
numberA = MyBigInt()
numberB = MyBigInt()
numberC = MyBigInt()

numberA.setHex("e035c6cfa42609b998b883bc1699df885cef74e2b2cc372eb8fa7e7")
numberB.setHex("5072f028943e0fd5fab3273782de14b1011741bd0c5cd6ba6474330")

numberC = numberA.XOR(numberB)
print(numberC.getHex())
numberC = numberA.OR(numberB)
print(numberC.getHex())
numberC = numberA.AND(numberB)
print(numberC.getHex())