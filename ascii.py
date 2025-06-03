ch = input("Enter a character to know the value in ASCII :")
class ASC():
    def __init__(self,ch):
        self.ch = ch
    def converter(self):
        res =ord(self.ch)
        print(f"The ASCII value of entered character is :{res}")
a = ASC(ch)
a.converter()