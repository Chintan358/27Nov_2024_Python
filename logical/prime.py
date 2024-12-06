
for j in range(3,101) :

    num = 5
    flag = 0


    for i in range(2,num):
        if num%i==0:
            flag=1
            break

    if flag==0:
        print(f"{num} is prime")
    else : 
        pass
        # print(f"{num} is not prime")