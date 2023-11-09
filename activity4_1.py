class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit: ${amount}. New Balance: {self.balance}")
        else:
            print("Invalid Deposit Amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw: ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid Withdrawal amount or insufficient funds")

    def check_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.balance}")

tuloy = True

Accounts = []

while tuloy == True:
    print("1 - Create a Bank account")
    print("2 - Deposit")
    print("3 - withdraw")
    print("4 - check balance")
    print("5 - exit")
    choice = eval(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter a new Account Holder: ")
        ib = float(eval(input("Enter an initial Balance: ")))
        
        new_account = BankAccount(name, ib)
        Accounts.append(new_account)
        print("Account has been Created")
        
    elif choice == 2:
        account_name = input("Enter the Account Holder Name you want to check --> ")
        money = float(input("How much you want to deposit? --->"))
        for every_account in Accounts:
            if every_account.account_holder == account_name:
                every_account.deposit(money)
            else:
                print("Account does not exist")

    elif choice == 3:
        account_name = input("Enter the Account Holder Name you want to check --> ")
        money = float(input("How much you want to withdraw? --->"))
        for every_account in Accounts:
            if every_account.account_holder == account_name:
                every_account.withdraw(money)
            else:
                print("Account does not exist")

    elif choice == 4:
        account_name = input("Enter the Account Holder Name you want to check --> ")
        for every_account in Accounts:
            if every_account.account_holder == account_name:
                every_account.check_balance()
            else:
                print("Account does not exist")
        
    elif choice == 5:
        print("Exit Transaction")
        tuloy == False
        break