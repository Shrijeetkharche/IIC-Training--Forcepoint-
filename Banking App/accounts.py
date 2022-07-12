from bank import Bank

class Accounts:
    accountId = -1
    def __init__(self, bank, balance):
        """Constructor."""
        self.bank = bank
        self.balance = balance
        self.accountId = Accounts.accountId

    def isAccountExist(self, bankAbbrv):
        """To check the presence of account."""
        return self.bank.bankAbbrv == bankAbbrv

    def displayBalance(self):
        """To display the balance."""
        print(self.bank.bankAbbrv, "Balance is: ", self.balance)

    def isSufficientBalance(self, amount):
        """To check the minimum balance."""
        return self.balance >= amount

    @staticmethod
    def createNewAccount(bankAbbrv, ):
        """To create a new account"""
        isBankExist, bankObject = Bank.findBank(bankAbbrv)
        if not isBankExist:
            return False, "Bank does not exist"
        Accounts.accountId+=1
        newAccount = Accounts(bankObject, 1000)
        return True, "Account Created"