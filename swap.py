a = int(input  ("Enter first value :"))
b = int(input("Enter second value :"))

class swap():
    def __init__(self,a,b):
        self.a = a 
        self.b = b
        print(f"First value {self.a}")
        print(f"Second value {self.b}")
    def log(self):
        temp = self.a
        self.a = self.b 
        self.b = temp
        print(self.a)
        print(self.b)
s = swap(a,b)
s.log()