class BankATM:
    def __init__(self, balance, username):
        self.balance = balance
        self.username = username
    
    def withdraw(self, amount):
        if (amount < 0):
            print("use deposit to deposit")
            return
        self.balance -= amount
        print("Withdrawn $" + str(amount))
    
    def deposit(self, amount):
        if (amount < 0):
            print("use withdraw to withdraw")
            return
        self.balance += amount
        print("Deposited $" + str(amount))
    
    def printStats(self):
        print("\n\n   ---  BANK ACCOUNT STATS  ---\n        - balance: " + str(self.balance) + "\n   ----------------------------\n\n")


def example():
    acc = BankATM(1000, "Person")
    acc.printStats()
    acc.deposit(100)
    acc.printStats()
    acc.withdraw(200)
    acc.printStats()
    acc.deposit(1000000)
    acc.printStats()

example()