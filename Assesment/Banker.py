d1 = []
def bankerperation():
    print("Welcome To bankers App : ")

    choice = "y"
    while choice != "n":

        print("""

            Operation mennu : 
            1 : Add customer
            2 : View Customer
            3 : Search customer
            4 : Total amount in bank
    """)
        
        
        menu = int(input("Enter operation which you want to perform : "))
        
        if menu ==1 : 
            acno = int(input("Enter account number : "))
            name = input("enter name : ")
            balance = float(input("enter amount : "))
            d1.append({"acno":acno,"name":name,"balance":balance}) 
        elif menu==2:
            print(d1) 
        elif menu==3:
            acno_search = int(input("Enter accocunt no. to search : "))
            for i in d1:
                if i['acno']==acno_search:
                    print(i)
        elif menu==4:
            total = 0
            for j in d1:
                total += j['balance']

            print("Total amount in Bank : ",total)
        else:
            print("Invalid Choice : ")
            
        
        choice = input("do u want to continue? y / n")      

