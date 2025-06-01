class Even_odd():
    def __init__(self,a):
        self.a = a 
    def checker(self):
        if(self.a%2 ==0):
            print(f"{self.a} is an even number")
        else :
            print(f"{self.a} is a odd number")
a = int(input("Enter a number to check whether it is even or odd : "))
num = Even_odd(a)
num.checker()
