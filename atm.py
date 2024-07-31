class Atm:
    def __init__(self) -> None:
        self.balance = 0
        self.pin = ""
        self.show_user_options()
        
    def show_user_options(self):
        while True:
            option = int(input('''
              1. Enter 1 to create pin
              2. Enter 2 to deposit
              3. Enter 3 to withdraw
              4. Enter 4 to check balance
              5. Enter 5 to exit
              '''))
            if option == 1:
                print("⚡Create PIN")
                self.create_pin()
            elif option == 2:
                print("⚡Deposit Amount")
                self.deposit()
            elif option == 3:
                print("⚡Withdraw Amount")
                self.withdraw()
            elif option == 4:
                print("⚡Check Balance")
                self.check_balance()
            elif option == 5:
                print("Bye")
                break
            else:
                print("Invalid option, please try again.")
               
    def create_pin(self):
        new_pin = int(input(f"Enter your new PIN : "))
        self.pin = new_pin
        print(f"Pin set successfully")
        
    def deposit(self):
        deposit = int(input(f"Enter amount to deposit : "))
        self.balance += deposit
        print(f"Deposit Successful")
        
    def withdraw(self):
        withdraw_amount = int(input(f"Enter amount to withdraw : "))
        entered_pin = int(input(f"Enter your PIN : "))
        if entered_pin == self.pin:
            if withdraw_amount > self.balance:
                print(f"Insufficient funds to withdraw")
            else:
                self.balance -= withdraw_amount
                print(f"Withdraw Successul")
        else:
            print(f"You entered wrong PIN")
            
    def check_balance(self):
        entered_pin = int(input("Enter your PIN to check balance"))
        if entered_pin == self.pin:
            print(f"Your balance is : {self.balance}")
        else:
            print(f"You have entered wrong PIN")
        
    