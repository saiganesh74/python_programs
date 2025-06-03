ch = input("Enter a character to know the value in ASCII :")[0]
class ASC():
    def __init__(self,ch):
        self.ch = ch
    def converter(self):
        res =ord(self.ch)
        print(f"The ASCII value of {self.ch} is :{res}")
a = ASC(ch)
a.converter()