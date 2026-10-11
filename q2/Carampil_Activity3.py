class BankAccount:
    def __init__(self, accountNumber, balance):
        self.__balance = balance
        self.__accountNumber = accountNumber

    @property
    def balance(self):
        return f"Balance: {self.__balance:.2f}"
        

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance must not be a negative number")

    @property
    def account_number(self):
        return f"Account Number: {self.__accountNumber}"

    @account_number.setter
    def account_number(self, accountNumber):
        self.__accountNumber = accountNumber

a1 = BankAccount("12345", 1000)

print(a1.balance)
print(a1.account_number)
a1.balance = -100
print(a1.balance)