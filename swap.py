a = int(input("Enter first number to swap :"))
b = int(input("Enter second number to swap :"))
print(f"The values before swapping are {a} and {b}")
class Swapper():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def swapping(self):
        self.a , self.b = self.b , self.a
        print(f"The values after swapping are {self.a} and {self.b}")
s = Swapper(a,b)
s.swapping()