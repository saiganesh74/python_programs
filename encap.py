class encapsulated():
    def __init__(self):
        self.var = 0 
    def deposit(self,money):
        self.var += money
    def print(self):
        print(f"The money that account holds is :{self.var}")
e= encapsulated()
e.deposit(10000)
e.print()