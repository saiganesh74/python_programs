arr = list(map(int,input("Enter list of numbers to add them up using array :").split()))
class Adding_array():
    def __init__(self,arr):
        self.arr = arr 
    def adder(self):
        tota = 0 
        for num in self.arr:
            tota +=num 
        print(f"The total sum of {self.arr} is : {tota}")
c = Adding_array(arr)
c.adder()