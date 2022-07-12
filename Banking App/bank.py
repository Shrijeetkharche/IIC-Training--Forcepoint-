class Bank: 
    bankId = -1
    allBanks = []
    def __init__(self, fullName, bankAbbrv):
        """Constructor"""
        self.fullName = fullName
        self.bankAbbrv = bankAbbrv
        Bank.bankId += 1
        self.bankId = Bank.bankId

    @staticmethod
    def findBank(bankAbbrv):
        """Check the presence of bank."""
        for i in Bank.allBanks:
            if i.bankAbbrv == bankAbbrv:
                return True,i
        return False, None

    @staticmethod
    def createNewBank(fullName, bankAbbrv):
        """To create a new bank object."""
        isBankExist, bankObject = Bank.findBank(bankAbbrv)
        if not isBankExist:
            return False, "Bank bankAbbrv alrady exist"
        if bankObject.fullName == fullName:
            return False, "Bank full name alrady exist"

        newBank = Bank(fullName, bankAbbrv)
        Bank.allBanks.append(newBank)
        return True, "Bank Created!"