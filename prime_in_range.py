a = int(input("Enter the starting of range :"))
b = int(input("Enter the end of range :"))
class PIR():
    def __init__(self,a,b):
        self.a = a 
        self.b = b
        for num in range(self.a, self.b+1):
            if num>1:
                is_prime = True
                for i in range (2,num):
                    if num% i == 0: 
                       is_prime = False 
                if is_prime:
                    print(num)
p = PIR(a,b)