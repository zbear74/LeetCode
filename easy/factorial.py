def fac(self,n: int) -> int:
    print("Iiteration =" ,n)
    if n < 1:
        return 1
    return self.fac(n-1) * n
    