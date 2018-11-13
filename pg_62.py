def Hello():
    print("Welocme to Python")
    num = 0
    while num < 5:
        print("Number is "+str(num))
        num+=1
        

def Login():
    print("Enter User Name:")
    username=input()
    password=input("Enter Password")
    if username=='sadiq' and password=='baloch':
        print('Welocme to login page')
    else:
        print('Password and username are incorrect')
        
    
Hello()
Login()