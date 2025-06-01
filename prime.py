a = int(input("Enter a value to check whether it is prime or not : "))
class Prime_number():
    def __init__(self,a):
        self.a = a
    def checker(self):
        if(self.a<= 1):
            print(f"{self.a} is not a prime number because 1 isnt a natural number")
        else:
            if(self.a % 2 ==0 ):
                print(f"{self.a} is not a prime number")
            else:
                print(f"{self.a} is a prime number ")
p = Prime_number(a)
p.checker()
