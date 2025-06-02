class Transaction:
	def __init__(self, date_time, narration, amount, transaction_type):
                self.date_time = date_time
                self.narration = narration
                self.amount = amount
                self.transaction_type = transaction_type

	def __repr__(self):
                return f"Transaction({self.date_time}, {self.narration}, {self.amount}, {self.transaction_type}"


class Account:
	def __init__(self, account_number):
                self.__account_number = account_number  
                self.__balance = 0.0 
                self.transactions = []  

	def deposit(self, amount, narration="Deposit"):
                if amount > 0:
                        self.__balance += amount
                        transaction = Transaction(narration, amount, "Deposit")
                        self.transactions.append(transaction)
                        print(f"Deposited: {amount}. New balance: {self.get_balance()}")
                else:
                        print("Deposit amount must be positive.")

	def withdraw(self, amount, narration="Withdrawal"):
                if 0 < amount <= self.__balance:
                        self.__balance -= amount
                        transaction = Transaction(narration, amount, "Withdrawal")
                        self.transactions.append(transaction)
                        print(f"Withdrew: {amount}. New balance: {self.get_balance()}")
                else:
                        print("Insufficient funds or invalid withdrawal amount.")

	def get_balance(self):
                return self.__balance

	def get_account_number(self):
                return self.__account_number

	def get_transactions(self):
                return self.transactions
