year = int(input("Enter a year to check for leap year :"))
class leap():
    def __init__(self,year):
        self.year = year
    def count(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            print("Its a leap year")
        else :
            print("its not a leap year") 
l = leap(year)
l.count()