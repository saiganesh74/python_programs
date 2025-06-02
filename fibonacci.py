# 0 1 1 2 3 5 8 
n = int(input("Enter the number : "))
class Fibo():
    def __init__(self,n):
        self.n = n 
    def fibonacci(self):
        print(self.n + (self.n-1))
f = Fibo(n)
f.fibonacci()