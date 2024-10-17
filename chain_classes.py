
class SavingAccount(BankAccount):
    pass

class CheckingAccount(BankAccount):
    pass

class Security:
    pass

class Stock(Security):
    pass

class Bond(Security):
    pass

class RealEstate:
    pass

class Asset(BankAccount, RealEstate, Security):
    pass

class InsurableItem(BankAccount, RealEstate):
    pass

class InterestBearingItem(BankAccount, Security):
    pass
