from functools import reduce  

# def add(x):
#     return x+1

# def multiply(x):
#     return x*2

# def apply(func,x) :
#     return func(x)

# result = apply(add, 5)
# result = apply(multiply, 5)
# print(result)

# add = lambda x:x+1
# multiply = lambda x : x*2

# result = add(2)
# print(result)


#map

l = [0,1,2,3,4,5]


# result = map(lambda x:x*2,l)
# print(list(result))

# result  =filter(lambda x :x%2==0,l)
# print(list(result))

# result = reduce(lambda x, y: x + y, l)
# print(result)

# data1 = list(map(str,input("Enter integer values: ").split()))  
# print(data1)

# base = [10,20,30]
# power = [2,3,4]

# # k = map(lambda x,y:x**y,base,pow)
# k = map(pow,base,power)
# print(list(k))


from math import sqrt

data = [1,4,9,16,25,41,5,8,66]

# result = map(sqrt,data)
# print(list(result))

def isquare(x):
    return sqrt(x).is_integer()

# k =  filter(isquare,data)

# print(list(k))