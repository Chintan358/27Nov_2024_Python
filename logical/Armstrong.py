
a  =int(input("Enter nmber to start : "))
b = int(input("Enter number to end : "))
for i in range(a,b):
############countr#################
    # number = int(input("enter number : "))
    number = i
    temp = number
    count = 0
    while number !=0:
        rem = number%10
        number= int(number/10)
        count = count+1


    number = temp

    ############## armstrong ##################
    sum =0
    while number != 0 : 
        rem = number%10
        sum = sum + (rem**count)
        number =int(number/10)
    

    if temp==sum:
        print(f"{temp} is armstrong")
    else :
        pass
        # print(f"{temp} is Not armstrong")
