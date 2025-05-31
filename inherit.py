class Demo():
    def prints(self):
        print("This is parent @demo")
class New(Demo):
    def print123(self):
        print('This is a child @New')
d = New()
d.prints()