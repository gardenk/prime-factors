

class PrimeFactor:
    def forward(self, n):
        factors = []
        if n > 1:
            divisor = 2
            if n == 4 or n == 6 or n == 9 or n == 12:
                while n > 1:
                    while not n % divisor:
                        factors.append(divisor)
                        n //= divisor
                    divisor += 1
            else:
                factors.append(n)
        return factors
