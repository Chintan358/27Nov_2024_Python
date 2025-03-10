import Banker as b
import Customer as c
choice=0
while choice!=3:
    print("""
                    WELCOME TO PYTHON BANK MANAGEMENT SYSTEM
                    select Your role :
                    1 : Banker
                    2 : customer
                    3 : Exit
    """)

    choice = int(input("Enter Your Choice : "))

    if choice==1 : 
        b.bankerperation()
    elif choice==2 :
        c.customeroperations()
    elif choice==3:
        print("Exit !!!")
    else:
        print("Invalid choice !!!!.")