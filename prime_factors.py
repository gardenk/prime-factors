

class PrimeFactor:
    def forward(self, n):
        factors = []
        divisor = 2
        while n > 1:
            while not n % divisor:
                factors.append(divisor)
                n //= divisor
            divisor += 1
        return factors
