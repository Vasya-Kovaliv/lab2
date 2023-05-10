class BigInt:
    def init(self, value):
        self.value = value

    def str(self):
        return str(self.value)

    def add(self, other):
        max_len = max(len(self.value), len(other.value))
        self.value = self.value.zfill(max_len)
        other.value = other.value.zfill(max_len)
        result = ''
        carry = 0
        for i in range(max_len - 1, -1, -1):
            temp_sum = int(self.value[i]) + int(other.value[i]) + carry
            result = str(temp_sum % 10) + result
            carry = temp_sum // 10
        if carry:
            result = str(carry) + result
        return BigInt(result)

    def sub(self, other):
        max_len = max(len(self.value), len(other.value))
        self.value = self.value.zfill(max_len)
        other.value = other.value.zfill(max_len)
        result = ''
        borrow = 0
        for i in range(max_len - 1, -1, -1):
            temp_diff = int(self.value[i]) - int(other.value[i]) - borrow
            if temp_diff < 0:
                temp_diff += 10
                borrow = 1
            else:
                borrow = 0
            result = str(temp_diff) + result
        return BigInt(result.lstrip('0') or '0')

    def mod(self, other):
        dividend = BigInt(self.value)
        divisor = BigInt(other.value)
        quotient = BigInt('0')
        while dividend >= divisor:
            dividend -= divisor
            quotient += BigInt('1')
        return dividend
    # тестування операції додавання


a = BigInt('123456789')
b = BigInt('987654321')
c = a + b
print(c)
# тестування операції віднімання
d = BigInt('987654321')
e = BigInt('123456789')
f = d - e
print(f)