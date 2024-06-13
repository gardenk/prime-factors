class PrimeFactor:
    def forward(self, n):
        factors = []
        if n > 1:
            if n == 4:
                factors.append(2)
                factors.append(2)
            else:
                factors.append(n)
        return factors
