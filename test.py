

# x = 20
# def test():
#     global x  # Declare x as a global variable
#     x = 10
#     print(x)


# print(x)  #20
# test()  #20
# print(x) #20


def test():
    x = 10  # Local variable
    
    def inner():
        nonlocal x
        x = 20
        print(x)
    
    print(x)  # 10
    inner()
    print(x)  # 20


test()  # 10