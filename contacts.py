contacts  ={}
while True:
    print("Select an option to continue: \n 1. Add Contact \n 2.View All \n 3. Search \n 4. Exit ")
    choice = input("Enter Choice :")
    if choice== '1':
        name = input("Enter Name :")
        number = int(input("Enter number :"))
        contacts[name]= number
        print("Details entered sucuessfully !!!")
    elif choice=='2':
        for name, number in contacts.items():
            print(f"Name : {name} \n Phone number : {number} ")
    elif choice=='3':
        search = input("Enter name to search :")
        print("Found :",contacts.get(search , "Not Found"))
    elif choice=='4':
        print("Exiting Contact Book boiii boii")
        break
    else: 
        print("Invalid Option") 