import random
a = int(input("Take a random guess between 1 to 10 :"))
guess = random.randint(1,10)
class Game():
    def __init__(self,a,guess):
        self.a = a 
        self.guess = guess
    def gamer(self):
        if a== random :
            print("You guessed the right one")
        else :
            print("U are incorrect :(")
g = Game(a,guess)
g.gamer()