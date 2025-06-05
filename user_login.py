user_name = 'admin'
password = 'admin' 
attempts = 3
class Logger():
    def __init__(self,user_name , password , attempts):
        self.user = user_name
        self.password = password
        self.attempts = attempts
        while self.attempts>0 and self.attempts <=3 :
            str1 = input("Enter User name :")
            str2 = input("Enter Password :")
            if str1 == self.user and str2== self.password:
                print("Logged in sucessfully !!")
                break
            else:
                self.attempts = self.attempts - 1
                print(f"Invalid credintials !! Attempts left : {self.attempts}")
            if self.attempts == 0 :
                print("Attempts exceeded !!")
                break
            
l = Logger(user_name, password ,attempts)