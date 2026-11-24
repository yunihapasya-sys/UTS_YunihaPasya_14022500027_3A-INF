class BankAccount:
    no = ""
    balance = 0
    active = "Benar"

    def __init__(self, no, balance=0): #Manual setup
        self.no = no
    
        if balance <=10000:
            self.balance = balance
            self.active = "Benar"
        else:
            self.balance = 0
            self.active = "Salah"
        
    @classmethod
    def disabled(cls, no, balance=0):
        result = cls(no, balance)
        result.active = "Salah"
        result.balance = 0
        return result

bank_account1 = BankAccount("1", 10000)
bank_account2 = BankAccount.disabled("2",20000)
print(f"Bank account {bank_account1.no} has balance {bank_account1.balance} and status {bank_account1.active}")
print(f"Bank account {bank_account2.no} has balance {bank_account2.balance} and status {bank_account2.active}")
