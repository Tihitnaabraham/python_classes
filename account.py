from datetime import datetime
class Transaction:
    def __init__(self, narration, amount, transaction_type):
        self.date_time = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type

    def __report__(self):
        return f"Transaction({self.date_time.reportftime('%Y-%m-%d %H:%M:%S')} | {self.naration}:  {self.amount} | {self.transaction_type.title() })"



class Account:
    def __init__(self,name):
      
        self.name=name
        self.__balance =0
        self.transactions=[]
        self.deposits=[]
        self.withdraws=[]
        self.transfers=[]
        self.transaction_fee= 100
        self.loan_amount=0
        self.loan_amount=0
        self.frozen = False
      
# Deposit: method to deposit funds, store the deposit and return a message with the new balance to the customer. It should only accept positive amounts.
      
    def deposit(self,amount):
        self.deposits.append(amount)
        if amount<=0:
            return "deposite amount must be positive"
        else:
            transaction = Transaction("Deposit to account",amount,"deposit")
            self.transactions.append(transaction)
            self.__balance+=amount
            
            return f"hello{self.name},you have recieved {amount}.your new balance is {self.__balance}"
# Withdraw: method to withdraw funds, store the withdrawal and return a message with the new balance to the customer. An account cannot be overdrawn.

        
    def withdraw(self, amount,narration="Withdrawal"):
        self.withdraws.append(amount)
        if amount>(self.__balance-self.transaction_fee):
            return f"hello{self.name},you can not wirhdraw,you have insufficient balace"
        else:
            transaction=Transaction("withdraw from account",amount,"Withdrawal")
            self.transactions.append(transaction)
            self.__balance-=amount
            return f"hello{self.name},you have withdrawn {amount},your balance is{self.__balance}"
# Transfer Funds: Method to transfer funds from one account to an instance of another account.
    def transfer(self, amount,other_account):
        self.transfers.append(amount)
        if amount <= 0:
            return "Transfer amount must be positive."
        elif amount>(self.__balance - self.transaction_fee):
            return "Insufficient balance for transfer."
        else:
            self.withdraw(amount)
            transaction=Transaction("transfer to account",amount,"transfer")
            self.transactions.append(transaction)
            self.__balance-=amount
            
            return f"${amount} transferred to {other_account} new balance is ${self.__balance}"
# Get Balance: Method to calculate an account balance from deposits and withdrawals.
    def get_balance(self):
        return f"current balance is {self.__balance}"
# Request Loan: Method to request a loan amount.
    def request_loan(self,amount):
        if amount<=0:
            return "loan amount must be positive"
        else:
            transaction=Transaction("requested loan",amount,"request loan")
            self.transactions.append(transaction)
            self.loan_amount+=amount
            self.__balance+=amount
            
            return f"loan of {amount} taken, new balance is {self.__balance}"
# Repay Loan: Method to repay a loan with a given amount.
    def repay_loan(self,amount):
        if amount<=0:
            return "repay loan amount must be positive"
        elif amount>self.loan_amount:
            return "amount exceed the loan"

        else:
            transaction=Transaction("repaied",amount,"repay")
            self.transactions.append(transaction)
            self.loan_amount-=amount
            self.__balance-=amount
            
            return f"you have remaining amount{self.loan_amount} "
# View Account Details: Method to display the account owner's details and current balance.
    def account_details(self):
        return f"name={self.name} and current balance is {self.__balance}"
        # Change Account Owner: Method to update the account owner's name.
    def change_account_owner(self, new_owner):
        return f"Account owner changed to {new_owner}."
# Account Statement: Method to generate a statement of all transactions in an account. (Print using a for loop).
    def statement(self):
        print(f"Account statemet for {self.name}")
        for transaction in self.transactions:
            print (transaction)
            

        
# Interest Calculation: Method to calculate and apply an interest to the balance. Use 5% interest. 
    def apply_interest(self):
        interest = self.__balance * 0.05
        self.balance += interest
        return f"Interest of {interest} applied new balance is {self.__balance}"
# Freeze/Unfreeze Account: Methods to freeze and unfreeze the account for security reasons.
    def freeze_account(self):
        self.frozen = True
        return "Account has been frozen."
    def unfreeze_account(self):
        self.frozen = False
        return "Account has been unfrozen."
 # Set Minimum Balance: Method to enforce a minimum balance requirement. You cannot withdraw if your balance is less
    def set_minimum_balance(self, amount):
        if amount >=1:
            self.minimum_balance = amount
            return f"Minimum balance set to {amount}."
        else:
            return "Minimum balance should be positive."
            
 # than this amount.Close Account: Method to close the account and set all balances to zero and empty all transactions.

    def close_account(self):
        self.__balance = 0
        self.loan_amount = 0
        self.loan_repaid = 0
        self.wirhdraws=[]
        self.deposits=[]
        return "Account closed. All balances set to zero."
    def get_transactions(self):
        return self.transactions
    

