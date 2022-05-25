class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        print("Welcome to the atm")
        self.startAtm()
    def startAtm(self):
        print('''
                ==============Please Choose Your Option==============
                Enter 1 : To set pin.
                Enter 2 : To check balance.
                Enter 3 : To add balance.
                Enter 4 : To withdraw balance.
                Enter 5 : To exit.
             ''')
        option = int(input("Enter your option"))
        if option == 1:
            self.setPin()
            self.startAtm()
        elif option == 2:
            if self.pin == "":
                print("Please set pin first.")
                self.setPin()
            self.checkBalance()
            self.startAtm()
        elif option == 3:
            if self.pin == "":
                print("Please set pin first.")
                self.setPin()
            self.addBalance()
            self.startAtm()
        elif option == 4:
            if self.pin == "":
                print("Please set pin first.")
                self.setPin()
            self.withDrawBalance()
            self.startAtm()
        elif option == 5:
            print("Exiting......")
        else:
            print("Wrong command")
            self.startAtm()
    def setPin(self):
        self.pin = input("Set a pin.")
    def checkBalance(self):
        print("Your balance is: ", self.balance)            
    def addBalance(self):
        self.balance += float(input("Enter balance"))
    def withDrawBalance(self):
        userPin = input("Please enter a pin.")
        if userPin == self.pin:
            print("Your total balance is : ", self.balance)
            reqBal = float(input("Enter balance you want to withdraw."))
            if reqBal < self.balance:
                self.balance = self.balance - reqBal
                print("Balance withdrawn: ",reqBal, "Total Balance : ",self.balance)
            else:
                print("Insufficient Balance")
        else:
            print("Wrong pin.")
        
        
    
