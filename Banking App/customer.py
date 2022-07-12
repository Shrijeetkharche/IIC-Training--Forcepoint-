from accounts import Accounts

class Customer:
    customerID = -1
    allCustomer = []

    def __init__(self, fName, lName, userName):
        self.fName = fName
        self.lName = lName
        self.totalBalance = 0
        self.customerId = Customer.customerId
        self.userName = userName
        self.accounts = []

    def deposit(self, amount, bankAbbrv):
        isAccountExist, account = self.findAccount(bankAbbrv)
        if not isAccountExist:
            return False, "Account does not exist"
        account.balance += amount
        self.__updateTotalBalance()
        self.displayBalance()
        return True, "Amount Deposited."

    def withdraw(self, amount, bankAbbrv):
        isAccountExist, account = self.findAccount(bankAbbrv)
        if not isAccountExist:
            return False, "Account does not exist"
        if not account.isSufficientBalance(amount):
            return False, "Insufficient Balance"
        account.balance -= amount
        self.__updateTotalBalance()
        self.displayBalance()
        return True, "Amount Withdrawn."

    def transferAmount(self, creditCustomerUsername, creditBankAbbrv, debitbankAbbrv, amount):
        iscreditCustomerExist, creditCustomer = Customer.findCustomer(creditCustomerUsername)
        if not iscreditCustomerExist:
            return False, "Credit Customer doesnot exist"

        flag1, message = self.withdraw(amount, debitbankAbbrv)
        if flag1:
            flag2, _ = creditCustomer.deposit(amount, creditBankAbbrv)
            return True if flag2 else self.deposit()

    def selfTransfer(self, creditbankAbbrv, debitbankAbbrv, amount):
        self.transferAmount(self.userName, creditbankAbbrv, debitbankAbbrv, amount)
        return True

    def __updateTotalBalance(self):
        self.totalBalance = 0
        for a in self.accounts:
            self.totalBalance += a.balance

    def findAccount(self, bankAbbrv):
        if len(self.accounts) == 0:
            return False, "No accounts found!"

        for a in self.accounts:
            if a.isAccountExist(bankAbbrv):
                return True, a
            return False, None

    def displayBalance(self):
        print(self.fname, "Total Balance is: ", self.totalBalance)
        for a in self.accounts:
            a.displayBalance()

    def createNewAccount(self, bankAbbrv):
        isAccountExist, account = self.findAccount()
        if isAccountExist:
            return False, "Your account already exist"
        isAccountCreated, account = Accounts.createAccount(bankAbbrv)
        if not isAccountCreated:
            return False, "Account not created, Retry!"
        self.accounts.append(account)
        return True, "Account Created"

    @staticmethod
    def findCustomer(userName):
        for u in Customer.allCustomer:
            if u.userName == userName:
                return True, u
        return False, None

    @staticmethod
    def createNewCustomer(fName, lName, userName):
        isCustomerExist, customer = Customer.findCustomer(userName)
        if isCustomerExist:
            return False, "Username already Exist"
        Customer.customerId += 1
        newCustomer = Customer(fName, lName, userName)
        Customer.allCustomer.append(newCustomer)
        return True, "Customer Created!"

