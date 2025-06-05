str1 = input("Enter first string :").lower()
str2 = input("Enter second string :").lower()
class Ana():
    def __init__(self,str1 , str2):
        self.a = str1
        self.b = str2
        if sorted(str1)== sorted(str2):
            print("These two are anagrams")
        else:
            print("These aren't anagrams")
a = Ana(str1,str2)