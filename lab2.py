class BigInt:
    def init(self, num_str):
        self.arr = []
        for i in range(len(num_str)-1, -1, -8):
            byte = num_str[max(i-7, 0):i+1]
            self.arr.append(int(byte, 16))

    def str(self):
        num_str = ""
        for byte in self.arr[::-1]:
            num_str += hex(byte)[2:].zfill(8)
        return num_str.upper()

    def set_number(self, num_str):
        self.arr = []
        for i in range(len(num_str)-1, -1, -8):
            byte = num_str[max(i-7, 0):i+1]
            self.arr.append(int(byte, 16))

    def get_number(self):
        num_str = ""
        for byte in self.arr[::-1]:
            num_str += hex(byte)[2:].zfill(8)
        return num_str.upper()


# автоматичне тестування
num1 = "1234567890ABCDEF"
big_num1 = BigInt(num1)
assert big_num1.get_number() == num1

num2 = "FEDCBA0987654321"
big_num2 = BigInt(num2)
assert big_num2.get_number() == num2

num3 = "1"
big_num3 = BigInt(num3)
assert big_num3.get_number() == num3

num4 = "100000000"
big_num4 = BigInt(num4)
assert big_num4.get_number() == num4

num5 = "1234567890ABCDEF1234567890ABCDEF"
big_num5 = BigInt(num5)
assert big_num5.get_number() == num5