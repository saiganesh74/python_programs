class Demo():
    def __init__(self,a='Demo_class'):
        self.a= a
    def display(self):
        print(f"Youre inside a class {self.a}")

d = Demo()
d.display()