a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

class Big():
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b 
        self.c = c 
    def biggest(self):
        if(self.a > self.b) and (self.a > self.c):
            print(f"{self.a} is greater among three numbers")
        elif(self.b > self .a and self.b > self.c ):
            print(f"{self.b} is greater among three numbers")
        else:
            print(f"{self.c} is greater among the numbers")
b = Big(a,b,c)
b.biggest()