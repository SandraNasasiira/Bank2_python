from datetime import datetime

class Account():


    def __init__(self,name,phone,loan_limit):
              self.name=name
              self.phone=phone
              self.balance=0
              self.loan_limit=loan_limit
              self.transactions=[]
              self.withdrawal=[]
              self.save_loan=[]
              
    def deposit(self,amount):
        if amount<=0:
             return f"hello {self.name},you have deposited {amount} to your account.Your new balance is {self.balance}"
        else:
             self.balance+=amount
             transactions={"amount":amount, "balance":self.balance ,"time":datetime.now(),"narration":"Deposit"}
             self.transactions.append(transactions)

             return f"hello {self.name},you have deposited {amount} to your account.Your new balance is {self.balance}"

    def show_balance(self):
             return self.balance

    def withdraw(self,amount):
        if amount<0:
             return f"you can't withdraw"
        elif amount>self.balance:

             return f"you have insufficient balance"
        else:
             self.balance-= amount
             return f"hello {self.name},you have withdrawn{amount} and your balance is{self.balance} "
    def borrow(self,amount):
        if  amount>=self.loan_limit:
             return f"Dear {self.name}, the amount you are trying to borrow is above your loan limit, please deposit more to increase your loan limit"
        elif self.loan>0:
             return f"Dear {self.name}, You still have not cleared your loan, please clear your outstanding debts so that you can borrow more thank you."
        elif amount<=0:
             return f"Dear {self.name}, You do not have enough to borrow"
        else:
             self.loan=1
             self.balance+=amount
             return f"Dear {self.name}, You have successfully borrowed {amount}. Your new balance is {self.balance}"

    def get_statement(self):
      for transaction in self.transactions:
            narration=transaction["narration"]
            amount   =transaction["amount"]
            balance  =transaction["balance"]
            time     =transaction["time"]
            print(f"{time.strftime('%D')}....{narration}....{amount}....Balance{balance}")

      for withdrawal in self.withdrawal:
           narration=withdrawal["narration"]
           amount   =withdrawal["amount"]
           balance  =withdrawal["balance"]
           time     =withdrawal["time"]
           print(f"{time.strftime('%D')}....{narration}....{amount}....Balance{balance}")

      for save_loan in self.save_loan:
           narration=save_loan["narration"]
           amount   =save_loan["amount"]
           balance  =save_loan["balance"]
           time     =save_loan["time"]
           print(f"{time.strftime('%D')}....{narration}....{amount}....Balance{balance}")
    def loan_payment(self,amount):
          if amount<0:
                return f"please put a positive amount"
          elif amount<self.loan:
              self.loan-=amount:
                return f"Dear {self.name} you have paid {amount} on your loan"
          else:
              difference=amount-self.loan
              self.balance+=difference
                return f"dear {self.name}you have fully paid your loan and your balance is{self.balance}"
    for loan_payment in self.save_loan:
           narration=loan_payment["narration"]
           amount   =sloan_payment["amount"]
           loan_payment =loan_payment["loan_payment"]
           time     =loan_payment["time"]
           print(f"{time.strftime('%D')}....{narration}....{amount}....Balance{balance}")
