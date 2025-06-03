ch = input("Enter a alphabet to check whether it is a vowel or not :")[0]
class Vowe():
    def __init__(self, a):
        self.a = a
        if (self.a == 'a' or self.a=='e' or self.a=='i' or self.a=='o' or self.a=='u' or self.a == 'A' or self.a=='E' or self.a=='I' or self.a=='O' or self.a=='U'):
            print(f"{self.a} is a vowel :)")
        else:
            print(f"{self.a} is not a vowel :(")
v = Vowe(ch)