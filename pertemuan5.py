class BankAccount:
    no = ""
    saldo = 0

    def __init__(self, no, saldo=0):
        #validasi saldo
        if saldo < 0:
            raise ValueError("gagal")
        self.no = no
        self.saldo = saldo
        
martin = BankAccount("1234567", 10000) #sukses
print(f"martin ({martin.no}) saldo: {martin.saldo}")

try:
    eko = BankAccount("1234567", -1000) #error
    print(f"eko ({eko.no}) saldo: {eko.saldo}")
except ValueError as e:
    print(f"eko tidak memiliki saldo ({e})")
