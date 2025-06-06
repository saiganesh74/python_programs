arr = list(map(int,input("Enter numbers (Comma separated) to store in array and find largest number :").split()))
class Arr_lar():
    def __init__(self,arr):
        self.arr = arr
    def array_largest(self):
        self.arr = max(self.arr)
        print(self.arr) 
a = Arr_lar(arr)
a.array_largest()