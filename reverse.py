str = input("Enter a string to reverse :")
class Reversal():
    def __init__(self,str):
        self.str = str 
        self.str = self.str[::-1]
        print(self.str)
r = Reversal(str)
