import random 
class Dicing():
    def __init__(self):
        user_input = input("Enter any key to roll a dice !!")
        if user_input:
            a = random.randint(1,6)
            print(a)
        else:
            print("Invalid ! No key entered")
d = Dicing()    