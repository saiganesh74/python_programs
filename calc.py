a= int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
c = input("Enter an operation to perform (+,-,*,/) :")
class Calc():
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b
        self.c = c
    def calculator(self):
        if(self.c == '+'):
            print(self.a + self.b)
        elif(self.c == '-'):
            print(self.a - self.b)
        elif(self.c == '*'):
            print(self.a * self.b) 
        else:
            print(self.a / self.b)
ca = Calc(a,b,c)
ca.calculator()