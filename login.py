def login():
    i=0
    while (i<3):
        username=input("Enter your username")
        password=input("Enter your password")
        if(username=='admin'):
            if(password=='admin'):
                return 1
            else:
                print("wrong password")
        else:
            print("Wrong username")
        i=i+1
    else:
        print("You have tried maximum 3 attempts")