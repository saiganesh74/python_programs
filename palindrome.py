word = input("Enter a string to check whether it is a palindrome or not :")
class Pali_checker():
    def __init__(self, word):
        self. a = word
        if self.a == self.a[::-1]:
            print(f"{self.a} a palindrome")
        else:
            print(f"Sorry, {self.a} isn't a  palindrome")
p = Pali_checker(word)
