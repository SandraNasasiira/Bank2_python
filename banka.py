class Account:

    def __init__(self,name,phone,account_number):
              self.name=name
              self.phone=phone
              self.account_number=account_number
              self.balance=0
              self.loan=loan
              self.loan_limit=
    def deposit(self,amount):
        self.balance+=amount
        return f"hello {self.name},you have deposited{amount}to your account.Your new balance is{self.balance}"
    def show_balance(self):
        return self.balance

    def withdraw(self,amount):
        if amount<0:
            return f"you can't withdraw"
        elif amount>self.balance:
            return f"you have insufficient balance"
        else:
            self.balance-= amount
            return f"hello {self.name},you have withdrawn{amount} from account number{self.account_number} amd your balance is{self.balance} "
    def borrow(self,amount):
        if amount>=self.loan_limit:
      return f"Dear {self.name}, the amount you are trying to borrow is above your loan limit, please deposit more to increase your loan limit"
    elif self.loan>0:
      return f"Dear {self.name}, You still have not cleared your loan, please clear your outstanding debts so that you can borrow more thank you."
    elif amount<=0:
      return f"Dear {self.name}, You do not have enough to borrow"
    else:
      self.loan=1
      self.balance+=amount
      return f"Dear {self.name}, You have successfully borrowed {amount}. Your new balance is {self.balance}"
    
