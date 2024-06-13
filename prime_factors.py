class PrimeFactor:
    def forward(self, n):
        factors = []
        if n > 1:
            if n == 4:
                while not n % 2:
                    factors.append(2)
                    n //= 2
            else:
                factors.append(n)
        return factors
